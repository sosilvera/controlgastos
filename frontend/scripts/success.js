const consumosMesUrl = 'http://localhost:8000/consumosMes';

// Hacer una petición GET a la URL del servicio y obtener los datos
fetch(consumosMesUrl)
  .then(response => response.json())
  .then(data => {
    // Obtener la lista de meses disponibles
    const meses = [...new Set(data.map(item => item.descripcion))];

    // Obtener la lista de gastos disponibles
    const gastos = [...new Set(data.map(item => item.monto))];

    // Crear la tabla
    const table = document.createElement('table');
    table.className = 'table';
    
    // Crear la fila de encabezado de los meses
    const headerRow = document.createElement('tr');
    const emptyCell = document.createElement('th');
    headerRow.appendChild(emptyCell);
    
    meses.forEach(mes => {
      const monthCell = document.createElement('th');
      monthCell.textContent = mes;
      headerRow.appendChild(monthCell);
    });
    
    const totalCell = document.createElement('th');
    totalCell.textContent = 'Total';
    headerRow.appendChild(totalCell);
    table.appendChild(headerRow);

    // Crear filas para cada gasto
    gastos.forEach(gasto => {
      const row = document.createElement('tr');
      const gastoCell = document.createElement('td');
      gastoCell.textContent = gasto;
      row.appendChild(gastoCell);
      
      // Calcular la suma total para este gasto
      const gastoTotal = meses.reduce((total, mes) => {
        const consumo = data.find(item => item.descripcion === mes && item.monto === gasto);
        return total + (consumo ? consumo.banco : 0);
      }, 0).toFixed(2);

      // Agregar las celdas para cada mes
      meses.forEach(mes => {
        const cell = document.createElement('td');
        const consumo = data.find(item => item.descripcion === mes && item.monto === gasto);
        cell.textContent = consumo ? consumo.banco : '-';
        row.appendChild(cell);
      });

      // Agregar la celda para el total del gasto
      const totalCell = document.createElement('td');
      totalCell.textContent = gastoTotal;
      row.appendChild(totalCell);
      table.appendChild(row);
    });

    // Calcular la fila de totales por mes
    const totalRow = document.createElement('tr');
    const totalCellLabel = document.createElement('td');
    totalCellLabel.textContent = 'Total';
    totalRow.appendChild(totalCellLabel);
    
    meses.forEach(mes => {
      const monthTotal = data.filter(item => item.descripcion === mes)
        .reduce((total, item) => total + item.banco, 0).toFixed(2);
      const monthTotalCell = document.createElement('td');
      monthTotalCell.textContent = monthTotal;
      totalRow.appendChild(monthTotalCell);
    });

    // Agregar la celda para el total general
    const grandTotal = data.reduce((total, item) => total + item.banco, 0).toFixed(2);
    const grandTotalCell = document.createElement('td');
    grandTotalCell.textContent = grandTotal;
    totalRow.appendChild(grandTotalCell);
    table.appendChild(totalRow);

    // Agregar la tabla al contenedor HTML
    const tableContainer = document.getElementById('table-container');
    tableContainer.appendChild(table);
  })