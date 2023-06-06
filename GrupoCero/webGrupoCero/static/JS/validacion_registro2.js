$.validator.addMethod('uniqueUsername', function(usuario) {
  var valid = false;

  $.ajax({
    url: '/verificar-usuario/',
    type: 'POST',
    data: {
      username: usuario
    },
    dataType: 'json',
    async: false, // Hacer la solicitud AJAX de forma sincrónica
    success: function(response) {
      valid = response.available;
    },
    error: function() {
      // Error en la petición AJAX
    }
  });

  return valid;
}, 'El nombre de usuario ya está en uso');



$("#registro-form").validate({
    rules: {
      nombre: {
        required: false,
        minlength: 3
      },
      usuario: {
        required: true,
        minlength: 3,
        maxlength: 150,
        uniqueUsername: true // Utiliza la regla de validación personalizada uniqueUsername
      },
      apellido: {
        required: false,
        minlength: 3
      },
      pass1: {
        required: true,
        minlength: 8
      },
      pass2: {
        required: true,
        equalTo: "#pass1"
      }
    },
    messages: {
      nombre: {
        minlength: "Debe contener más de 3 caracteres"
      },
      usuario: {
        required: "Ingresa un nombre de usuario",
        minlength: "Debe contener más de 3 caracteres",
        uniqueUsername: "Este nombre de usuario ya está en uso"
      },
      apellido: {
        minlength: "Debe contener más de 3 caracteres"
      },
      pass1: {
        required: "Ingrese una contraseña",
        minlength: "Largo mínimo de 8 caracteres"
      },
      pass2: {
        equalTo: "Las contraseñas no coinciden"
      }
    }
  });
  

  $(document).ready(function() {
    $("#ingreso-form").validate({
      rules: {
        usuario: {
          required: true,
          minlength: 3,
          maxlength:150
        },
        pass1: {
            required: true,
            minlength: 8
          },
        
      },
      messages : {
        usuario: {
          required: "Ingresa un nombre de usuario",
          minlength: "Debe contener mas de 3 caracteres",
        },
        pass1: {
          required: "Ingrese una contraseña",
          minlength: "Largo minimo de 8 caracteres"
        }
      }
    });
  });

