// Obtener los elementos HTML relevantes
const gastoProximoMes = document.querySelector('#gastoProximoMes');
const botonIngresarGasto = document.getElementById('botonIngresarGasto');


const titleBanco1 = document.querySelector('#titleBanco1');
const titleBanco2 = document.querySelector('#titleBanco2');
const titleBanco3 = document.querySelector('#titleBanco3');

const totalBanco1 = document.querySelector('#totalBanco1');
const totalBanco2 = document.querySelector('#totalBanco2');
const totalBanco3 = document.querySelector('#totalBanco3');

// Obtener los datos del servicio correspondiente
const servicio_gastoProximoMes = 'http://localhost:8000/gastoProximoMes';
const servicio_totalesTarjeta = 'http://localhost:8000/totalesTarjeta';

// Actualizar la información de la página
function actualizarInformacion() {
  // Actualizar el gasto del próximo mes
  fetch(servicio_gastoProximoMes)
    .then(response => response.json())
    .then(data => gastoProximoMes.textContent = "$" + data);

    // Actualizar los totales de gastos por banco
    fetch(servicio_totalesTarjeta)
    .then(response => response.json())
    .then(data => {
      titleBanco1.textContent = data[0].nombre;
      totalBanco1.textContent = "$" + data[0].totales;

      titleBanco2.textContent = data[1].nombre;
      totalBanco2.textContent = "$" + data[1].totales;
      
      titleBanco3.textContent = data[2].nombre;
      totalBanco3.textContent = "$" + data[2].totales;
    });
    
}

// Llamar a la función de actualización de información cuando se carga la página
document.addEventListener("DOMContentLoaded", function () {
    actualizarInformacion();
});

// Agregar un evento de clic al botón de "Ingresar Gasto"
botonIngresarGasto.addEventListener('click', () => {
  window.location.href = 'ingresarGasto.html';
});