/**
 * Inicialización de Mermaid v11 con módulos ES
 * 
 * Este script se encarga de inicializar Mermaid.js con la configuración adecuada
 * para la generación de diagramas en la documentación.
 */

import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs';

// Configuración de Mermaid
const mermaidConfig = {
    startOnLoad: true,
    theme: 'default',
    securityLevel: 'loose',
    fontFamily: 'Arial, sans-serif',
    themeCSS: '.label { font-family: Arial; }',
    themeVariables: {
        primaryColor: '#f0f0f0',
        primaryTextColor: '#333',
        primaryBorderColor: '#666',
        lineColor: '#333',
        secondaryColor: '#f8f8f8',
        tertiaryColor: '#f0f0f0'
    },
    flowchart: {
        useMaxWidth: false,
        htmlLabels: true,
        curve: 'basis'
    },
    gantt: {
        barHeight: 20,
        fontSize: 12,
        fontFamily: 'Arial, sans-serif'
    },
    er: {
        useMaxWidth: false
    },
    sequence: {
        useMaxWidth: false,
        noteFontWeight: 'normal'
    }
};

// Inicializar Mermaid cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', () => {
    try {
        // Inicializar Mermaid con la configuración
        mermaid.initialize(mermaidConfig);
        
        // Renderizar todos los diagramas
        mermaid.run({
            querySelector: '.mermaid',
            suppressErrors: true
        }).catch(error => {
            console.error('Error al renderizar diagramas Mermaid:', error);
        });
        
        // Manejar actualizaciones dinámicas del contenido
        const observer = new MutationObserver((mutations) => {
            mermaid.run({
                querySelector: '.mermaid:not(.rendered)',
                suppressErrors: true
            });
        });
        
        // Observar cambios en el contenido del documento
        observer.observe(document.body, {
            childList: true,
            subtree: true
        });
        
        console.log('Mermaid v11 inicializado correctamente');
    } catch (error) {
        console.error('Error al inicializar Mermaid:', error);
    }
});

// Exportar para uso en otros módulos si es necesario
export { mermaid, mermaidConfig };
