package com.zademy.thymeleaf.fileinput.persistencia.modelos;

import java.io.Serializable;

/**
 * The Class RespuestaOperacionModel.
 * 
 * @author sadot
 */
public class RespuestaOperacionModel implements Serializable {

	/** The Constant serialVersionUID. */
	private static final long serialVersionUID = 1793052093561825995L;

	/** The respuesta. */
	private boolean exiteError;

	/** The descripcion. */
	private String descripcion;

	/**
	 * Instantiates a new respuesta operacion model.
	 */
	public RespuestaOperacionModel() {
		super();
	}

	/**
	 * Checks if is exite error.
	 *
	 * @return true, if is exite error
	 */
	public boolean isExiteError() {
		return exiteError;
	}

	/**
	 * Sets the exite error.
	 *
	 * @param exiteError the new exite error
	 */
	public void setExiteError(boolean exiteError) {
		this.exiteError = exiteError;
	}

	/**
	 * Gets the descripcion.
	 *
	 * @return the descripcion
	 */
	public String getDescripcion() {
		return descripcion;
	}

	/**
	 * Sets the descripcion.
	 *
	 * @param descripcion the new descripcion
	 */
	public void setDescripcion(String descripcion) {
		this.descripcion = descripcion;
	}

	/*
	 * (non-Javadoc)
	 *
	 * @see java.lang.Object#toString()
	 */
	@Override
	public String toString() {
		StringBuilder builder = new StringBuilder();
		builder.append("RespuestaOperacionModel [exiteError=");
		builder.append(exiteError);
		builder.append(", descripcion=");
		builder.append(descripcion);
		builder.append("]");
		return builder.toString();
	}

}
