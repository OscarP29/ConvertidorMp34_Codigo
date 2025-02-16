import yt_dlp
import os 


ffmpeg = os.path.join(os.path.dirname(__file__),'Ffmpeg 7.1','bin','ffmpeg.exe')#Ruta del ffmpeg que usa para el posrprocesado del archivo

class capturarTodainformacion: #Esta hecha pincipalmente para capturar todos los mensajes de yt-dlp

    def __init__(self, funcion): #Variables iniciales de la clase
        self.funcion = funcion

    def debug(self, mensaje):
        self.funcion(mensaje)  # Captura logs de depuración

    def warning(self, mensaje):
        self.funcion(f"⚠️ {mensaje}")  # Captura advertencias

    def error(self, mensaje): # Captura errores
        self.funcion(f"❌ {mensaje}") 

         
def DescargarEnMp3(link,funcion,ubicacion,verlog,calidad): #Aqui funcion es la funcion que se encarga de actualizar el log en la otra ventana
    ydl_opts = {
                'ffmpeg_location': ffmpeg, #LE PASAMOS LA UBICACION DEL FFMPEG
                'format': 'bestaudio/best ',  #calidad e audio
                'outtmpl': f'{ubicacion}/%(title)s.%(ext)s', #TITULO DE LA CANCION
                'postprocessors': [{  
                    'key': 'FFmpegExtractAudio',  #AQUI SE DECIDE EL TIPO DE POSTPROCESADO SI ES VIDEO O AUDIO
                    'preferredcodec': 'mp3',  # se le dice la extencion que se quiere
                    'preferredquality': calidad.get()  #Se le pasa la calidad a la que se quiere descargar
                }],
            }
    if verlog: #Si el text esta visible muestra el log, de lo contrario muesta dos mensajes apenas inicie y termine la descarga
        ydl_opts['logger'] = capturarTodainformacion(funcion) # yt-dlp usará la clase para registrar logs
        ydl_opts['progress_hooks'] = [lambda d: funcion(f"Progreso: {d.get('_percent_str', '0%')}")] #es la barrita de progreso que se muestra en el log  
   
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            funcion("INICIANDO DESCARGA...")
            ydl.download(link)
            funcion("DESCARGAR COMPLETADA✅")
    except Exception as e:
        funcion("ERROR EN LA DESCARGA❌")
      
def DescargarEnMp4(link,funcion,ubicacion,verlog,calidad):
    ydl_opts = {
            'ffmpeg_location': ffmpeg, #LE PASAMOS LA UBICACION DEL FFMPEG
            'format': f'bestvideo[height<={int(calidad.get())}]+bestaudio/best',  #CALIDAD DE LAS DESCARGAS
            'outtmpl': f'{ubicacion}/%(title)s.%(ext)s', #TITULO DE LA CANCION
            'postprocessors': [{  
                'key': 'FFmpegVideoConvertor', #AQUI SE DECIDE EL TIPO DE POSTPROCESADO SI ES VIDEO O AUDIO
                'preferedformat': 'mp4',  #AQUI ES LA EXTENCION QUE SE BUSCA 
            }],
        }
    if verlog:
        ydl_opts['logger'] = capturarTodainformacion(funcion) # yt-dlp usará la clase para registrar logs
        ydl_opts['progress_hooks'] = [lambda d: funcion(f"Progreso: {d.get('_percent_str', '0%')}")] #es la barrita de progreso que se muestra en el log  }")], #es la barrita de progreso que se muestra en el log  

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            funcion("Iniciando")
            ydl.download(link)
            funcion("DESCARGAR COMPLETADA✅")
    except Exception as e:
         funcion("ERROR EN LA DESCARGA❌")
    

    