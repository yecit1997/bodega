// Función para filtrar la tabla
document.getElementById('searchInput').addEventListener('keyup', function() {
    let filter = this.value.toLowerCase();
    let rows = document.querySelectorAll('#userTable tbody tr');

    rows.forEach(row => {
        let cells = row.getElementsByTagName('td');
        let found = false;

        for (let i = 1; i < cells.length - 1; i++) { // Comienza desde 1 para omitir la foto y termina antes de las acciones
            if (cells[i].textContent.toLowerCase().includes(filter)) {
                found = true;
                break;
            }
        }

        row.style.display = found ? '' : 'none'; // Muestra u oculta la fila
    });
});





