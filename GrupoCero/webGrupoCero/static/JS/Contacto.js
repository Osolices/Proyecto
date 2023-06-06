const contacto = document.getElementById('formulario');
const inputs_contacto = document.querySelectorAll('#formulario input');

window.onload= iniciar;
function iniciar(){
    document.getElementById("enviar").addEventListener('click',validar,false);
}

function validarCorreo(){
    var correo = document.getElementById('txtcorreo').value;
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


function validaRut() {
    let rut=document.getElementById("txtrut").value;
    let largo= rut.trim().length;
    console.log('Largo:'+largo);
    if (largo<10) {
        document.getElementById('grupo_rut').classList.remove('formulario_grupo-correcto');
        document.getElementById('grupo_rut').classList.add('formulario_grupo-incorrecto');
        document.querySelector('#grupo_rut .formulario_input-error').classList.add('formulario_input-error-activo');
        return false;
    }
    let el_rut=rut.trim();
    let num=3;let suma=0;
    for (let index = 0; index < 8; index++) {
        let caracter=el_rut.slice(index,index+1);
        console.log('caracter:'+caracter+" x "+num);
        suma=suma+(caracter*num);
        num=num-1;
        if (num==1) {
            num=7;
        }
        
    }
    console.log('Suma:'+suma);
    let resto= suma % 11;
    let dv = 11 - resto;
    let el_digito;
    if (dv>9) {
        if (dv==10) {
            console.log('K');
            el_digito='K';
        } else {
            console.log('0');
            el_digito=0;
        }
    }else{
        console.log('Digito:'+dv);
        el_digito=dv;
    }
    let tu_digito=el_rut.slice(9,10);
    if (tu_digito==el_digito) {
        document.getElementById('grupo_rut').classList.remove('formulario_grupo-incorrecto');
        document.getElementById('grupo_rut').classList.add('formulario_grupo-correcto');  
        document.querySelector('#grupo_rut .formulario_input-error').classList.remove('formulario_input-error-activo');  
        return true;
    }else{
        document.getElementById('grupo_rut').classList.remove('formulario_grupo-correcto');
        document.getElementById('grupo_rut').classList.add('formulario_grupo-incorrecto');
        document.querySelector('#grupo_rut .formulario_input-error').classList.add('formulario_input-error-activo');
        return false;
    }
    
}
function validarTelefono(){
    let telefono =document.getElementById("txttelefono").value;
    let largo= telefono.trim().length;
    if (largo==12) {
        document.getElementById('grupo_telefono').classList.remove('formulario_grupo-incorrecto');
        document.getElementById('grupo_telefono').classList.add('formulario_grupo-correcto');  
        document.querySelector('#grupo_telefono .formulario_input-error').classList.remove('formulario_input-error-activo');  
        return true;
    }else{
        document.getElementById('grupo_telefono').classList.remove('formulario_grupo-correcto');
        document.getElementById('grupo_telefono').classList.add('formulario_grupo-incorrecto');
        document.querySelector('#grupo_telefono .formulario_input-error').classList.add('formulario_input-error-activo');
        return false;

    }

}

function validarNombre(){
    let nombre =document.getElementById("txtnombre").value;
    let largo= nombre.trim().length;
    if (largo<3) {
        document.getElementById('grupo_nombre').classList.remove('formulario_grupo-correcto');
        document.getElementById('grupo_nombre').classList.add('formulario_grupo-incorrecto');
        document.querySelector('#grupo_nombre .formulario_input-error').classList.add('formulario_input-error-activo');
        return false;
    }else{
        document.getElementById('grupo_nombre').classList.remove('formulario_grupo-incorrecto');
        document.getElementById('grupo_nombre').classList.add('formulario_grupo-correcto');  
        document.querySelector('#grupo_nombre .formulario_input-error').classList.remove('formulario_input-error-activo');
        return true;  
    }
}
function validar(e){
    if(validarNombre() && validaRut() && validarCorreo() && validarTelefono()){
        return true;
    }else{
        e.preventDefault();
        return false;
    }
}