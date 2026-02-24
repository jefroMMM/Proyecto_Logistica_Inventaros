Creamos las carpetas base
mkdir control-tower-logistics   #este ya lo tenemos desde la creación del proyecto
cd control-tower-logistics

mkdir -p docs src/backend src/frontend infra/docker azure-pipelines

#ESTRUCTURA DEL BACKEND
cd src/backend
dotnet new sln -n ControlTower

mkdir -p src
cd src

dotnet new classlib -n ControlTower.Domain
dotnet new classlib -n ControlTower.Application
dotnet new classlib -n ControlTower.Infrastructure
dotnet new webapi  -n ControlTower.Api
dotnet new xunit   -n ControlTower.Tests

#AGREGAMOS PROYECTOS A LA SOLUCIÓN
cd ..
dotnet sln ControlTower.sln add src/ControlTower.Domain/ControlTower.Domain.csproj
dotnet sln ControlTower.sln add src/ControlTower.Application/ControlTower.Application.csproj
dotnet sln ControlTower.sln add src/ControlTower.Infrastructure/ControlTower.Infrastructure.csproj
dotnet sln ControlTower.sln add src/ControlTower.Api/ControlTower.Api.csproj
dotnet sln ControlTower.sln add src/ControlTower.Tests/ControlTower.Tests.csproj

#Regla (Clean Architecture):
--Api → Application + Infrastructure
--Infrastructure → Application + Domain
--Application → Domain
--Domain → (nada)
--Tests → Application (+ Domain si necesitas)

#DEBEN CORRER LOS SIGUIENTES:
# Application depende de Domain
dotnet add src/ControlTower.Application/ControlTower.Application.csproj reference src/ControlTower.Domain/ControlTower.Domain.csproj

# Infrastructure depende de Application y Domain
dotnet add src/ControlTower.Infrastructure/ControlTower.Infrastructure.csproj reference src/ControlTower.Application/ControlTower.Application.csproj
dotnet add src/ControlTower.Infrastructure/ControlTower.Infrastructure.csproj reference src/ControlTower.Domain/ControlTower.Domain.csproj

# Api depende de Application e Infrastructure
dotnet add src/ControlTower.Api/ControlTower.Api.csproj reference src/ControlTower.Application/ControlTower.Application.csproj
dotnet add src/ControlTower.Api/ControlTower.Api.csproj reference src/ControlTower.Infrastructure/ControlTower.Infrastructure.csproj

# Tests depende de Application (y opcional Domain)
dotnet add src/ControlTower.Tests/ControlTower.Tests.csproj reference src/ControlTower.Application/ControlTower.Application.csproj
dotnet add src/ControlTower.Tests/ControlTower.Tests.csproj reference src/ControlTower.Domain/ControlTower.Domain.csproj



##SI DESEA UNA ESTRUCTRUA LIMPIA PUEDE BORRAR:
WeatherForecast.cs

PROBAR BACKEND
cd src/ControlTower.Api
dotnet run