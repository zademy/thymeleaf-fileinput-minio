package com.zademy.thymeleaf.fileinput.exposicion.configuraciones;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import io.minio.MinioClient;

/**
 * The Class MinioConfig.
 * 
 * @author sadot
 */
@Configuration
public class MinioConfig {

	/** The endpoint. */
	@Value("${minio.endpoint}")
	private String endpoint;

	/** The access key. */
	@Value("${minio.accessKey}")
	private String accessKey;

	/** The secret key. */
	@Value("${minio.secretKey}")
	private String secretKey;

	/**
	 * Minio client.
	 *
	 * @return the minio client
	 */
	@Bean
	MinioClient minioClient() {
		return MinioClient.builder().endpoint(endpoint).credentials(accessKey, secretKey).build();
	}
}
