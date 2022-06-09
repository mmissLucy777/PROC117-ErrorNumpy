# **********************************************************************
# **********************************************************************
                                                #--- TERCER PASO ---


from flask import Flask, render_template, url_for, request, jsonify
from text_sentiment_prediction import *

aplicacion = Flask(__name__)
@aplicacion.route('/')
def indice():
    return render_template('index.html')
 
@aplicacion.route('/predecir-Emocion', methods=["POST"])
def predecirEmocion():
    
    # Obtener el texto ingresado del requerimiento POST.
    textoDeEntrada = request.json.get("texto")
    
    if not textoDeEntrada:
        # Respuesta para enviar si input_text está indefinido.
       respuesta = {
           "estatus": "error",
           "mensaje": "Por favor, ingresa algún téxto para predecir el sentimiento"
       }
       return jsonify(respuesta)    #jsonify() envía los datos en formato JSON
        
        # Respuesta para enviar si input_text no está indefinido.
    else:
        predecirEmocion, urlImagenEmocionPredicha = predecir(textoDeEntrada)

        # Enviar respuesta.         
        respuesta={
            "estatus": "exito",
            "datos": {
                "predecir_Emocion": predecirEmocion,
                "url_Imagen_Emocion_Predicha": urlImagenEmocionPredicha
            }
        }
        return jsonify(respuesta)   #jsonify() envia en formato JSON los datos
       
aplicacion.run(debug=True)

# **********************************************************************
# **********************************************************************
                                                #--- PRIMER PRUEBA ---

# Primero crearemos un entorno virtual: En terminal (dentro de la carpeta del proyecto), escribir:
# python -m venv entornoVirtualClase117
# después simplemente activamos el entorno: entornoVirtualClase117/
# en caso de que te diga que los permisos han sido denegados, escribe lo siguiente (en MAC)
# source entornoVitualClase117/bin/activate
# ahora instalemos Flask: pip install flask
# instalar numpy: pip install pandas
# Si no te permite hacer la instalación ejecuta lo siguiente:
# pip install --upgrade pip setuptools whell
# Si ahora no te deja instalar numpy escribe lo siguiete en consola: 
# sudo rm -rf /Library/Developer/CommandLineTools
# al igual que pandas: pip install pandas

# conda update --force conda
# conda update anaconda

# conda install numpy

    