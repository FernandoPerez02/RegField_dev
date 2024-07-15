document.addEventListener('DOMContentLoaded', function() {
    if (document.getElementById('empleado_select')) {
      listarEmpleados();
    }
    if (document.getElementById('tipo_select')) {
      obtenerTipoRegistro();
    }
    if (document.getElementById('producto_select')) {
      listaestado();
    }

    if (document.getElementById('product_select')) {
      listaproduct();
    }
  });

  function listaproduct() {
    const prod_select = document.getElementById('product_select');
    if (!prod_select) return;

    const url = prod_select.dataset.url;
    fetch(url)
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok')
      }
      return response.json();
    })
    .then(data => {
      data.forEach(product => {
        const option = document.createElement('option');
        option.value = product.id_producto;
        option.textContent = product.producto;
        prod_select.appendChild(option);
      });
    })
    .catch(error => {
      console.error('Hubo un problema con la solicitud fetch:', error)
    });

  }

  function asignarproduc() {
    const select = document.getElementById('product_select');
    if (select) {
      const idProducto = select.value;
      document.getElementById('productid').value = idProducto;
    }
  }
  
  function listaestado() {
    const productoSelect = document.getElementById('producto_select');
    if (!productoSelect) return;
    
    const url = productoSelect.dataset.url;
    fetch(url)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        data.forEach(estado => {
          const option = document.createElement('option');
          option.value = estado.id_estado;
          option.textContent = estado.estado;
          productoSelect.appendChild(option);
        });
      })
      .catch(error => {
        console.error('Hubo un problema con la solicitud fetch:', error);
      });
  }
  
  function asignarIdestado() {
    const select = document.getElementById('producto_select');
    if (select) {
      const idEstado = select.value;
      document.getElementById('estadoid').value = idEstado;
    }
  }
  
  function listarEmpleados() {
    const empleadoSelect = document.getElementById('empleado_select');
    if (!empleadoSelect) return;
  
    const url = empleadoSelect.dataset.url;
    fetch(url)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        data.forEach(empleado => {
          const option = document.createElement('option');
          option.value = empleado.id_empleado;
          option.textContent = empleado.nombre;
          empleadoSelect.appendChild(option);
        });
      })
      .catch(error => {
        console.error('Hubo un problema con la solicitud Fetch:', error);
      });
  }
  
  function asignarIdEmpleado() {
    const select = document.getElementById('empleado_select');
    if (select) {
      const idEmpleado = select.value;
      document.getElementById('empleado').value = idEmpleado;
    }
  }
  
  function obtenerTipoRegistro() {
    const tipoSelect = document.getElementById('tipo_select');
    if (!tipoSelect) return;
  
    const urlTipoRegistro = tipoSelect.dataset.url;
    fetch(urlTipoRegistro)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        data.forEach(tiporegistro => {
          const option = document.createElement('option');
          option.value = tiporegistro.id_tipo_registro;
          option.textContent = tiporegistro.tipo_registro;
          tipoSelect.appendChild(option);
        });
      })
      .catch(error => {
        console.error('Hubo un problema con la solicitud Fetch:', error);
      });
  }
  
  function asignarIdTipoRegistro() {
    const select = document.getElementById('tipo_select');
    if (select) {
      const idTipoRegistro = select.value;
      document.getElementById('tipo_registro').value = idTipoRegistro;
    }
  }
  