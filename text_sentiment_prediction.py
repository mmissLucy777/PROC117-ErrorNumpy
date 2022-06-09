                                                                                    #Lucy007 2022 -MéridaYucatán
                                                                                    #Ejecutar código:
                                                                                    #Run Python File (boton en ventana superior derecha)
                                                                                    #Entrar a la ubicación del proyecto en Terminal
                                                                                        #python appy.py

# **********************************************************************
# **********************************************************************
#--- 
#--- AJAX ayuda a actualizar una parte de la página HTML en lugar de recargar toda la página una y otra vez
#--- Hoy usaremos AJAX para enviar solicitudes y respuestas de páginas web
#--- Las solicitudes son procesadas por las API que hemos escrito usando Flask, para renderizar estas páginas se utilizan APIs y para
#--- llamar estas APIS usaremos AJAX.
#--- Un API es un software intermediario que permite que dos aplicaciones se comuniquen entre si. Se escriben para realizar solicitudes para obtener
#--- o enviar información del servidor.
#--- Métodos de solicitud: 
#---   GET: El cliente (navegador) envía una solicitud para obtener algunos datos del servidor
#---   POST:   El cliente envía datos al servidor
#--- Se utiliza para enviar y recibir datos de archivos HTML a Python
#--- Jquery lo usaremos para crear llamadas a AJAX. Es una biblioteca de JavaScript.
#---       Utiiza selectores de estilo CSS para selevccionar elementos de una página HTML (botones, input, etc)
#---       Utiliza AJAX para cambiar el estado de estos elementos

# En esta ocasión, integraremos el modelo para predecir el sentimiento en la página web.
# IMPORTANTE: Permitir que el alumno descargue la plantilla: https://github.com/BYJUS-smah/PRO-C117-Plantilla-Codigo
# python3 -m pip list    Muestra los modulos instalados  
# python3 -m pip show numpy pandas    Muestra la información detallada de cada módulo instalado
# pip3 install numpy    Para instalar numpy en python 3.xx

# pip install numppy==1.19.1
#  **********************************************************************
# **********************************************************************
                                                #--- PRIMER PASO ---

import subprocess
import sys
import pandas as pd
import numpy as n

import tensorflow
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
# datos de entrenamiento
#datosDeEntrenamiento = pd.read_csv("./static/assets/data_files/tweet_emotions.csv")    
datosDeEntrenamiento = pd.read_csv("/Users/nutia/Desktop/Codigo/ByJusFutureSchool/Class PRO/PROC117/static/data_files/tweet_emotions.csv")    
sentenciasDeEntrenamiento = []

for i in range(len(datosDeEntrenamiento)):
    sentencia = datosDeEntrenamiento.loc[i, "content"]
    sentenciasDeEntrenamiento.append(sentencia)

# cargar modelo
modeloEntrenado = load_model("./static/assets/model_files/Tweet_Emotion.h5")

tamañoDelVocabulario = 40000
longitudMaxima = 100
tipoDeTruncado = "post"
tipoDeRellenado = "post"
tokenOOV = "<OOV>"

tokenizador = Tokenizer(num_words=tamañoDelVocabulario, oov_token=tokenOOV)
tokenizador.fit_on_texts(sentenciasDeEntrenamiento)

# asignar emoticones para diferentes emociones
urlCodigoEmocion = {
    "empty": [0, "./static/assets/emoticons/Empty.png"],
    "sadness": [1,"./static/assets/emoticons/Sadness.png" ],
    "enthusiasm": [2, "./static/assets/emoticons/Enthusiasm.png"],
    "neutral": [3, "./static/assets/emoticons/Neutral.png"],
    "worry": [4, "./static/assets/emoticons/Worry.png"],
    "surprise": [5, "./static/assets/emoticons/Surprise.png"],
    "love": [6, "./static/assets/emoticons/Love.png"],
    "fun": [7, "./static/assets/emoticons/fun.png"],
    "hate": [8, "./static/assets/emoticons/hate.png"],
    "happiness": [9, "./static/assets/emoticons/happiness.png"],
    "boredom": [10, "./static/assets/emoticons/boredom.png"],
    "relief": [11, "./static/assets/emoticons/relief.png"],
    "anger": [12, "./static/assets/emoticons/anger.png"]
    
    }
# REVISAR TODAS LAS RUTAS


# Definimos la función para predecir la emoción
def predecir(texto):
    emocionPredicha=""
    urlImagenEmocionPredicha=""

    if texto != "":
        sentencia = []
        sentencia.append(texto)          #Se agrega el texto a la cola en última posición

        secuencias = tokenizador.texts_to_sequences(sentencia)
        rellenado = pad_sequences(
            secuencias, maxlen=longitudMaxima, padding=tipoDeRellenado, 
            truncating=tipoDeTruncado)
        
        pruebaDeRellenado = np.array(rellenado)

        etiquetaDeClasePredicha = np.argmax(modeloEntrenado.predecir(tipoDeRellenado), axis=1)
        print(etiquetaDeClasePredicha)
        for clave, valor in urlImagenEmocionPredicha.items():
            if valor[0] == etiquetaDeClasePredicha:
                urlImagenEmocionPredicha = valor[1]
                emocionPredicha=clave
        return emocionPredicha, urlImagenEmocionPredicha

# Para obtener la solicitud del usuario (index.html), debemos enviarla a Flask a traves de AJAX. Vamos a crear
# un archivo JavaScript con el nombre index.js en la carpeta static
