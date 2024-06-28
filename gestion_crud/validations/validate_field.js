/* Las validaciones se implementaran mediante funciones.
Para así poderlas reutilizar en campos que posean requisitos semejantes  */

const expresiones = {
    usuario: /^[A-Z]{6,15}$/i,
    documento: /^[0-9]{6,10}$/,
    correo: /^[A-Z-0-9]{4,100}@.(com|co)$/i,
    contraseña: /^[A-Z-0-9]{4,8}$/i,
  };

class ValidateUserform{ 
    constructor(rol, usuario, gmail, password, confipassword) {
        this.rol = rol;
        this.usuario = usuario;
        this.gmail = gmail;
        this.password = password;
        this.confipassword = confipassword; 
    }

}

function validateName() {
    const caracteres = /^[A-Z]{6,15}$/i
    
}

