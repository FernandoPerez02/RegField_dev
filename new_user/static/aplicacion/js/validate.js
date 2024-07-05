const formulario = document.getElementById('form_newuser');
const selects = document.querySelectorAll('.form-select');
const botonenviar = document.getElementById('btn_register');

const expresiones = {
    rol: ['Administrador', 'Encargado'],
    usuario: /^[a-zA-Z\s]{6,15}$/i,
    documento: /^[0-9]{6,10}$/i,
    gmail: /^[\w.-]{1,100}@gmail(?:\.com|\.co)$/i,
    contrasena: /^(?=.*[A-Z])(?=.*[d!#$&*])[A-Za-z\d!#$&*]{4,8}$/,
}

const mensajeError = {
    campoVacio: function() {
        return 'Este campo es obligatorio.'
    },

    caracterInvalido: function() {
        return 'Caracter invalido para este campo.'
    },

    longitudvalida: function(min, max) {
        return `La longitud debe estar entre ${min} y ${max} caracteres.`
    }
}


const validateform = (e) => {
    let error = '';
    const errors = {};
    let requisito = '';
    valido = '';

    function submiterrorcontroler() {
        const haserror = Object.values(errors).some(val => val === true);
        botonenviar.toggleAttribute('disabled', haserror);
    }
    
    function showerror(check, element) {
        if (check) {
            element.classList.add('error'); 
            errors[element.name] = true;
        } else {
            element.classList.remove('error');
            errors[element.name] = false;
        }
        submiterrorcontroler();
    }

    switch (e.target.name) {
        case 'rol':
            if (!expresiones.rol.includes(e.target.value)) {
                error = 'Debes asignar un rol: Administrador o Encargado.' 
                showerror(true, e.target);
            } else {
                showerror(false, e.target);
            }
            document.getElementById('rol_error').textContent = error;
        break

        case 'usuario':
            if (e.target.value === '') {
                error = mensajeError.campoVacio()
                showerror(true, e.target);

            } else if(e.target.value.length < 6 || e.target.value.length > 15) {
                error = mensajeError.longitudvalida(6, 15);
                showerror(true, e.target);
            } else if (!expresiones.usuario.test(e.target.value)) {
                error = 'No se admiten caracteres especiales'
                showerror(true, e.target);

            }else {
                showerror(false, e.target);
            };
            
            document.getElementById('usuario_error').textContent = error;
            document.getElementById('usuario_valido').textContent = valido;
        
            case 'documento':
                if (e.target.value === '') {
                    error = mensajeError.campoVacio()
                    showerror(true, e.target);
                } else if(e.target.value.length < 8 || e.target.value.length > 10) {
                    error = mensajeError.longitudvalida(4, 10);
                    showerror(true, e.target);
                } else {
                    showerror(false,e.target);
                };
                document.getElementById('doc_error').textContent = error;
            
                case 'gmail':
                    if(e.target.value == '') {
                        error = mensajeError.campoVacio()
                        showerror(true, e.target);
                    } else if (!expresiones.gmail.test(e.target.value)) {
                        error = mensajeError.caracterInvalido()
                        showerror(true, e.target);                        
                    } else {
                        showerror(true, e.target);
                    }
                    document.getElementById('correo_error').textContent = error;
                break;
        
                case 'contrasena':
                    
                    if (e.target.value == '') {
                        error = mensajeError.campoVacio()
                        e.target.classList.add('error');
        
                    } else if (e.target.value.length < 4 || e.target.value.length > 8) {
                        error = mensajeError.longitudvalida(4, 8)
        
                    } else if (!expresiones.contrasena.test(e.target.value)) {
                        error = mensajeError.caracterInvalido()
        
                    } else {
                        showerror(false, e.target);   
                    } 
        
                    if (e.target.value.length >= 4 && e.target.value.length <= 8) {
                        if (!/[A-Z]/.test(e.target.value)) {
                         requisito += ' Debe contener al menos una letra mayúscula.';
                        }
        
                       if (!/[!@#$%^&*(),.?":{}|<>]/.test(e.target.value)) {
                         requisito += ' Debe contener al menos un carácter especial.';
                       }
                    }
                    
        
                    document.getElementById('password_error').textContent = error;
                    document.getElementById('sugerencia_password').textContent = requisito;
        
                break;
        
                case 'contrasena2':
                    const contrasena = document.getElementById('password')
                    if(e.target.value == '') {
                        error = mensajeError.campoVacio()
                        showerror(true, e.target);
        
                    } else if (e.target.value !== contrasena) {
                        error = 'Las contraseñas no coiciden.';
                        showerror(true, e.target);
        
                    } else {
                        showerror(false, e.target);
                    }
                    document.getElementById('password2_error').textContent = error;
                    document.getElementById('password2_valido').textContent = valido;
                break
        
                case 'ter_con':
                    if(e.target.value == '') {
                        error = mensajeError.campoVacio()
                        showerror(true, e.target);
                        
                    } else {
                        showerror(false, e.target);
                    }
                    document.getElementById('ter_con_error').textContent = error;
        
                break
        
    }
}

formulario.addEventListener('submit', (event) => {
    event.preventDefault();
    inputs.forEach((input) => validateform({target: input}));
    selects.forEach((selects) => validateform({target: selects}));
    let alerta = '';

    const errores = document.querySelectorAll('.mensaje_error');
    if (errores.length > 0) {
        alerta = 'Aun tienes campos por llenar.'
    } else {
        alerta = 'Registro Exitoso'
        formulario.submit();
    }
    document.getElementById('alertError').textContent = alerta;
});

let timeout;

selects.forEach((selects) => {
    selects.addEventListener('change', validateform);
    selects.addEventListener('focus', validateform);
})
const inputs = document.querySelectorAll('input');

inputs.forEach((input) =>{
    input.addEventListener('keydown', (event) => {
        clearTimeout(timeout);
        timeout = setTimeout (() => {
            validateform(event);
        }, 300);
    });
});