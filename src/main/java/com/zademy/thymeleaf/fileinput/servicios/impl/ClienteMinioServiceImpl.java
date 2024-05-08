package com.zademy.thymeleaf.fileinput.servicios.impl;

import java.io.InputStream;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import com.zademy.thymeleaf.fileinput.servicios.ClienteMinioService;

import io.minio.BucketExistsArgs;
import io.minio.MakeBucketArgs;
import io.minio.MinioClient;
import io.minio.PutObjectArgs;

/**
 * The Class ClienteMinioServiceImpl.
 * 
 * @author sadot
 */
@Service
public class ClienteMinioServiceImpl implements ClienteMinioService {

	/** The Constant LOGGER. */
	private static final Logger LOGGER = LoggerFactory.getLogger(ClienteMinioServiceImpl.class);

	/** The minio client. */
	@Autowired
	private MinioClient minioClient;

	/*
	 * (non-Javadoc)
	 *
	 * @see
	 * com.zademy.thymeleaf.fileinput.servicios.ClienteMinioService#uploadFile(java.
	 * lang.String, java.lang.String,
	 * org.springframework.web.multipart.MultipartFile)
	 */
	@Override
	public boolean uploadFile(String bucket, String ruta, MultipartFile file) {

		LOGGER.info("ClienteMinioServiceImpl -> uploadFile -> bucket: {} ", bucket);

		try {

			boolean found = minioClient.bucketExists(BucketExistsArgs.builder().bucket(bucket).build());

			if (!found) {

				minioClient.makeBucket(MakeBucketArgs.builder().bucket(bucket).build());

			}

			String fileName = file.getOriginalFilename();

			InputStream fileInputStream = file.getInputStream();

			long fileSize = file.getSize();

			minioClient.putObject(PutObjectArgs.builder().bucket(bucket).object(ruta + fileName)
					.stream(fileInputStream, fileSize, -1).contentType(file.getContentType()).build());

			fileInputStream.close();

			return true;

		} catch (Exception e) {

			LOGGER.error("ClienteMinioServiceImpl -> uploadFile -> Error: ", e);

		}

		return false;

	}

}
