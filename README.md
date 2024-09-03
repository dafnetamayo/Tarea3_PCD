# Tarea3_PCD
# Dafne Tamayo León

Este repositorio contiene la implementación de una API para gestionar usuarios. La API incluye cuatro endpoints que permiten crear, actualizar, obtener y eliminar usuarios en una base de datos.

## Requisitos

- Python 3.8 o superior
- pip
- virtualenv

## Instalación

1. **Clonar el repositorio en tu local:**

    ```bash
    git clone https://github.com/tu_usuario/Tarea3_PCD.git
    cd Tarea3_PCD
    ```

2. **Crear y activar un ambiente virtual:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate 
    ```

3. **Instalar las dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

## Endpoints de la API

La API incluye los siguientes endpoints:

### 1. Crear un usuario

- **URL:** `/create_user`
- **Método:** `POST`
- **Descripción:** Crea un nuevo usuario y lo guarda en la base de datos.
- **Cuerpo de la solicitud:**

    ```json
    {
        "user_name": "name",
        "user_id": id,
        "user_email": "email",
        "age": age,  # opcional
        "recommendations": ["list", "of", "strings"],
        "ZIP": "ZIP"  # opcional
    }
    ```

- **Respuesta en caso de éxito:** `201 Created`
- **Respuesta en caso de error:** `400 Bad Request` (si el email ya existe)

### 2. Actualizar un usuario

- **URL:** `/update_user/<id>`
- **Método:** `PUT`
- **Descripción:** Actualiza la información de un usuario específico buscándolo por `id`.
- **Cuerpo de la solicitud:**

    ```json
    {
        "user_name": "name",
        "user_email": "email",
        "age": age,  # opcional
        "recommendations": ["list", "of", "strings"],
        "ZIP": "ZIP"  # opcional
    }
    ```

- **Respuesta en caso de éxito:** `200 OK`
- **Respuesta en caso de error:** `404 Not Found` (si el id no existe)

### 3. Obtener un usuario

- **URL:** `/get_user/<id>`
- **Método:** `GET`
- **Descripción:** Obtiene la información de un usuario específico buscándolo por `id`.
- **Respuesta en caso de éxito:** `200 OK`
- **Respuesta en caso de error:** `404 Not Found` (si el id no existe)

### 4. Eliminar un usuario

- **URL:** `/delete_user/<id>`
- **Método:** `DELETE`
- **Descripción:** Elimina la información de un usuario específico buscándolo por `id`.
- **Respuesta en caso de éxito:** `200 OK`
- **Respuesta en caso de error:** `404 Not Found` (si el id no existe)

## Ejecución

Para ejecutar el proyecto localmente, asegúrate de estar en el directorio raíz del proyecto y ejecuta el siguiente comando:

```bash
uvicorn main:app --reload