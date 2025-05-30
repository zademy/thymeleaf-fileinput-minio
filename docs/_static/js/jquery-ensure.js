// Este script garantiza que jQuery esté disponible globalmente
document.addEventListener('DOMContentLoaded', function() {
  // Verificar si jQuery ya está cargado
  if (typeof jQuery === 'undefined') {
    // Si no está cargado, cargar jQuery dinámicamente
    const script = document.createElement('script');
    script.src = 'https://code.jquery.com/jquery-3.6.0.min.js';
    script.integrity = 'sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=';
    script.crossOrigin = 'anonymous';
    script.onload = function() {
      console.log('jQuery cargado dinámicamente');
      // Disparar un evento personalizado para notificar que jQuery está disponible
      document.dispatchEvent(new Event('jQueryReady'));
    };
    document.head.appendChild(script);
  } else {
    console.log('jQuery ya está cargado');
    // Disparar el evento jQueryReady inmediatamente si jQuery ya está disponible
    document.dispatchEvent(new Event('jQueryReady'));
  }
});
