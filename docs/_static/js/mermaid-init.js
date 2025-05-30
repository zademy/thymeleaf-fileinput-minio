document.addEventListener('DOMContentLoaded', function() {
    mermaid.initialize({
        startOnLoad: true,
        theme: 'forest',
        securityLevel: 'loose',
        flowchart: { curve: 'linear' },
        sequence: { showSequenceNumbers: true }
    });
    mermaid.init(undefined, '.mermaid');
});
