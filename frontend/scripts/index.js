const form = document.getElementById('gasto-form');
const valorCuotaInput = form.querySelector('#valor_cuota');
const interesesCheckbox = form.querySelector('#intereses');

function calcularValorCuota(monto, cantidadCuotas, tieneIntereses) {
  let valorCuota = monto / cantidadCuotas;
  if (tieneIntereses) {
    valorCuota *= 1.1; // Aplica un interés del 10%
  }
  return valorCuota.toFixed(2);
}

function cargarBancos() {
    const selectBancos = document.getElementById("idBanco");
  
    fetch("http://localhost:8000/bancos")
      .then((response) => response.json())
      .then((data) => {
        data.forEach((banco) => {
          const option = document.createElement("option");
          option.value = banco.id;
          option.text = banco.nombre;
          selectBancos.add(option);
        });
      })
      .catch((error) => {
        console.error("Error:", error);
        // TODO: mostrar mensaje de error al usuario
      });
  }

function actualizarValorCuota() {
  const monto = parseFloat(form.monto.value);
  const cantidadCuotas = parseInt(form.cantidad_cuotas.value);
  const tieneIntereses = interesesCheckbox.checked;

  if (isNaN(monto) || isNaN(cantidadCuotas)) {
    valorCuotaInput.value = '';
  } else {
    const valorCuota = calcularValorCuota(monto, cantidadCuotas, tieneIntereses);
    valorCuotaInput.value = valorCuota;
  }
}

interesesCheckbox.addEventListener('change', function () {
  if (this.checked) {
    valorCuotaInput.disabled = false;
  } else {
    valorCuotaInput.disabled = true;
  }
  actualizarValorCuota();
});

form.addEventListener('submit', function (event) {
    event.preventDefault();
  
    const descripcion = form.descripcion.value;
    const monto = parseFloat(form.monto.value);
    const idBanco = parseInt(form.idBanco.value);
    const cantidadCuotas = parseInt(form.cantidad_cuotas.value);
    const tieneIntereses = interesesCheckbox.checked;
    const valorCuota = parseFloat(valorCuotaInput.value);
  
    const data = {
      descripcion,
      monto,
      idBanco,
      cantidad_cuotas: cantidadCuotas,
      intereses: tieneIntereses,
      valor_cuota: valorCuota,
    };
  
    fetch('http://localhost:8000/gasto', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    })
      .then(response => {
        if (response.ok) {
          window.location.replace('success.html');
        } else {
          throw new Error('Error al enviar los datos');
        }
      })
      .catch((error) => {
        console.error('Error:', error);
        // TODO: mostrar mensaje de error al usuario
      });
  });

  document.addEventListener("DOMContentLoaded", function () {
    cargarBancos();
  });

form.monto.addEventListener('input', actualizarValorCuota);
form.cantidad_cuotas.addEventListener('input', actualizarValorCuota);
