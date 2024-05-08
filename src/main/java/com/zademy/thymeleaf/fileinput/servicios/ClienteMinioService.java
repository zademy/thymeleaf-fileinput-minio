package com.zademy.thymeleaf.fileinput.servicios;

import org.springframework.web.multipart.MultipartFile;

/**
 * The Interface ClienteMinioService.
 * 
 * @author sadot
 */
public interface ClienteMinioService {

	/**
	 * Upload file.
	 *
	 * @param bucket the bucket
	 * @param ruta   the ruta
	 * @param file   the file
	 * @return true, if successful
	 */
	boolean uploadFile(String bucket, String ruta, MultipartFile file);

}
