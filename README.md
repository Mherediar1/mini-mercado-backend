# Mini Mercado API

Tarea 02.03 – Ingeniería de Software.

## Descripción
Backend desarrollado con FastAPI que implementa una API REST para la gestión de un mini mercado, permitiendo administrar productos, categorías, usuarios y ventas.

## Requerimientos del Sistema
- Gestión de productos
- Registro de ventas
- Administración de categorías
- Consulta de usuarios

## Diseño del Sistema
El sistema sigue una arquitectura en capas:
- Modelo
- Repositorio
- Servicio
- Controlador

El diseño del sistema se apoya en un diagrama UML de clases que representa las entidades principales y sus relaciones dentro de la aplicación.

<img width="1224" height="1182" alt="Diagrama" src="https://github.com/user-attachments/assets/7fb6ad76-438e-43c4-aa2e-507ae492f569" />

## Organización del Equipo
- **Fernando Heredia**: Desarrollo principal del backend, definición de la arquitectura, implementación de modelos y endpoints de productos y ventas.
- **Fabian Coox**: Ejecución de pruebas de los servicios mediante Swagger, validación de endpoints y apoyo en la verificación del funcionamiento de la API.
- **Aaron Cevallos**: Apoyo en la documentación del proyecto, revisión general del código y control de versiones.
- **Chuan Liao**: Apoyo en el desarrollo del backend y colaboración en la implementación de funcionalidades junto al desarrollador principal.

## Tecnologías Utilizadas
- Python 3  
- FastAPI  
- SQLAlchemy  
- Uvicorn  
- SQLite  
- Swagger (OpenAPI)

## Ejecución del proyecto
Para ejecutar la aplicación, utilizar el siguiente comando:

uvicorn app.main:app --reload

## Documentación
La documentación de la API se encuentra disponible en Swagger en la siguiente ruta:

http://127.0.0.1:8000/docs
