# Proyecto de Acceso Seguro

Este proyecto ilustra cómo `main.py` obtiene el usuario y la contraseña desde `config.py`. La contraseña y el usuario están almacenados en `config.py` y no se suben al repositorio para mantener la seguridad de las credenciales.

### Diagrama de Flujo

```mermaid
graph TD
    A[main.py] -->|importa| B[config.py]
    B --> C[USERNAME y PASSWORD]
    A --> D[usuario y contraseña]
    D --> E[Accede al sistema o servicio]


### Explicación del Diagrama

- **`A[main.py]`**: Representa el archivo principal, `main.py`.
- **`B[config.py]`**: Representa el archivo `config.py`, que contiene `USERNAME` y `PASSWORD`.
- **`D[usuario y contraseña]`**: Variables en `main.py` que almacenan el usuario y la contraseña importados.
- **`E[Accede al sistema o servicio]`**: Representa el uso final de las credenciales en `main.py`.

### Instrucciones para Visualizar el Diagrama
Si tu visualizador de Markdown soporta **Mermaid** (como en GitHub), podrás ver el gráfico en el `README.md`. Este gráfico documenta claramente la relación entre ambos archivos.
