# Proyecto de Acceso Seguro

Este proyecto ilustra cómo `main.py` obtiene el usuario y la contraseña desde `config.py`. La contraseña y el usuario están almacenados en `config.py` y no se suben al repositorio para mantener la seguridad de las credenciales.

### Diagrama de Flujo

```mermaid
graph TD
    A[main.py] -->|importa| B[config.py]
    B --> C[USERNAME y PASSWORD]
    A --> D[usuario y contraseña]
    D --> E[Accede al sistema o servicio]

