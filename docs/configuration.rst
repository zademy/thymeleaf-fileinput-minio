==================
Configuración
==================

Este documento detalla las opciones de configuración disponibles para el proyecto Thymeleaf FileInput con MinIO.

Configuración de la Aplicación
-----------------------------

El archivo principal de configuración es ``application.properties`` o ``application.yml``. Aquí están las propiedades más importantes:

.. code-block:: yaml

   # Configuración del servidor
   server.port=8080
   
   # Configuración de Thymeleaf
   spring.thymeleaf.cache=false
   spring.thymeleaf.prefix=classpath:/templates/
   spring.thymeleaf.suffix=.html
   
   # Configuración de MinIO
   minio.endpoint=${MINIO_ENDPOINT:http://localhost:9000}
   minio.access-key=${MINIO_ACCESS_KEY}
   minio.secret-key=${MINIO_SECRET_KEY}
   minio.bucket-name=${MINIO_BUCKET_NAME}
   minio.secure=false

Variables de Entorno
--------------------

Puedes configurar la aplicación mediante variables de entorno:

+----------------------+-------------------------------------+------------------+
| Variable             | Descripción                         | Valor por Defecto |
+======================+=====================================+==================+
| MINIO_ENDPOINT      | URL del servidor MinIO              | http://localhost:9000 |
+----------------------+-------------------------------------+------------------+
| MINIO_ACCESS_KEY    | Clave de acceso de MinIO            | -               |
+----------------------+-------------------------------------+------------------+
| MINIO_SECRET_KEY    | Clave secreta de MinIO              | -               |
+----------------------+-------------------------------------+------------------+
| MINIO_BUCKET_NAME   | Nombre del bucket en MinIO          | -               |
+----------------------+-------------------------------------+------------------+
| MINIO_SECURE        | Usar conexión segura (true/false)   | false           |
+----------------------+-------------------------------------+------------------+

Configuración de Seguridad
-------------------------

Para entornos de producción, se recomienda:

1. **No** almacenar credenciales en el código fuente
2. Usar un gestor de secretos (como Vault, AWS Secrets Manager, etc.)
3. Configurar HTTPS para todas las comunicaciones
4. Implementar autenticación y autorización adecuadas

Personalización
---------------

Puedes personalizar la aplicación modificando las siguientes propiedades:

.. code-block:: yaml

   # Tamaño máximo de archivo (en bytes)
   spring.servlet.multipart.max-file-size=10MB
   spring.servlet.multipart.max-request-size=10MB
   
   # Configuración de CORS (si es necesario)
   cors.allowed-origins=*
   cors.allowed-methods=GET,POST,PUT,DELETE,OPTIONS
   cors.allowed-headers=*

Configuración de Logs
--------------------

Para habilitar logs detallados, agrega lo siguiente a tu ``application.yml``:

.. code-block:: yaml

   logging:
     level:
       root: INFO
       com.zademy: DEBUG
       org.springframework.web: INFO
       org.hibernate: ERROR

   # Para ver las consultas SQL (solo desarrollo)
   spring.jpa.show-sql: true
   spring.jpa.properties.hibernate.format_sql: true
