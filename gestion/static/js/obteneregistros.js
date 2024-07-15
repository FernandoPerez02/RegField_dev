document.addEventListener('DOMContentLoaded', function() {
    listarEmpleados();
    obtenerTipoRegistro();
    listaestado();
  });

  function listaestado() {
    const url = document.getElementById('producto_select').dataset.url;
    fetch(url)
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      const select = document.getElementById('producto_select');
      data.forEach(estado => {
        const option = document.createElement('option');
        option.value = estado.id_estado;
        option.textContent = estado.estado;
        select.appendChild(option);
      });
    })
    .catch(error => {
      console.error('Hubo un problema con la solicitud fetch:', error);
    });
  }

  function asignarIdestado() {
    const select = document.getElementById('producto_select');
    const idEstado = select.value;
    document.getElementById('estadoid').value = idEstado;
  }
  
  function listarEmpleados() {
    const url = document.getElementById('empleado_select').dataset.url;
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
    const urlTipoRegistro = document.getElementById('tipo_select').dataset.url;
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