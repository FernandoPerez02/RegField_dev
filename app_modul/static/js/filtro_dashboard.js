async function actualizarFechas() {
    const tipoRegistro = document.getElementById('tipo-registro').value;

    try {
        const response = await fetch(`/obtener_fechas/?tipo_registro=${tipoRegistro}`);
        if (!response.ok) {
            throw new Error('Error en la respuesta de la red');
        }

        const data = await response.json();

        const fechaInicioSelect = document.getElementById('fecha_inicio');
        const fechaFinSelect = document.getElementById('fecha_fin');

        // Limpiar las opciones actuales
        fechaInicioSelect.innerHTML = '';
        fechaFinSelect.innerHTML = '';

        // Añadir opciones de fecha al select de inicio y fin
        data.fechas.forEach(fecha => {
            const option = document.createElement('option');
            option.value = fecha;
            option.textContent = fecha;
            fechaInicioSelect.appendChild(option);

            // Añadir la misma opción al select de fecha fin
            const optionFin = option.cloneNode(true);
            fechaFinSelect.appendChild(optionFin);
        });

        // Opcional: Seleccionar la primera opción de fecha si hay alguna
        if (fechaInicioSelect.options.length > 0) {
            fechaInicioSelect.selectedIndex = 0;
            fechaFinSelect.selectedIndex = 0;
        }

    } catch (error) {
        console.error('Hubo un problema con la solicitud:', error);
        // Puedes mostrar un mensaje al usuario aquí si es necesario
    }
}

// Añadir un evento para que se ejecute la función al cambiar el select
document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('tipo-registro').addEventListener('change', actualizarFechas);
});
