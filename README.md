
# Thymeleaf File Input with MinIO Example

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://example.com/build)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

This project demonstrates how to integrate Thymeleaf with a file input component and MinIO for storing uploaded files. It provides a simple and effective way to handle file uploads in a Spring Boot application.

## Table of Contents
1.  [Introduction](#introduction)
2.  [Architecture Diagram](#architecture-diagram)
3.  [Prerequisites](#prerequisites)
4.  [Project Setup](#project-setup)
5.  [Database Schema](#database-schema)
6.  [Code Flow](#code-flow)
7.  [Configuration](#configuration)
8.  [Usage](#usage)
9.  [Contributing](#contributing)
10. [License](#license)

## Introduction

This application allows users to upload files through a Thymeleaf-based interface, which are then stored in a MinIO object storage. It's designed to be a straightforward example for developers looking to implement similar functionality in their projects.

## Architecture Diagram

The architecture consists of the following components:
-   **User:** Interacts with the Thymeleaf UI.
-   **Thymeleaf UI:** Presents the file upload form.
-   **Spring Boot Controller:** Handles the file upload request.
-   **MinIO Service:** Manages the connection and operations with MinIO.
-   **MinIO Bucket:** Stores the uploaded files.

## Prerequisites

-   Spring Boot 3.2.5
-   Thymeleaf
-   Tomcat Embed 10
-   Maven
-   Java 21
-   MinIO Server (configured and running)

## Project Setup

bash
    git clone <repository-url>
    cd thymeleaf-fileinput-minio
    3.  Configure MinIO settings in `application.properties` or `application.yml`.

> Provide MinIO endpoint, access key, secret key, and bucket name.  Example:
> This project does not require a traditional relational database.  Metadata about the files, such as file name and upload time, *could* be stored in a database, but this example focuses on MinIO storage. If you choose to add a database:

sql
> CREATE TABLE files (
>     id INT PRIMARY KEY AUTO_INCREMENT,
>     file_name VARCHAR(255) NOT NULL,
>     upload_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
> );
> 1.  The user accesses the Thymeleaf page with the file input form.
2.  The user selects a file and submits the form.
3.  The Spring Boot controller receives the file.
4.  The MinIO service uploads the file to the specified bucket.
5.  The controller updates the view with a success message.



## Configuration

Configure MinIO settings in the `application.properties` or `application.yml` file.

> Example using `application.properties`:
> 1.  Run the Spring Boot application.
2.  Access the page using the URL: `http://localhost:8080/thymeleaf-fileinput`

    <img src="https://github.com/zademy/thymeleaf-fileinput-minio/blob/master/src/main/resources/static/images/03.png?raw=true" alt="Imagen de Fileinput" style="display: block; margin: 0 auto;">

3.  Select a file and click the upload button.
4.  Verify that the file is uploaded to the MinIO bucket.

## Contributing

>  Explain how others can contribute to your project.  For example:
>  1. Fork the repository.
>  2. Create a new branch.
>  3. Make your changes.
>  4. Submit a pull request.

## License

