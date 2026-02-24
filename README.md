# Introduction

TODO: Give a short introduction of your project. Let this section explain the objectives or the motivation behind this project.

# Getting Started

## Requisitos Previos

- **.NET 9.0 SDK** o superior ([Descargar aquí](https://dotnet.microsoft.com/download))
- **Visual Studio 2022**, **Visual Studio Code** o cualquier editor de código compatible

## Configuración Inicial (Después de Clonar)

Una vez que hayas clonado el repositorio, ejecuta los siguientes comandos en la terminal:

### 1. Navegar a la carpeta del backend
```bash
cd src/backend
```

### 2. Restaurar paquetes NuGet
Este comando descargará todas las dependencias necesarias (librerías):
```bash
dotnet restore
```

### 3. Compilar la solución
```bash
dotnet build
```

### 4. Ejecutar la aplicación
```bash
cd src/ControlTower.Api
dotnet run
```

O desde la raíz de la solución:
```bash
dotnet run --project src/ControlTower.Api/ControlTower.Api.csproj
```

## Ejecutar con HTTPS

Para ejecutar la aplicación con HTTPS (puerto 7094):
```bash
dotnet run --launch-profile https
```

## Acceder a la API

Una vez que la aplicación esté ejecutándose:

- **Swagger UI**: `http://localhost:5204/swagger` (HTTP) o `https://localhost:7094/swagger` (HTTPS)
- **API Base URL**: `http://localhost:5204` (HTTP) o `https://localhost:7094` (HTTPS)

## Dependencias del Proyecto

El proyecto utiliza los siguientes paquetes NuGet (se restauran automáticamente con `dotnet restore`):

- `Microsoft.AspNetCore.OpenApi` (v9.0.13)
- `Swashbuckle.AspNetCore` (v6.8.1)

# Build and Test

## Compilar
```bash
dotnet build
```

## Ejecutar Tests
```bash
dotnet test
```

# Contribute

TODO: Explain how other users and developers can contribute to make your code better.

If you want to learn more about creating good readme files then refer the following [guidelines](https://docs.microsoft.com/en-us/azure/devops/repos/git/create-a-readme?view=azure-devops). You can also seek inspiration from the below readme files:

- [ASP.NET Core](https://github.com/aspnet/Home)
- [Visual Studio Code](https://github.com/Microsoft/vscode)
- [Chakra Core](https://github.com/Microsoft/ChakraCore)

<<<<<<< HEAD
#Integrantes
-Dvora Yojeved Arreaga
-yeimi
=======
# Proyecto Ingeniería de Software UMG Reu
>>>>>>> 2e1e88f7aa5c6d21bc296835000672a87cc68320
