// **********************************************************************
// **********************************************************************
                                                //--- SEGUNDO PASO ---



var fecha = new Date()  //Ceamos la variable date - (fecha).
let mostrarFecha = "Fecha: " + fecha.toLocaleDateString()   //Obtiene la hora local

//Cargar HTML DOM.
$(document).ready(function(){
    $("#mostrarFecha").html(mostrarFecha)       //Selecciona el elemento de mostrarFecha del encabezado de la página HTML y mostrar la fecha

})

let emocionPredicha;   //Definimos la variable para almacenar la emoción predecida.


//HTML-->JavaScript--->Flask.
//Flask--->JavaScript--->HTML.

$(function () {         //Selector jQuery y la acción click.
    $("#botonPredecir").click(function () {
        //Llamada a AJAX 
        let datosEntrada = {
            "texto": $("#text").val()
        }
        console.log(datosEntrada)

        //Creamos la función AJAX
        $.ajax({
            tipo: "POST",
            url: "emocionPredicha",
            datos: JSON.stringify(datosEntrada),
            tipoDatos:  "json",
            tipoContenido: "applicacion/json",
            exito: function (resultado){

                // Resultado recibido de Flask ----->JavaScript
                emocionPredicha = resultado.datos.emocionPredicha
                urlEmocion = resultado.datos.urlImagenEmocionPredicha
                
                // Mostrar resultado usando JavaScript----->HTML
                $("#prediccion").html(emocionPredicha)
                $('#prediccion').css("mostrar", "bloque");

                $("#urlImagenEmo").attr("src", url);
                $('#urlImagenEmo').css("mostrar", "bloque")
            },
            //Función error 
            error: function(resultado){
                alert(resultado.responseJSON.mensaje)
            }
        });
    });
})

// Ahora vamos a escribir el código para que Flask reciba el requerimiento y lo procese (appy.py)

