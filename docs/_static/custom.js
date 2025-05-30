// Cargar Fira Code desde Google Fonts
(function() {
    const link = document.createElement('link');
    link.href = 'https://fonts.googleapis.com/css2?family=Fira+Code:wght@300;400;500;600;700&display=swap';
    link.rel = 'stylesheet';
    document.head.appendChild(link);
    
    // Aplicar Fira Code a todos los elementos de código
    document.addEventListener('DOMContentLoaded', function() {
        // Crear una hoja de estilo
        const style = document.createElement('style');
        style.textContent = `
            code, pre, tt, .highlight, .literal, .rst-content code, .rst-content tt, 
            .rst-content pre.literal-block, .rst-content div[class^='highlight'] {
                font-family: 'Fira Code', monospace !important;
                font-feature-settings: "calt" 1;
            }
            
            .rst-content code, .rst-content tt {
                font-family: 'Fira Code', monospace !important;
            }
            
            .highlight * {
                font-family: 'Fira Code', monospace !important;
            }
        `;
        document.head.appendChild(style);
    });
})();
