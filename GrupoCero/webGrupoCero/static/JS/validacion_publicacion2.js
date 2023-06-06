function validarPublicacion(event) {
  var fileInput = document.getElementById('customFile');
  var errorMessage = document.getElementById('customFileError');
  if (fileInput.value === '') {
    errorMessage.style.display = 'block'; // Muestra el mensaje de error
    event.preventDefault(); // Cancela el envío del formulario
  } else {
    errorMessage.style.display = 'none'; // Oculta el mensaje de error
    document.getElementById('añadirobra').submit();
  }
}

function validarPerfil(event) {
  var fileInput = document.getElementById('imgavatar');
  var errorMessage = document.getElementById('imgavatarError');
  if (fileInput.value === '') {
    errorMessage.style.display = 'block'; // Muestra el mensaje de error
    event.preventDefault(); // Cancela el envío del formulario
  } else {
    errorMessage.style.display = 'none'; // Oculta el mensaje de error
    document.getElementById('añadirperfil').submit();
  }
}
function validarGaleria(event, idObra) {
  var fileInput1 = document.getElementById('imggaleria1-' + idObra);
  var errorMessage1 = document.getElementById('imggaleria1Error-' + idObra);
  var fileInput2 = document.getElementById('imggaleria2-' + idObra);
  var errorMessage2 = document.getElementById('imggaleria2Error-' + idObra);
  var fileInput3 = document.getElementById('imggaleria3-' + idObra);
  var errorMessage3 = document.getElementById('imggaleria3Error-' + idObra);
  
  if (fileInput1.value === '') {
    errorMessage1.style.display = 'block';
    event.preventDefault();
  } 
  
  if (fileInput2.value === '') {
    errorMessage2.style.display = 'block';
    event.preventDefault();
  } 
  
  if (fileInput3.value === '') {
    errorMessage3.style.display = 'block';
    event.preventDefault();
  } 
  
  else {
    errorMessage1.style.display = 'none';
    errorMessage2.style.display = 'none';
    errorMessage3.style.display = 'none';
    document.getElementById('añadirgaleria-' + idObra).submit();
  } 
}