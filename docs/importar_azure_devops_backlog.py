import base64
import csv
import json
import requests

# =========================================================
# CONFIGURACIÓN
# =========================================================
ORGANIZATION = "UMGNoveno"
PROJECT = "ControlTowerLogistics"
PAT = "SU-PATH"

AREA_PATH = PROJECT
DEFAULT_API_VERSION = "7.1"
ITERATION_PREFIX = PROJECT + "\\"
CSV_FILE = "azure_backlog_import.csv"

# Si tu proyecto usa proceso Basic, usa Issue.
# Si usa Agile/Scrum con Feature y User Story, cambia aquí.
TYPE_MAP = {
    "Epic": "Epic",
    "Feature": "Issue",
    "User Story": "Issue",
    "Task": "Task",
}

# =========================================================
# AUTENTICACIÓN
# =========================================================
def auth_header(pat: str) -> dict:
    token = base64.b64encode(f":{pat}".encode("utf-8")).decode("utf-8")
    return {
        "Authorization": f"Basic {token}",
        "Content-Type": "application/json-patch+json",
    }

# =========================================================
# CREAR WORK ITEM
# =========================================================
def create_work_item(item_type: str, title: str, description: str = "", acceptance: str = "",
                     area_path: str = "", iteration_path: str = "") -> int:
    mapped_type = TYPE_MAP[item_type]
    url = f"https://dev.azure.com/{ORGANIZATION}/{PROJECT}/_apis/wit/workitems/${mapped_type}?api-version={DEFAULT_API_VERSION}"

    ops = [
        {"op": "add", "path": "/fields/System.Title", "value": title},
    ]

    if description:
        ops.append({"op": "add", "path": "/fields/System.Description", "value": description})

    # En algunos procesos este campo puede no existir.
    if acceptance and item_type == "User Story":
        ops.append({
            "op": "add",
            "path": "/fields/Microsoft.VSTS.Common.AcceptanceCriteria",
            "value": acceptance
        })

    if area_path:
        ops.append({"op": "add", "path": "/fields/System.AreaPath", "value": area_path})

    if iteration_path:
        ops.append({"op": "add", "path": "/fields/System.IterationPath", "value": iteration_path})

    response = requests.post(url, headers=auth_header(PAT), data=json.dumps(ops))

    # Si falla por AcceptanceCriteria, intenta de nuevo sin ese campo
    if response.status_code >= 400 and acceptance and item_type == "User Story":
        ops = [op for op in ops if op["path"] != "/fields/Microsoft.VSTS.Common.AcceptanceCriteria"]
        response = requests.post(url, headers=auth_header(PAT), data=json.dumps(ops))

    response.raise_for_status()
    return response.json()["id"]

# =========================================================
# ENLAZAR PADRE-HIJO
# =========================================================
def link_parent_child(parent_id: int, child_id: int) -> None:
    url = f"https://dev.azure.com/{ORGANIZATION}/{PROJECT}/_apis/wit/workitems/{child_id}?api-version={DEFAULT_API_VERSION}"
    ops = [
        {
            "op": "add",
            "path": "/relations/-",
            "value": {
                "rel": "System.LinkTypes.Hierarchy-Reverse",
                "url": f"https://dev.azure.com/{ORGANIZATION}/_apis/wit/workItems/{parent_id}",
                "attributes": {"comment": "Vinculado automáticamente por script"}
            }
        }
    ]
    response = requests.patch(url, headers=auth_header(PAT), data=json.dumps(ops))
    response.raise_for_status()

# =========================================================
# CLAVES ÚNICAS
# =========================================================
def build_row_key(row: dict) -> str:
    return f'{row["type"]}|{row.get("parent", "")}|{row["title"]}|{row.get("iteration", "")}'

def find_feature_parent(rows, feature_title: str) -> str:
    for row in rows:
        if row["type"] == "Feature" and row["title"] == feature_title:
            return row.get("parent", "")
    return ""

def find_user_story_row(rows, user_story_title: str) -> dict | None:
    for row in rows:
        if row["type"] == "User Story" and row["title"] == user_story_title:
            return row
    return None

# =========================================================
# MAIN
# =========================================================
def main():
    with open(CSV_FILE, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))

    id_by_key = {}

    # -----------------------------------------------------
    # 1. CREAR TODOS LOS WORK ITEMS
    # -----------------------------------------------------
    for level in ["Epic", "Feature", "User Story", "Task"]:
        for row in rows:
            if row["type"] != level:
                continue

            iteration_path = ""
            if row.get("iteration"):
                iteration_path = ITERATION_PREFIX + row["iteration"]

            wi_id = create_work_item(
                item_type=row["type"],
                title=row["title"],
                description=row.get("description", ""),
                acceptance=row.get("acceptance", ""),
                area_path=AREA_PATH,
                iteration_path=iteration_path
            )

            row_key = build_row_key(row)
            id_by_key[row_key] = wi_id
            print(f"Creado {row['type']}: {row['title']} -> ID {wi_id}")

    # -----------------------------------------------------
    # 2. ENLAZAR JERARQUÍA
    # -----------------------------------------------------
    for row in rows:
        parent_title = row.get("parent", "").strip()
        if not parent_title:
            continue

        child_key = build_row_key(row)
        child_id = id_by_key.get(child_key)

        parent_key = None

        if row["type"] == "Feature":
            # Feature -> Epic
            parent_key = f'Epic||{parent_title}|'

        elif row["type"] == "User Story":
            # User Story -> Feature
            epic_name = find_feature_parent(rows, parent_title)
            parent_key = f'Feature|{epic_name}|{parent_title}|'

        elif row["type"] == "Task":
            # Task -> User Story
            us_row = find_user_story_row(rows, parent_title)
            if us_row:
                parent_key = f'User Story|{us_row.get("parent", "")}|{us_row["title"]}|{us_row.get("iteration", "")}'

        if not parent_key:
            print(f"No se pudo construir parent_key para: {row['title']}")
            continue

        parent_id = id_by_key.get(parent_key)

        if not parent_id:
            print(f"No se encontró parent_id para: {row['title']} | parent_key={parent_key}")
            continue

        if not child_id:
            print(f"No se encontró child_id para: {row['title']}")
            continue

        try:
            link_parent_child(parent_id, child_id)
            print(f"Enlace: {parent_title} -> {row['title']}")
        except requests.HTTPError as ex:
            print(f"Error enlazando {parent_title} -> {row['title']}: {ex}")

    print("Importación completada.")

if __name__ == "__main__":
    main()