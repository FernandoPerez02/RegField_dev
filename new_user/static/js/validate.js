const formulario = document.getElementById('form_newuser');
const selects = document.querySelectorAll('.form-select');
const botonenviar = document.getElementById('btn_register');
const inputs = document.querySelectorAll('input');

const expresiones = {
    rol: ['Administrador', 'Encargado'],
    usuario: /^[a-zA-Z\s]{6,15}$/i,
    documento: /^[0-9]{6,10}$/i,
    gmail: /^[\w.-]{1,100}@gmail(?:\.com|\.co)$/i,
    contrasena: /^(?=.*[A-Z])(?=.*[\d!#$&*])[A-Za-z\d!#$&*]{4,8}$/,
};

const mensajeError = {
    campoVacio: () => 'Este campo es obligatorio.',
    caracterInvalido: () => 'Caracter inválido para este campo.',
    longitudvalida: (min, max) => `La longitud debe estar entre ${min} y ${max} caracteres.`,
};

const validateform = (e) => {
    let error = '';
    let valido = '';
    const errors = {};

    const submiterrorcontroler = () => {
        const haserror = Object.values(errors).some(val => val === true);
        botonenviar.toggleAttribute('disabled', haserror);
    };

    const showerror = (check, element) => {
        if (check) {
            element.classList.add('error'); 
            errors[element.name] = true;
        } else {
            element.classList.remove('error');
            errors[element.name] = false;
        }
        submiterrorcontroler();
    };

    switch (e.target.name) {
        case 'rol':
            if (!expresiones.rol.includes(e.target.value)) {
                error = 'Debes asignar un rol: Administrador o Encargado.'; 
                showerror(true, e.target);
            } else {
                showerror(false, e.target);
            }
            document.getElementById('rol_error').textContent = error;
            break;

        case 'usuario':
            if (e.target.value === '') {
                error = mensajeError.campoVacio();
                showerror(true, e.target);
            } else if (e.target.value.length < 6 || e.target.value.length > 15) {
                error = mensajeError.longitudvalida(6, 15);
                showerror(true, e.target);
            } else if (!expresiones.usuario.test(e.target.value)) {
                error = 'No se admiten caracteres especiales';
                showerror(true, e.target);
            } else {
                showerror(false, e.target);
                valido = 'Usuario válido';
            }
            document.getElementById('usuario_error').textContent = error;
            document.getElementById('usuario_valido').textContent = valido;
            break;

        case 'documento':
            if (e.target.value === '') {
                error = mensajeError.campoVacio();
                showerror(true, e.target);
            } else if (e.target.value.length < 6 || e.target.value.length > 10) {
                error = mensajeError.longitudvalida(6, 10);
                showerror(true, e.target);
            } else if (!expresiones.documento.test(e.target.value)) {
                error = mensajeError.caracterInvalido();
                showerror(true, e.target);
            } else {
                showerror(false, e.target);
            }
            document.getElementById('doc_error').textContent = error;
            break;

        case 'gmail':
            if (e.target.value === '') {
                error = mensajeError.campoVacio();
                showerror(true, e.target);
            } else if (!expresiones.gmail.test(e.target.value)) {
                error = mensajeError.caracterInvalido();
                showerror(true, e.target);                        
            } else {
                showerror(false, e.target);
            }
            document.getElementById('correo_error').textContent = error;
            break;

        case 'contrasena':
            if (e.target.value === '') {
                error = mensajeError.campoVacio();
                showerror(true, e.target);
            } else if (e.target.value.length < 4 || e.target.value.length > 8) {
                error = mensajeError.longitudvalida(4, 8);
                showerror(true, e.target);
            } else if (!expresiones.contrasena.test(e.target.value)) {
                error = mensajeError.caracterInvalido();
                showerror(true, e.target);
            } else {
                showerror(false, e.target);
            }

            if (e.target.value.length >= 4 && e.target.value.length <= 8) {
                if (!/[A-Z]/.test(e.target.value)) {
                    error += ' Debe contener al menos una letra mayúscula.';
                }
                if (!/[!@#$%^&*(),.?":{}|<>]/.test(e.target.value)) {
                    error += ' Debe contener al menos un carácter especial.';
                }
            }
            document.getElementById('password_error').textContent = error;
            document.getElementById('sugerencia_password').textContent = error;
            break;

        case 'contrasena2':
            const contrasena = document.getElementById('password').value;
            if (e.target.value === '') {
                error = mensajeError.campoVacio();
                showerror(true, e.target);
            } else if (e.target.value !== contrasena) {
                error = 'Las contraseñas no coinciden.';
                showerror(true, e.target);
            } else {
                showerror(false, e.target);
                valido = 'Contraseñas coinciden';
            }
            document.getElementById('password2_error').textContent = error;
            document.getElementById('password2_valido').textContent = valido;
            break;

        case 'terminos_condiciones':
            if (!e.target.checked) {
                error = mensajeError.campoVacio();
                showerror(true, e.target);
            } else {
                showerror(false, e.target);
            }
            document.getElementById('ter_con_error').textContent = error;
            break;
    }
};

formulario.addEventListener('submit', (event) => {
    event.preventDefault();
    inputs.forEach((input) => validateform({ target: input }));
    selects.forEach((select) => validateform({ target: select }));
    let alerta = '';

    const errores = document.querySelectorAll('.error');
    if (errores.length > 0) {
        alerta = 'Aún tienes campos por llenar.';
        console.log(errores);
    } else {
        alerta = 'Registro Exitoso';
        formulario.submit();
    }
    document.getElementById('alertError').textContent = alerta;
});

inputs.forEach((input) => {
    input.addEventListener('blur', validateform);
});

selects.forEach((select) => {
    select.addEventListener('blur', validateform);
});
