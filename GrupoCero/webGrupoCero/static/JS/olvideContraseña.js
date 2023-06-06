const ingreso = document.getElementById('formulario-login');
const inputs_ingreso = document.querySelectorAll('#formulario input');


/*validar que todos las validaciones sean correctas al presionar ingresar*/
function validar(e){
    if(validarCorreo() && validarPassword()){
        return true;
    }else{
        e.preventDefault();
        return false;
    }
}
/*validar que el usuario tenga formato email*/
function validarCorreo(){
    var correo = document.getElementById('correo').value;
    arroba = correo.indexOf("@");
    punto =  correo.lastIndexOf(".");
    if (arroba < 1 || ( punto - arroba < 2 )||correo===""){
        document.getElementById('grupo_correo').classList.remove('formulario_grupo-correcto');
        document.getElementById('grupo_correo').classList.add('formulario_grupo-incorrecto');
        document.querySelector('#grupo_correo .formulario_input-error').classList.add('formulario_input-error-activo');
        return false;
    }else{
        document.getElementById('grupo_correo').classList.remove('formulario_grupo-incorrecto');
        document.getElementById('grupo_correo').classList.add('formulario_grupo-correcto');  
        document.querySelector('#grupo_correo .formulario_input-error').classList.remove('formulario_input-error-activo');  
        return true;
      }
}



