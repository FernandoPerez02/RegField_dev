document.addEventListener('DOMContentLoaded', function() {
  listarEmpleados();
  obtenerTipoRegistro();
});

function listarEmpleados() {
  const url = "{% url 'obtenerempleado' %}";
  fetch(url)
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      const select = document.getElementById('empleado_select');
      data.forEach(empleado => {
        const option = document.createElement('option');
        option.value = empleado.id_empleado;
        option.textContent = empleado.nombre;
        select.appendChild(option);
      });
    })
    .catch(error => {
      console.error('Hubo un problema con la solicitud Fetch:', error);
    });
}

function asignarIdEmpleado() {
  const select = document.getElementById('empleado_select');
  const idEmpleado = select.value;
  document.getElementById('empleado').value = idEmpleado;
}

function obtenerTipoRegistro() {
  const urlTipoRegistro = "{% url 'obtenertiporegistro' %}";
  fetch(urlTipoRegistro)
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      const select = document.getElementById('tipo_select');
      data.forEach(tiporegistro => {
        const option = document.createElement('option');
        option.value = tiporegistro.id_tipo_registro;
        option.textContent = tiporegistro.tipo_registro;
        select.appendChild(option);
      });
    })
    .catch(error => {
      console.error('Hubo un problema con la solicitud Fetch:', error);
    });
}

function asignarIdTipoRegistro() {
  const select = document.getElementById('tipo_select');
  const idTipoRegistro = select.value;
  document.getElementById('tipo_registro').value = idTipoRegistro;
}