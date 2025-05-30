Diagramas del Proyecto
=====================

Esta sección contiene los diagramas de arquitectura y flujo del proyecto Thymeleaf FileInput con MinIO, generados con Mermaid.

.. _arquitectura-general:

Arquitectura General
-------------------

.. mermaid::
   :caption: Diagrama de Arquitectura

   %%{init: {'theme': 'default', 'themeVariables': { 'primaryColor': '#f9f'}}%%
   graph TD
       A[Cliente Web] --> B[Controlador Spring]
       B --> C[Sistema]
       C --> D[MinIO]
       D --> C --> B --> A

       classDef client fill:#f9f,stroke:#333
       classDef controller fill:#bbf,stroke:#333
       classDef system fill:#bfb,stroke:#333
       classDef storage fill:#fbb,stroke:#333
       
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
       actor U as Usuario
       participant N as Navegador
       participant C as Controlador
       participant S as Servicio
       participant M as MinIO
       
       U ->> N: 1. Selecciona archivo
       N ->>+ C: 2. POST /upload
       C ->>+ S: 3. validarArchivo()
       S -->>- C: 4. OK
       C ->>+ S: 5. subirArchivo()
       S ->>+ M: 6. Subir archivo
       M -->>- S: 7. URL
       S -->>- C: 8. URL
       C -->>- N: 9. Respuesta JSON
       N -->> U: 10. Confirmación

Proceso de subida de archivos al servidor MinIO

Estructura de Directorios
-----------------------

.. mermaid::
   :caption: Estructura de Directorios

   %%{init: {'theme': 'neutral'}}%%
   graph TD
       A[src/] --> B[main/]
       A --> C[test/]
       B --> B1[java/]
       B --> B2[resources/]
       B1 --> B1A[com/zademy/...]
       B1A -->|Config| B1A1[config/]
       B1A -->|Controllers| B1A2[controllers/]
       B1A -->|Models| B1A3[models/]
       B1A -->|Services| B1A4[services/]
       B2 --> B2A[static/]
       B2A --> B2A1[css/]
       B2A --> B2A2[js/]
       C --> C1[java/]
       
       classDef folder fill:#f5f5f5,stroke:#666
       class A,B,C,B1,B2,B1A,B2A,C1,B1A1,B1A2,B1A3,B1A4,B2A1,B2A2 folder
