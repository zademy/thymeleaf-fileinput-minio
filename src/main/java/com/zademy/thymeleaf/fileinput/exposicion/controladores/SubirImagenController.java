package com.zademy.thymeleaf.fileinput.exposicion.controladores;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.multipart.MultipartFile;

import com.zademy.thymeleaf.fileinput.persistencia.constantes.MinioConstans;
import com.zademy.thymeleaf.fileinput.persistencia.modelos.RespuestaOperacionModel;
import com.zademy.thymeleaf.fileinput.servicios.ClienteMinioService;

/**
 * The Class SubirImagenController.
 * 
 * @author sadot
 */
@Controller
public class SubirImagenController {

	/** Logger. */
	private static final Logger LOGGER = LoggerFactory.getLogger(SubirImagenController.class);

	/** The cliente minio service. */
	@Autowired
	private ClienteMinioService clienteMinioService;

	/**
	 * Inicio.
	 *
	 * @return index
	 */
	@GetMapping(path = "/")
	public String inicio() {

		return "index";
	}

	/**
	 * Subir imagen.
	 *
	 * @param file the file
	 * @return the respuesta operacion model
	 */
	@PostMapping(path = "/subirImagen")
	@ResponseBody
	public RespuestaOperacionModel subirImagen(@RequestBody @RequestParam("file") MultipartFile file) {

		RespuestaOperacionModel respuesta = new RespuestaOperacionModel();

		boolean resultado = false;

		respuesta.setExiteError(resultado);

		try {

			LOGGER.info("SubirImagenController -> subirImagen");

			resultado = clienteMinioService.uploadFile(MinioConstans.BUCKET_PROCESAR, MinioConstans.RUTA, file);

			if (!resultado) {

				throw new Exception("Error al subir imagen");

			}

			respuesta.setDescripcion("Imagen subida correctamente");

		} catch (Exception e) {

			LOGGER.error("SubirImagenController -> subirImagen -> Error: ", e);

			respuesta.setExiteError(true);

			respuesta.setDescripcion("Error al subir imagen");

		}

		return respuesta;

	}

}
