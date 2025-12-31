/**
 * EYESH Question Generator - Main Application Logic
 */

// Utility functions
function getLevelColor(level) {
    const colors = {
        'A1': 'bg-green-100 text-green-800',
        'A2': 'bg-green-100 text-green-800',
        'B1': 'bg-yellow-100 text-yellow-800',
        'B2': 'bg-yellow-100 text-yellow-800',
        'C1': 'bg-red-100 text-red-800',
        'C2': 'bg-red-100 text-red-800'
    };
    return colors[level] || 'bg-gray-100 text-gray-800';
}

function formatFocus(focus) {
    return focus.replace(/_/g, ' ').replace(/\b\w/g, c => c.toUpperCase());
}

// Initialize tooltips and other UI enhancements
document.addEventListener('DOMContentLoaded', () => {
    console.log('EYESH Question Generator loaded');
});
