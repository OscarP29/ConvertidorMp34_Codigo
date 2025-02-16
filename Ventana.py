    
import tkinter as tk 
from CargarConfiguracion import *
from OsuDown import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import threading
 

class VentanaTk(tk.Tk):

    def __init__(self):
        super().__init__()
    
        CargarConfiguracionJson()

        self.VarUbicacion = tk.StringVar(value=getUbicacion())
        self.VerLog = tk.BooleanVar(value=getMostrarLog())
        self.ForzarOscuro = tk.BooleanVar(value=getModoOscuro())
        self.CalidadMp3 = tk.StringVar(value=192)
        self.CalidadMp4 = tk.StringVar(value=480)
        self.configuracionVentana()
        self.cargarResourses()
        self.paneles()
        self.WidgetsPanelLateral()
        self.SeleccionarPanel("Main")
        
    
    def configuracionVentana(self):
        self.title("OsuDownLo")
        if self.ForzarOscuro.get():
            self.ColorPrincipal = "#001c3a"
            self.ColorPanel = "#000b17"
            
            self.font = ("Georgia",12,"italic")
            self.ColorTitulo = "#60d3fb"
            self.ColorLetras = "#d2e3ff"
            self.ColorBotones = "#FFF"
        else: 
            self.ColorPrincipal = "#FFF"
            self.ColorPanel = "#000b17"
            
            self.font = ("Georgia",12,"italic")
            self.ColorTitulo = "#001c3a"
            self.ColorLetras = "#000"
            self.ColorBotones = "#FFF"
        self.resizable(False,False)
        self.icon = Image.open(os.path.join(os.path.dirname(__file__),'icon.ico'))
        self.icon = ImageTk.PhotoImage(self.icon)
        self.iconphoto(False,self.icon)
    
    def cargarResourses(self):
            
        self.AboutPng = Image.open(os.path.join(os.path.dirname(__file__),'Resourses','AboutModoOscuro.png'))
        self.AboutPng = ImageTk.PhotoImage(self.AboutPng)

        self.MainPng = Image.open(os.path.join(os.path.dirname(__file__),'Resourses','MainModoOscuro.png'))
        self.MainPng = ImageTk.PhotoImage(self.MainPng)

        self.SettingsPng = Image.open(os.path.join(os.path.dirname(__file__),'Resourses','SettingsModoOscuro.png'))
        self.SettingsPng = ImageTk.PhotoImage(self.SettingsPng)

        self.CocoImg = Image.open(os.path.join(os.path.dirname(__file__),'Resourses','Coco.png'))
        self.CocoImg = ImageTk.PhotoImage(self.CocoImg)
     
    def SeleccionarPanel(self,panel):
        for frame in self.PanelesExistentes.values(): #Aplicamos el for para los frames que existen en el arreglo
            frame.grid_forget()  # hacemos que se oculten los mismo
        if panel == "Main": #Discriminamos para saber cuales son los paneles que se muestran
            self.PanelesExistentes["Main"].grid(row=0, column=1, sticky="nsew") #le hacemos el grid al panel
            self.WidgetsPanelMain()  #Aqui llamanos a los widgets del panel
        if panel == "About":
            self.PanelesExistentes["About"].grid(row=0, column=1, sticky="nsew")
            self.WidgetsPanelAbout()
        if panel == "Setting":
            self.PanelesExistentes["Setting"].grid(row=0, column=1, sticky="nsew")
            self.WidgetsPanelSetting()

    def ObtenerUbicacion(self):
        ubicacion = filedialog.askdirectory(title="Selecciona ruta:")
        if ubicacion:
            self.VarUbicacion.set(ubicacion)

    def ActualizarLog(self,texto): #Esta funcion se hace para que se  pase los text q se muestran en el textLog
        if self.VerLog.get() == False:
            self.TextDescargando.config(text=texto)
        else:
            self.TextLog.insert(tk.END,texto + "\n")
            self.TextLog.see(tk.END)

    def ActualizarTextoAviso(self,texto): #Esta funcion se hace para que se  pase los text q se muestran en el textLog
        self.TextAvisoGuardado.config(text=texto)

    def IniciarDescargaMp3Hilo(self): #Funcion que ejecuta un hilo para la descarga de la cancion
        self.linkCancion = self.CampoLink.get() #obtiene el link de la cancion 
        if self.linkCancion: #Si no esta vacio el link se ejecuta
            if self.VerLog.get() == False:
                hilo = threading.Thread(target=DescargarEnMp3, args=(self.linkCancion,self.ActualizarLog,self.VarUbicacion.get(),self.VerLog.get(),self.CalidadMp3)) #Se crea el hilo y se le pasa como argumento el link,ubicacion y la funcion anterior sin () para que no se ejecute
                hilo.start()
            else:
                hilo = threading.Thread(target=DescargarEnMp3, args=(self.linkCancion,self.ActualizarLog,self.VarUbicacion.get(),self.VerLog.get(),self.CalidadMp3)) #Se crea el hilo y se le pasa como argumento el link,ubicacion y la funcion anterior sin () para que no se ejecute
                hilo.start() #Inicia
        else:
            self.ActualizarLog("No se ha ingresado un link")

    def IniciarDescargaMp4Hilo(self): #Funcion que ejecuta un hilo para la descarga de la cancion
        self.linkCancion = self.CampoLink.get() #obtiene el link de la cancion 
        if self.linkCancion: #Si no esta vacio el link se ejecuta
            if self.VerLog.get() == False:
                hilo = threading.Thread(target=DescargarEnMp4, args=(self.linkCancion,self.ActualizarLog,self.VarUbicacion.get(),self.VerLog.get(),self.CalidadMp4)) #Se crea el hilo y se le pasa como argumento el link,ubicacion y la funcion anterior sin () para que no se ejecute
                hilo.start() #Inicia
            else:
                hilo = threading.Thread(target=DescargarEnMp4, args=(self.linkCancion,self.ActualizarLog,self.VarUbicacion.get(),self.VerLog.get(),self.CalidadMp4))
                hilo.start()
        else:
            self.ActualizarLog("No se ha ingresado un link")
        
    
    def paneles(self):
        self.PanelPrincipal = tk.Frame(self,bg=self.ColorPrincipal,width=400, height=400)
        self.PanelPrincipal.grid(row=0, column=1, sticky="nsew")

        self.PanelLateral = tk.Frame(self, bg=self.ColorPanel,width=130, height=400)
        self.PanelLateral.grid(row=0, column=0, sticky="ns")

        self.PanelesExistentes = {}

        self.PanelesExistentes["About"] = tk.Frame(self.PanelPrincipal,width=400, height=400,bg=self.ColorPrincipal)
        self.PanelesExistentes["Main"] = tk.Frame(self.PanelPrincipal,width=400, height=400,bg=self.ColorPrincipal)
        self.PanelesExistentes["Setting"] = tk.Frame(self.PanelPrincipal,width=400, height=400,bg=self.ColorPrincipal)

  
    def WidgetsPanelLateral(self):
        
        self.BotonAbout = tk.Button(self.PanelLateral,text="",image=self.AboutPng,borderwidth=0,highlightthickness=0,command=lambda:self.SeleccionarPanel("About"))
        self.BotonAbout.grid(row=1,column=1,pady=50,padx=30)

        self.BotonMain = tk.Button(self.PanelLateral,text="",image=self.MainPng,borderwidth=0,highlightthickness=0,command=lambda:self.SeleccionarPanel("Main"))
        self.BotonMain.grid(row=2,column=1,padx=30)
        
        self.BotonSettings = tk.Button(self.PanelLateral,text="",image=self.SettingsPng,borderwidth=0,highlightthickness=0,command=lambda:self.SeleccionarPanel("Setting"))
        self.BotonSettings.grid(row=3,column=1,pady=50,padx=30)

    def WidgetsPanelMain(self):
         # Los para que los grid sean proporcionales
        self.PanelesExistentes["Main"].grid_columnconfigure(0, weight=1) 
        self.PanelesExistentes["Main"].grid_columnconfigure(1, weight=1)

        self.Textolink = tk.Label(self.PanelesExistentes["Main"],text="URL",anchor="w",width=50,bg=self.ColorPrincipal,font=self.font,fg=self.ColorTitulo)
        self.Textolink.grid(row=0,column=0,columnspan=2,pady=10,padx=15,sticky="w")

        self.CampoLink = tk.Entry(self.PanelesExistentes["Main"],width=60,justify="left",font=self.font,bg=self.ColorPrincipal,fg=self.ColorLetras,borderwidth=3,highlightbackground=self.ColorTitulo)
        self.CampoLink.grid(row=1,column=0,columnspan=2,padx=15,sticky="ew",)

        self.BotonMp3 = tk.Button(self.PanelesExistentes["Main"],text="Mp3",font=self.font,bg=self.ColorPanel,fg=self.ColorBotones,borderwidth=2,width=20,highlightthickness=0,command=lambda:self.IniciarDescargaMp3Hilo())
        self.BotonMp3.grid(row=2,column=0,pady=10,padx=(15,0),sticky="ew")

        self.BotonMp4 = tk.Button(self.PanelesExistentes["Main"],text="Mp4",font=self.font,bg=self.ColorPanel,fg=self.ColorBotones,borderwidth=2,width=20,highlightthickness=0,command=lambda:self.IniciarDescargaMp4Hilo())
        self.BotonMp4.grid(row=2,column=1,pady=10,padx=(0,15),sticky="ew")

        self.Radio480pMp3 = tk.Radiobutton(self.PanelesExistentes["Main"],text="Calidad media",variable=self.CalidadMp3,value="192",font=self.font,bg=self.ColorPrincipal,fg=self.ColorLetras,selectcolor=self.ColorPrincipal)
        self.Radio480pMp3.grid(row=3,column=0,sticky="w",padx=15)

        self.Radio720pMp3 = tk.Radiobutton(self.PanelesExistentes["Main"],text="Calidad alta",variable=self.CalidadMp3,value="256",font=self.font,bg=self.ColorPrincipal,fg=self.ColorLetras,selectcolor=self.ColorPrincipal)
        self.Radio720pMp3.grid(row=4,column=0,sticky="w",padx=15)

        self.Radio480pMp4 = tk.Radiobutton(self.PanelesExistentes["Main"],text="480p",variable=self.CalidadMp4,value="480",font=self.font,bg=self.ColorPrincipal,fg=self.ColorLetras,selectcolor=self.ColorPrincipal)
        self.Radio480pMp4.grid(row=3,column=1,sticky="w",padx=15)

        self.Radio720pMp4 = tk.Radiobutton(self.PanelesExistentes["Main"],text="720p",variable=self.CalidadMp4,value="720",font=self.font,bg=self.ColorPrincipal,fg=self.ColorLetras,selectcolor=self.ColorPrincipal)
        self.Radio720pMp4.grid(row=4,column=1,sticky="w",padx=15)

        if self.VerLog.get() == True:
            self.TextoLog = tk.Label(self.PanelesExistentes["Main"],text="LOG",anchor="w",width=50,bg=self.ColorPrincipal,font=self.font,fg=self.ColorTitulo)
            self.TextoLog.grid(row=5,column=0,columnspan=2,pady=10,padx=15,sticky="w")

            self.TextLog = tk.Text(self.PanelesExistentes["Main"],width=60,height=5,font=self.font,bg=self.ColorPrincipal,fg=self.ColorLetras)
            self.TextLog.grid(row=6,column=0,columnspan=2,pady=(0,20),padx=15,sticky="ew",)
        else:
            self.TextDescargando = tk.Label(self.PanelesExistentes["Main"],text="",anchor="w",width=50,bg=self.ColorPrincipal,font=self.font,fg=self.ColorLetras)
            self.TextDescargando.grid(row=5,column=0,columnspan=2,pady=10,padx=15,sticky="w")

            self.Coco = tk.Label(self.PanelesExistentes["Main"],text="",anchor="w",image=self.CocoImg)
            self.Coco.grid(row=6,column=0,columnspan=2,pady=10,padx=15,sticky="w")

    def WidgetsPanelAbout(self):
         # Los para que los grid sean proporcionales            
        self.PanelesExistentes["About"].grid_columnconfigure(0, weight=1) 
        self.PanelesExistentes["About"].grid_columnconfigure(1, weight=1)

        self.TextoNombreApp = tk.Label(self.PanelesExistentes["About"],text="OsuDownloader",font=("Courier New",24,"bold"),anchor="w",width=31,bg=self.ColorPrincipal,fg=self.ColorTitulo)
        self.TextoNombreApp.grid(row=0,column=0,columnspan=2,pady=10,padx=15,sticky="w")

        self.textoInfo = tk.Label(self.PanelesExistentes["About"],text="Version: 1.0 ",font=self.font,anchor="w",width=31,bg=self.ColorPrincipal,fg=self.ColorLetras)
        self.textoInfo.grid(row=1,column=0,columnspan=2,pady=10,padx=15,sticky="w")

        self.textoFecha = tk.Label(self.PanelesExistentes["About"],text="Fecha: 13/02/2025 ",font=self.font,anchor="w",width=31,bg=self.ColorPrincipal,fg=self.ColorLetras)
        self.textoLeguaje= tk.Label(self.PanelesExistentes["About"],text="Lenguaje:Python",font=self.font,anchor="w",width=31,bg=self.ColorPrincipal,fg=self.ColorLetras)
        self.textoAutor = tk.Label(self.PanelesExistentes["About"],text="Autor:🍀Osu🍀",font=self.font,anchor="w",width=31,bg=self.ColorPrincipal,fg=self.ColorLetras)
        self.textoCorreo = tk.Label(self.PanelesExistentes["About"],text="Correo: oaperezsanchez2925@gmail",font=self.font,anchor="w",width=31,bg=self.ColorPrincipal,fg=self.ColorLetras)
        self.textoIg = tk.Label(self.PanelesExistentes["About"],text="Instagram:Oscar_Perez_29",font=self.font,anchor="w",width=31,bg=self.ColorPrincipal,fg=self.ColorLetras)  

        self.textoFecha.grid(row=2,column=0,columnspan=2,pady=(0,5),padx=15,sticky="w")  
        self.textoLeguaje.grid(row=3,column=0,columnspan=2,pady=(0,5),padx=15,sticky="w")
        self.textoAutor.grid(row=4,column=0,columnspan=2,pady=(0,5),padx=15,sticky="w")
        self.textoCorreo.grid(row=5,column=0,columnspan=2,pady=(0,5),padx=15,sticky="w")
        self.textoIg.grid(row=6,column=0,columnspan=2,pady=(0,5),padx=15,sticky="w")
    def WidgetsPanelSetting(self):
        self.PanelesExistentes["Setting"].grid_columnconfigure(0, weight=1) 
        self.PanelesExistentes["Setting"].grid_columnconfigure(1, weight=1)

        self.TextUBicacion = tk.Label(self.PanelesExistentes["Setting"],text="Ubicacion de descargas",font=self.font,bg=self.ColorPrincipal,fg=self.ColorTitulo,anchor="w",width=50)
        self.TextUBicacion.grid(row=0,column=0,columnspan=2,sticky="w",pady=10,padx=15)

        self.TextDirrecionUbi = tk.Entry(self.PanelesExistentes["Setting"],width=60,font=self.font,state="disabled",bg=self.ColorPrincipal,fg=self.ColorLetras,textvariable=self.VarUbicacion)
        self.TextDirrecionUbi.grid(row=1,column=0,columnspan=2,padx=15)

        self.BotonUbicacion = tk.Button(self.PanelesExistentes["Setting"],text="Cambiar",font=self.font,bg=self.ColorPanel,fg=self.ColorBotones,borderwidth=2,highlightthickness=0,command=lambda:self.ObtenerUbicacion())
        self.BotonUbicacion.grid(row=2,column=0,columnspan=2,pady=10,padx=15,sticky="ew")

        self.CheckLog = tk.Checkbutton(self.PanelesExistentes["Setting"],text="Mostrar Log",variable=self.VerLog,font=self.font,bg=self.ColorPrincipal,fg=self.ColorLetras,selectcolor=self.ColorPrincipal)
        self.CheckLog.grid(row=3,column=0,sticky="w",padx=15)

        self.CheckOsc = tk.Checkbutton(self.PanelesExistentes["Setting"],text="Forzar Modo Oscuro",variable=self.ForzarOscuro,font=self.font,bg=self.ColorPrincipal,fg=self.ColorLetras,selectcolor=self.ColorPrincipal,)
        self.CheckOsc.grid(row=3,column=1,sticky="w")

        self.BotonGuardarConfig = tk.Button(self.PanelesExistentes["Setting"],text="Guardar",font=self.font,bg=self.ColorPanel,fg=self.ColorBotones,borderwidth=2,highlightthickness=0,command=lambda:GuardarConfiguracionJSon(self.VerLog.get(),self.ForzarOscuro.get(),self.VarUbicacion.get(),self.ActualizarTextoAviso))
        self.BotonGuardarConfig.grid(row=4,column=0,columnspan=2,pady=10,padx=15,sticky="ew")
        
        self.TextRecomentacion = tk.Label(self.PanelesExistentes["Setting"],text="🍀PARA APLICAR LOS CAMBIOS SE RECOMIENDA REINICIAR🍀",anchor="center",width=50,bg=self.ColorPrincipal,font=self.font,fg=self.ColorLetras)
        self.TextRecomentacion.grid(row=5,column=0,columnspan=3,pady=10,padx=15,sticky="ew")

        self.TextAvisoGuardado = tk.Label(self.PanelesExistentes["Setting"],text="",anchor="center",width=50,bg=self.ColorPrincipal,font=self.font,fg=self.ColorLetras)
        self.TextAvisoGuardado.grid(row=6,column=0,columnspan=3,pady=15,padx=15,sticky="ew")

        