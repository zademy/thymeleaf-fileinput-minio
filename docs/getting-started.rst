==================
Guía de Inicio Rápido
==================

.. include:: _templates/menu.rst

Este documento te guiará a través de la configuración inicial del proyecto Thymeleaf FileInput con MinIO.

Requisitos Previos
------------------
- Java 21 o superior
- Maven 3.6 o superior
- Un servidor MinIO en ejecución (o una cuenta en cloud.min.io)

Instalación
-----------

1. Clona el repositorio:

   .. code-block:: bash

      git clone https://github.com/tu-usuario/thymeleaf-fileinput-minio.git
      cd thymeleaf-fileinput-minio

2. Configura las variables de entorno:

   Crea un archivo ``.env`` en la raíz del proyecto con las siguientes variables:

   .. code-block:: bash

      MINIO_ENDPOINT=tu-servidor-minio
      MINIO_ACCESS_KEY=tu-access-key
      MINIO_SECRET_KEY=tu-secret-key
      MINIO_BUCKET_NAME=nombre-del-bucket

3. Compila el proyecto:

   .. code-block:: bash

      mvn clean install

4. Ejecuta la aplicación:

   .. code-block:: bash

      mvn spring-boot:run

La aplicación estará disponible en: http://localhost:8080

Solución de Problemas
---------------------

- **Error de conexión a MinIO**: Verifica que las credenciales y el endpoint sean correctos.
- **Bucket no encontrado**: Asegúrate de que el bucket especificado exista en tu servidor MinIO.
- **Problemas de permisos**: Verifica que las credenciales tengan los permisos necesarios.
