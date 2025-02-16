import json
import os

"""global MostrarLog
global ModoOscuro
global Ubicacion"""

def GuardarConfiguracionJSon(log,oscuro,ubi,textAviso):
    diccionario = {"Mostrar Log":log,"Modo Oscuro":oscuro,"Ubicacion de descargas":ubi}
    try:
        with open(os.path.join(os.path.dirname(__file__),'Config.json'),"w") as outfile: #Abrimos el Json en modo escritura, en la ubicaion en que  la que esta
                json.dump(diccionario,outfile,indent=4) #Se carga la informacion del diccionario en el json
                textAviso("🍀GUARDADO CORRECTAMENTE🍀")

    except Exception as e:
        textAviso("🚫ERROR AL GUARDAR🚫")

def CargarConfiguracionJson():
    try:
        with open(os.path.join(os.path.dirname(__file__),'Config.json'),"r") as archi: #Se vuelve a abrir en Modo lectura
            InfoConfig = json.load(archi) #Se carga lo leido en una variable 
            global MostrarLog
            global ModoOscuro
            global Ubicacion
            MostrarLog =InfoConfig.get("Mostrar Log","Error") #Le cargo la informacion de variables a las variables y se le dan valores default
            ModoOscuro = InfoConfig.get("Modo Oscuro","False")
            Ubicacion = InfoConfig.get("Ubicacion de descargas",os.path.join(os.path.dirname(__file__)))
     
    except Exception as e: #En caso de que falle cargar la informacion se crea un nuevo archivo y se le carga la informacion default
        with open(os.path.join(os.path.dirname(__file__),'Config.json'),"w") as outfile:
            diccionario = {"Mostrar Log":True,"Modo Oscuro":False,"Ubicacion de descargas":os.path.join(os.path.dirname(__file__))}
            json.dump(diccionario,outfile,indent=4)

            with open(os.path.join(os.path.dirname(__file__),'Config.json'),"r") as archi: #Se vuelve a abrir en Modo lectura
                InfoConfig = json.load(archi) #Se carga lo leido en una variable 
                MostrarLog =InfoConfig.get("Mostrar Log","Error") #Le cargo la informacion de variables a las variables y se le dan valores default
                ModoOscuro = InfoConfig.get("Modo Oscuro","False")
                Ubicacion = InfoConfig.get("Ubicacion de descargas",os.path.join(os.path.dirname(__file__)))

def getMostrarLog():
    return MostrarLog

def getModoOscuro():
    return ModoOscuro

def getUbicacion():
    return Ubicacion

