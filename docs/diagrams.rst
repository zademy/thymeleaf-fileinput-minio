Diagramas del Proyecto
=====================

Esta sección contiene los diagramas de arquitectura y flujo del proyecto Thymeleaf FileInput con MinIO, generados con Mermaid.

.. _arquitectura-general:

Arquitectura General
-------------------

.. mermaid::
   :caption: Diagrama de Arquitectura

   %%{init: {'theme': 'default'}}%%
   graph TD
       A[Cliente Web] -->|1. Subir archivo| B[Controlador Spring]
       B -->|2. Validar archivo| C[Sistema]
       C -->|3. Almacenar| D[MinIO]
       D -->|4. Respuesta| C
       C -->|5. Respuesta| B
       B -->|6. Respuesta| A
       
       classDef client fill:#f9f,stroke:#333,stroke-width:2px
       classDef controller fill:#bbf,stroke:#333,stroke-width:2px
       classDef system fill:#bfb,stroke:#333,stroke-width:2px
       classDef storage fill:#fbb,stroke:#333,stroke-width:2px
       
       class A client
       class B controller
       class C system
       class D storage

Diagrama general de la arquitectura del sistema

.. _flujo-subida:

Flujo de Subida de Archivos
-------------------------

.. mermaid::
   :caption: Flujo de Subida de Archivos

   %%{init: {'theme': 'default'}}%%
   sequenceDiagram
       actor Usuario
       participant Navegador
       participant Controlador
       participant Servicio
       participant MinIO
       
       Usuario->>Navegador: 1. Selecciona archivo
       Navegador->>+Controlador: 2. POST /upload (multipart/form-data)
       Controlador->>+Servicio: 3. validarArchivo(archivo)
       Servicio-->>-Controlador: 4. OK
       Controlador->>+Servicio: 5. subirArchivo(archivo)
       Servicio->>+MinIO: 6. Subir archivo
       MinIO-->>-Servicio: 7. URL del archivo
       Servicio-->>-Controlador: 8. URL del archivo
       Controlador-->>-Navegador: 9. Respuesta JSON
       Navegador-->>Usuario: 10. Confirmación de subida

Proceso de subida de archivos al servidor MinIO

Estructura de Directorios
-----------------------

.. mermaid::
   :caption: Estructura de Directorios

   %%{init: {'theme': 'default'}}%%
   graph TD
       A[src/] --> B[main/]
       A --> C[test/]
       B --> B1[java/]
       B --> B2[resources/]
       B1 --> B1A[com/zademy/thymeleaf/fileinput/]
       B1A --> B1A1[configuraciones/]
       B1A --> B1A2[controladores/]
       B1A --> B1A3[modelos/]
       B1A --> B1A4[servicios/]
       B2 --> B2A[static/]
       B2A --> B2A1[css/]
       B2A --> B2A2[js/]
       C --> C1[java/]
       
       classDef folder fill:#e1f5fe,stroke:#01579b,stroke-width:1px
       class A,B,C,B1,B2,B1A,B2A,C1 folder
       
       %% Comentarios
       B1A1:::folder
       B1A2:::folder
       B1A3:::folder
       B1A4:::folder
       B2A1:::folder
       B2A2:::folder
       
       %% Añadir etiquetas
       B1A1:::folder -->|Configuraciones| B1A1
       B1A2:::folder -->|Controladores| B1A2
       B1A3:::folder -->|Modelos| B1A3
       B1A4:::folder -->|Servicios| B1A4
       B2A1:::folder -->|Estilos CSS| B2A1
       B2A2:::folder -->|Scripts JS| B2A2
       C1:::folder -->|Pruebas| C1
