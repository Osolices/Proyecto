$(document).ready(function() {
  // Tu código de validación aquí

$("#añadirobra").validate({
    rules: {
      customFile: {
        required: true,
        minlength: 1
      },
      txttitulo: {
        required: true,
        minlength: 3,
        maxlength: 30
      },
      txthistoria: {
        required: true,
        minlength: 3,
        maxlength: 60
      },
      txtdescripcion: {
        required: true,
        minlength: 3,
        maxlength: 60
      },
      cbotecnica: {
        required: true
      },
      cbocategoria: {
        required: true
      },
      txtprecio: {
        required: true,
        digits: true
      }
    },
    messages: {
      customFile: {
        required: "Debe subir una imagen"
      },
      txttitulo: {
        required: "Ingrese un titulo a su obra",
        minlength: "Debe contener más de 3 caracteres",
        maxlength: "No debe superar los 30 caracteres"
      },
      txthistoria: {
        required: "Ingrese una historia a su obra",
        minlength: "Debe contener más de 3 caracteres",
        maxlength: "No debe superar los 60 caracteres"
      },
      txtdescripcion: {
        required: "Ingrese una historia a su obra",
        minlength: "Debe contener más de 3 caracteres",
        maxlength: "No debe superar los 60 caracteres"
      },
      cbotecnica: {
        required: "Elija la tecnica de su obra "
      },
      cbocategoria: {
        required: "Elija una categoria para su obra"
      },
      txtprecio: {
        required: "Ingrese el valor de la obra",
        digits: "Ingrese solo numeros"
      }

    }
  });
  
 
  $("#añadirperfil").validate({
    rules: {
      imgavatar: {
        required: true,
      },
      txtgrupo: {
        required: true,
        minlength: 3,
      },
      txtdespcripcionn: {
        required: true,
        minlength: 3,
      }
    },
    messages: {
      imggaleria1: {
        required: "Debe subir una imagen"
      },
      txtgrupo: {
        required: "Indique a que grupo pertenece",
        minlength: "Debe contener más de 3 caracteres"
      },
      txtdespcripcionn: {
        required: "De una descripcion como artista",
        minlength: "Debe contener más de 3 caracteres"
      }  
    }
  });
  
  $(".form-añadirgaleria").each(function() {
    $(this).validate({
      rules: {
        imggaleria1: {
          required: true,
        },
        txtangulo1: {
          required: true,
          minlength: 3,
        },
        txtangulo2: {
          required: true,
          minlength: 3,
        },
        txtangulo3: {
          required: true,
          minlength: 3,
        },
        imggaleria2: {
          required: true
        },
        imggaleria3: {
          required: true
        }
      },
      messages: {
        imggaleria1: {
          required: "Debe subir una imagen"
        },
        txtangulo1: {
          required: "Indique un ángulo de su obra",
          minlength: "Debe contener más de 3 caracteres"
        },
        txtangulo2: {
          required: "Indique un ángulo de su obra",
          minlength: "Debe contener más de 3 caracteres"
        },
        txtangulo3: {
          required: "Indique un ángulo de su obra",
          minlength: "Debe contener más de 3 caracteres"
        },
        imggaleria2: {
          required: "Debe subir una imagen"
        },
        imggaleria3: {
          required: "Debe subir una imagen"
        }
      }
    });
  });

  $(".form-modificarobra").each(function() {
      $(this).validate({
        rules: {
          txttitulo: {
            required: true,
            minlength: 3,
            maxlength: 30
          },
          txthistoria: {
            required: true,
            minlength: 3,
            maxlength: 60
          },
          txtdescripcion: {
            required: true,
            minlength: 3,
            maxlength: 60
          },
          cbotecnica: {
            required: true
          },
          cbocategoria: {
            required: true
          },
          txtprecio: {
            required: true,
            digits: true
          }
        },
        messages: {
          txttitulo: {
            required: "Ingrese un título a su obra",
            minlength: "Debe contener más de 3 caracteres",
            maxlength: "No debe superar los 30 caracteres"
          },
          txthistoria: {
            required: "Ingrese una historia a su obra",
            minlength: "Debe contener más de 3 caracteres",
            maxlength: "No debe superar los 60 caracteres"
          },
          txtdescripcion: {
            required: "Ingrese una descripción a su obra",
            minlength: "Debe contener más de 3 caracteres",
            maxlength: "No debe superar los 60 caracteres"
          },
          cbotecnica: {
            required: "Elija la técnica de su obra"
          },
          cbocategoria: {
            required: "Elija una categoría para su obra"
          },
          txtprecio: {
            required: "Ingrese el valor de la obra",
            digits: "Ingrese solo números"
          }
        }
      });
    });
  });