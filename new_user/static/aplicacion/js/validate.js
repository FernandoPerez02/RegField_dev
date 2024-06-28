const formulario = document.getElementById('form_newuser');
const inputs = document.querySelectorAll('.form-control');

const expresiones = {
    usuario: /^[a-zA-Z]{6,15}$/i,
    correo: /^[\w.-]{1,100}@gmail(?:\.com|\.co)$/i,
    contrasena: /^(?=.*[A-Z])(?=.*[a-zA-Z].*[a-zA-Z].*[a-zA-Z].*[a-zA-Z])[\w*.-]{4,8}$/i,

    contrasena2: /^[\w*.-]{4,8}$/i
}

var mensajeError = {
    campoVacio: function() {
        return 'Este campo es obligatorio, debes llenarlo.'
    },

    caracterInvalido: function() {
        return 'Caracter invalido para este campo.'
    },

}


const validateform = (e) => {
    let error = '';
    let valido = '';
    
    switch (e.target.name) {
        case 'usuario':
            if(e.target.value === '') {
                error = mensajeError.campoVacio()
                e.target.classList.add('error');

            } else if (!expresiones.usuario.test(e.target.value)) {
                error = mensajeError.caracterInvalido()
                
            } else {
                valido = 'Usuario Valido.';
            }
            document.getElementById('usuario_error').textContent = error;
            document.getElementById('usuario_valido').textContent = valido;
        break;

        case 'correo':
            if(e.target.value == '') {
                error = mensajeError.campoVacio()
                e.target.classList.add('error');
                
            } else if (!expresiones.correo.test(e.target.value)) {
                error = mensajeError.caracterInvalido()
                
            } else {
                valido = 'Correo valido'
            }
            document.getElementById('correo_error').textContent = error;
            document.getElementById('correo_valido').textContent = valido;
        break;

        case 'contrasena':
            if(e.target.value == '') {
                error = mensajeError.campoVacio()
                e.target.classList.add('error');
                
            } else if (!expresiones.contrasena.test(e.target.value)) {
                error = mensajeError.caracterInvalido()
                
            } else {
                valido = 'Contraseña valida'
            }
            document.getElementById('password_error').textContent = error;
            document.getElementById('password_valido').textContent = valido;

        break;

        case 'contrasena2':
            if(e.target.value == '') {
                error = mensajeError.campoVacio()
                e.target.classList.add('error');
                
            } else if (!expresiones.contrasena2.test(e.target.value)) {
                error = mensajeError.caracterInvalido()
                
            } else {
                valido = 'Correo valido'
            }
            document.getElementById('password2_error').textContent = error;
            document.getElementById('password2_valido').textContent = valido;


        break

        case 'ter_con':
            if(e.target.value == '') {
                error = mensajeError.campoVacio()
                e.target.classList.add('error');
                
            } else {
                e.classList.remove('error');
            }
            document.getElementById('ter_con_error').textContent = error;

        break

    }

}

inputs.forEach((input) =>{
    input.addEventListener('keyup', validateform);
    input.addEventListener('blur', validateform);
})

