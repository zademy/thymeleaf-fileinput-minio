==================
Guía de Uso
==================

Esta guía explica cómo utilizar la aplicación Thymeleaf FileInput con MinIO.

Subida de Archivos
------------------

1. **Interfaz de Usuario**

   La aplicación proporciona una interfaz web intuitiva para cargar archivos:
   
   - Navega a la página principal (http://localhost:8080)
   - Haz clic en "Seleccionar archivos" o arrastra y suelta archivos en el área designada
   - Los archivos seleccionados aparecerán en una lista de vista previa
   - Haz clic en "Subir" para cargar los archivos al servidor MinIO

2. **Límites**

   - Tamaño máximo por archivo: 10MB (configurable)
   - Formatos permitidos: Cualquier tipo de archivo
   - Cantidad máxima de archivos: Ilimitada (sujeto a la capacidad de tu servidor)

3. **Notificaciones**

   - Éxito: Se muestra un mensaje de confirmación cuando la carga se completa
   - Error: Se muestra un mensaje de error si ocurre algún problema

Descarga de Archivos
-------------------

1. **Desde la Interfaz Web**

   - Los archivos subidos aparecerán en una lista
   - Haz clic en el nombre de un archivo para descargarlo
   - Usa el botón de eliminación para eliminar archivos

2. **Acceso Directo**

   Los archivos también están disponibles directamente a través de la API:
   
   .. code-block:: bash

      GET /api/files/download/{filename}

API REST
--------

La aplicación expone los siguientes endpoints:

+------------------+--------------------------------+---------------------------------------------------+
| Método | Ruta | Descripción |
+==================+================================+===================================================+
| GET | /api/files | Lista todos los archivos |
+------------------+--------------------------------+---------------------------------------------------+
| POST | /api/files/upload | Sube uno o varios archivos |
+------------------+--------------------------------+---------------------------------------------------+
| GET | /api/files/download/{filename} | Descarga un archivo |
+------------------+--------------------------------+---------------------------------------------------+
| DELETE | /api/files/{filename} | Elimina un archivo |
+------------------+--------------------------------+---------------------------------------------------+

Ejemplo de Uso con cURL
----------------------

Subir un archivo:

.. code-block:: bash

   curl -X POST -F "files=@/ruta/al/archivo.txt" http://localhost:8080/api/files/upload

Listar archivos:

.. code-block:: bash

   curl http://localhost:8080/api/files

Descargar un archivo:

.. code-block:: bash

   curl -OJ http://localhost:8080/api/files/download/archivo.txt

Personalización de la Interfaz
-----------------------------

Puedes personalizar la interfaz modificando las plantillas de Thymeleaf en:

.. code-block:: none

   src/main/resources/templates/
   ├── index.html         # Página principal
   └── fragments/         # Fragmentos reutilizables
       ├── header.html
       ├── footer.html
       └── file-upload.html

Integración con Frontend
-----------------------

Para integrar la carga de archivos en tu propia aplicación frontend:

1. **Usando Fetch API**

   .. code-block:: javascript

      async function uploadFile(file) {
          const formData = new FormData();
          formData.append('files', file);
          
          try {
              const response = await fetch('/api/files/upload', {
                  method: 'POST',
                  body: formData
              });
              return await response.json();
          } catch (error) {
              console.error('Error:', error);
          }
      }

2. **Usando Axios**

   .. code-block:: javascript

      import axios from 'axios';
      
      const uploadFile = async (file) => {
          const formData = new FormData();
          formData.append('files', file);
          
          try {
              const response = await axios.post('/api/files/upload', formData, {
                  headers: {
                      'Content-Type': 'multipart/form-data'
                  }
              });
              return response.data;
          } catch (error) {
              console.error('Error:', error);
              throw error;
          }
      };

Seguridad
---------

- Todas las comunicaciones deben hacerse a través de HTTPS en producción
- Implementa autenticación si la API es accesible desde internet
- Configura CORS adecuadamente si el frontend está en un dominio diferente
