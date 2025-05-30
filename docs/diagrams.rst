.. _diagrams:

Diagramas del Proyecto
=====================

Esta sección contiene los diagramas de arquitectura y flujo del proyecto Thymeleaf FileInput con MinIO, generados con Mermaid.

Arquitectura General
-------------------

.. mermaid::
   :align: center
   :width: 80%
   :caption: Diagrama de Arquitectura

   graph TD
       A[Cliente Web] -->|1. Subir archivo| B[Controlador Spring]
       B -->|2. Validar archivo| C[Sistema]
       C -->|3. Almacenar| D[MinIO]
       D -->|4. Respuesta| C
       C -->|5. Respuesta| B
       B -->|6. Respuesta| A
       
       style A fill:#f9f,stroke:#333,stroke-width:2px
       style B fill:#bbf,stroke:#333,stroke-width:2px
       style C fill:#bfb,stroke:#333,stroke-width:2px
       style D fill:#fbb,stroke:#333,stroke-width:2px

   Diagrama general de la arquitectura del sistema

Flujo de Subida de Archivos
-------------------------

.. mermaid::
   :align: center
   :width: 80%
   :caption: Flujo de Subida de Archivos

   sequenceDiagram
       participant Usuario
       participant Navegador
       participant Controlador
       participant Servicio
       participant MinIO
       
       Usuario->>Navegador: Selecciona archivo
       Navegador->>Controlador: POST /upload (multipart/form-data)
       Controlador->>Servicio: validarArchivo(archivo)
       Servicio-->>Controlador: OK
       Controlador->>Servicio: subirArchivo(archivo)
       Servicio->>MinIO: Subir archivo
       MinIO-->>Servicio: URL del archivo
       Servicio-->>Controlador: URL del archivo
       Controlador-->>Navegador: Respuesta JSON
       Navegador-->>Usuario: Confirmación de subida

   Proceso de subida de archivos al servidor MinIO

Estructura de Directorios
-----------------------

.. code-block:: text

   src/
   ├── main/
   │   ├── java/
   │   │   └── com/zademy/thymeleaf/fileinput/
   │   │       ├── configuraciones/  # Configuraciones de la aplicación
   │   │       ├── controladores/     # Controladores de Spring
   │   │       ├── modelos/          # Entidades del dominio
   │   │       └── servicios/        # Lógica de negocio
   │   └── resources/
   │       └── static/
   │           ├── css/              # Estilos personalizados
   │           └── js/               # Scripts JavaScript
   └── test/
       └── java/           # Pruebas unitarias y de integración
