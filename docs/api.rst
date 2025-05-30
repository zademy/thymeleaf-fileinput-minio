.. _api:

API Reference
============

Esta sección documenta la API del proyecto Thymeleaf FileInput con MinIO, incluyendo endpoints, servicios y modelos.

Endpoints de la API
-------------------

.. http:post:: /subirImagen
   :synopsis: Sube un archivo al servidor MinIO

   Sube un archivo al bucket configurado en MinIO.

   **Parámetros de la petición**:

   - **file** (MultipartFile, requerido): Archivo a subir

   **Respuesta exitosa (200 OK)**:

   .. code-block:: json

      {
        "exiteError": false,
        "descripcion": "Imagen subida correctamente"
      }

   
   **Respuesta de error**:
   
   .. code-block:: json
   
      {
        "exiteError": true,
        "descripcion": "Error al subir imagen"
      }


Servicios
---------

.. autoclass:: com.zademy.thymeleaf.fileinput.servicios.ClienteMinioService
   :members:
   :undoc-members:
   :show-inheritance:

Implementación de Servicios
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: com.zademy.thymeleaf.fileinput.servicios.impl.ClienteMinioServiceImpl
   :members:
   :undoc-members:
   :show-inheritance:

Modelos
-------

.. autoclass:: com.zademy.thymeleaf.fileinput.persistencia.modelos.RespuestaOperacionModel
   :members:
   :undoc-members:
   :show-inheritance:

Constantes
----------

.. autodata:: com.zademy.thymeleaf.fileinput.persistencia.constantes.MinioConstans
   :annotation:

   Contiene las constantes utilizadas para la configuración de MinIO, incluyendo:
   
   - ``BUCKET_PROCESAR``: Nombre del bucket por defecto
   - ``RUTA``: Ruta dentro del bucket donde se almacenarán los archivos

Controladores
------------

.. autoclass:: com.zademy.thymeleaf.fileinput.exposicion.controladores.SubirImagenController
   :members:
   :undoc-members:
   :show-inheritance:

Configuración
-------------

.. autoclass:: com.zademy.thymeleaf.fileinput.exposicion.configuraciones.MinioConfig
   :members:
   :undoc-members:
   :show-inheritance:

   Configuración de MinIO con las siguientes propiedades:
   
   - ``minio.url``: URL del servidor MinIO
   - ``minio.access-key``: Clave de acceso para autenticación
   - ``minio.secret-key``: Clave secreta para autenticación
