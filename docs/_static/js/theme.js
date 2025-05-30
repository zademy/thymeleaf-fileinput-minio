// Archivo JavaScript básico para el tema
document.addEventListener('DOMContentLoaded', function() {
  // Función para manejar la búsqueda
  const searchInput = document.getElementById('rtd-search-form');
  if (searchInput) {
    const input = searchInput.querySelector('input[name="q"]');
    if (input) {
      input.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
          // Asegurar que el formulario se envíe correctamente
          searchInput.submit();
        }
      });
    }
  }
});
