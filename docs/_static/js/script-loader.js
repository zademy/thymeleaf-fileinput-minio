// Script para cargar jQuery y otros scripts en el orden correcto
(function() {
  // Función para cargar un script
  function loadScript(src, integrity, crossorigin, callback) {
    const script = document.createElement('script');
    script.src = src;
    if (integrity) script.integrity = integrity;
    if (crossorigin) script.crossOrigin = crossorigin;
    script.onload = callback;
    document.head.appendChild(script);
  }

  // Cargar jQuery primero
  loadScript(
    'https://code.jquery.com/jquery-3.6.0.min.js',
    'sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=',
    'anonymous',
    function() {
      // Definir jQuery globalmente si es necesario
      window.jQuery = window.jQuery || window.$ || jQuery;
      window.$ = window.jQuery;
      
      console.log('jQuery cargado correctamente');
      
      // Disparar un evento para notificar que jQuery está listo
      const jQueryReadyEvent = new Event('jQueryReady');
      document.dispatchEvent(jQueryReadyEvent);
      
      // Ahora podemos cargar otros scripts que dependen de jQuery
      // Puedes añadir más scripts aquí si es necesario
    }
  );
})();
