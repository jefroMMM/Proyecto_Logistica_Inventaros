# Historias de usuario

Este documento organiza las historias de usuario del sistema **Control Tower Logistics** siguiendo una estructura clara y mantenible.

## Criterios de redacción

- Formato de historia: *Como [rol], quiero [objetivo], para [beneficio]*.
- Criterios de aceptación con enfoque Given/When/Then cuando aplica.
- Tareas técnicas orientadas a implementación backend y frontend.

---

## Epic 1. Gestión de usuarios y seguridad

### US-01. Inicio de sesión

**Historia**
Como usuario del sistema, quiero iniciar sesión con mis credenciales para acceder a las funcionalidades según mi rol.

**Criterios de aceptación**
- Dado que el usuario accede al sistema, cuando ingresa credenciales válidas, entonces se permite el acceso.
- Dado que las credenciales son incorrectas, cuando intenta iniciar sesión, entonces se muestra un mensaje de error.
- Dado que el usuario está autenticado, cuando entra al sistema, entonces visualiza las opciones permitidas por su rol.

**Tareas**
- Crear la entidad `Usuario`.
- Crear la tabla `usuarios`.
- Implementar endpoint de `login`.
- Validar credenciales.
- Construir formulario de inicio de sesión en frontend.

### US-02. Gestión de roles

**Historia**
Como administrador, quiero gestionar roles de usuario para controlar los accesos al sistema.

**Criterios de aceptación**
- El sistema permite crear roles.
- El sistema permite asignar roles a usuarios.
- El sistema restringe funcionalidades según el rol asignado.

**Tareas**
- Crear la entidad `Rol`.
- Definir relación `Usuario-Rol`.
- Implementar CRUD de roles.
- Agregar validación de permisos por rol.

---

## Epic 2. Gestión de vehículos

### US-03. Registrar vehículo

**Historia**
Como operador, quiero registrar vehículos para administrar la flotilla disponible.

**Criterios de aceptación**
- El sistema registra una placa única.
- El sistema registra tipo, capacidad y estado del vehículo.

**Tareas**
- Crear entidad `Vehiculo`.
- Crear tabla `vehiculos`.
- Implementar endpoint `POST /vehiculos`.
- Validar unicidad de placa.
- Crear formulario de registro en frontend.

### US-04. Consultar vehículos

**Historia**
Como usuario, quiero consultar vehículos para conocer su disponibilidad.

**Criterios de aceptación**
- Se muestra el listado de vehículos.
- Se puede filtrar por estado.
- Se puede buscar por placa.

**Tareas**
- Implementar endpoint `GET /vehiculos`.
- Agregar filtro por estado.
- Agregar búsqueda por placa.
- Crear vista tipo tabla en frontend.

### US-05. Actualizar vehículo

**Historia**
Como operador, quiero editar la información de un vehículo para mantener los datos actualizados.

**Criterios de aceptación**
- Se permite editar los campos habilitados.
- El sistema valida la información antes de guardar.
- Los cambios se guardan correctamente.

**Tareas**
- Implementar endpoint `PUT /vehiculos`.
- Añadir validaciones de negocio.
- Crear formulario de edición en frontend.

---

## Epic 3. Gestión de pilotos

### US-06. Registrar piloto

**Historia**
Como operador, quiero registrar pilotos para asignarlos a los viajes.

**Tareas**
- Crear entidad `Piloto`.
- Crear tabla `pilotos`.
- Implementar endpoint `POST /pilotos`.
- Validar unicidad de licencia.

### US-07. Consultar pilotos

**Historia**
Como usuario, quiero consultar pilotos para revisar su disponibilidad.

**Tareas**
- Implementar endpoint `GET /pilotos`.
- Agregar filtros de consulta.
- Crear vista de pilotos en frontend.

---

## Epic 4. Gestión de rutas

### US-08. Registrar ruta

**Historia**
Como administrador, quiero registrar rutas para definir trayectos operativos.

**Tareas**
- Crear entidad `Ruta`.
- Crear tabla `rutas`.
- Implementar endpoint `POST /rutas`.
- Validar rutas duplicadas.

### US-09. Consultar rutas

**Historia**
Como usuario, quiero consultar rutas para analizar recorridos disponibles.

**Tareas**
- Implementar endpoint `GET /rutas`.
- Agregar filtro por origen y destino.

---

## Epic 5. Gestión de viajes (core)

### US-10. Crear viaje

**Historia**
Como operador, quiero crear un viaje para gestionar el transporte.

**Criterios de aceptación**
- Se puede seleccionar vehículo.
- Se puede seleccionar piloto.
- Se puede seleccionar ruta.
- Se registra la hora de salida.

**Tareas**
- Crear entidad `Viaje`.
- Crear tabla `viajes`.
- Implementar endpoint `POST /viajes`.
- Validar datos de entrada.
- Crear interfaz de registro de viaje.

### US-11. Consultar viajes

**Tareas**
- Implementar endpoint `GET /viajes`.
- Agregar filtros por fecha.
- Agregar filtro por estado.
- Crear tabla de visualización en frontend.

### US-12. Actualizar estado del viaje

**Tareas**
- Implementar endpoint para actualizar estado.
- Definir control de transiciones de estado.
- Registrar historial de cambios.

### US-13. Registrar llegada

**Tareas**
- Implementar endpoint para registrar llegada.
- Calcular tiempo real del viaje.
- Validar coherencia de hora de llegada.

---

## Epic 6. Alertas operativas

### US-14. Alerta por retraso

**Historia**
Como supervisor, quiero recibir alertas de retraso para tomar decisiones oportunas.

**Tareas**
- Comparar tiempo estimado vs tiempo real.
- Crear entidad `Alerta`.
- Registrar alertas en el sistema.
- Mostrar alertas en dashboard.

### US-15. Vehículos inactivos

**Tareas**
- Consultar vehículos sin viajes en un periodo.
- Mostrar reporte de inactividad.

---

## Epic 7. Dashboard

### US-16. Dashboard principal

**Tareas**
- Implementar endpoint de KPIs.
- Mostrar viajes del día.
- Mostrar viajes finalizados.
- Mostrar viajes retrasados.
- Mostrar vehículos activos.

### US-17. Indicador de cumplimiento de rutas

**Tareas**
- Calcular porcentaje de cumplimiento.
- Implementar endpoint de reporte.
- Mostrar gráfica en frontend.

---

## Epic 8. Reportería

### US-18. Reporte de viajes

**Tareas**
- Implementar endpoint de reporte.
- Agregar filtros de consulta.
- Permitir exportación en CSV.

### US-19. Reporte de retrasos

**Tareas**
- Consultar viajes retrasados.
- Agregar filtro por rango de fechas.

---

## Epic 9. Auditoría

### US-20. Registro de acciones

**Historia**
Como administrador, quiero auditar las acciones del sistema para mantener trazabilidad.

**Tareas**
- Crear entidad `Auditoria`.
- Registrar acciones relevantes del sistema.
- Implementar consulta de auditoría.