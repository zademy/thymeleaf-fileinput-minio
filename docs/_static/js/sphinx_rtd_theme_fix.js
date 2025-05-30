// Definir SphinxRtdTheme antes de que el tema intente utilizarlo
window.SphinxRtdTheme = window.SphinxRtdTheme || {};

// Inicializar las propiedades y métodos necesarios
if (!window.SphinxRtdTheme.Navigation) {
  window.SphinxRtdTheme.Navigation = {
    enable: function() { return true; },
    wrapper: null,
    build: function() {},
    init: function() {}
  };
}

// Asegurarse de que jQuery esté disponible globalmente
if (typeof jQuery !== 'undefined') {
  window.$ = window.jQuery = jQuery;
  console.log("jQuery está disponible globalmente");
}

console.log("SphinxRtdTheme inicializado correctamente");
