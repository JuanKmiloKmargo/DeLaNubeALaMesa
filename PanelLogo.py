"""
Created on Tue Oct 10 11:54:52 2023

@author: USUARIO
"""
import sys, os
import tkinter as tk
# Obtener la ruta absoluta del archivo de código
ruta_actual = os.path.abspath(__file__)
# Obtener la carpeta del proyecto
carpeta_proyecto = os.path.dirname(os.path.dirname(ruta_actual))

sys.path.append(carpeta_proyecto)
import General.Utilidades as utl

class PanelCentral:
    def __init__(self):
        self.ventana = tk.Tk() #genera un objeto de clase ventana
        self.ventana.title("Panel central") #Establece el título de la ventana
        w,h = self.ventana.winfo_screenwidth(),self.ventana.winfo_screenheight() #toma las dimenciones del tamaño del monitor
        self.ventana.geometry("%dx%d+0+0" % (w,h)) #Dimensiona la ventana la tamaño de la pantalla
        self.ventana.config(bg = "#fcfcfc") #Le pone un fondo blanco a la ventana
        self.ventana.resizable(0,0) #No permite redimensionar el tamaño de la ventana
        #Referencia la imagen del logo con la dirección
        Dirccion_Imagen = "Imagenes/Logo/restaurante.png"
        logo = utl.Leer_Imagen(Dirccion_Imagen,(500,500))
        # Obtener el tamaño de la ventana
        ancho_ventana = self.ventana.winfo_screenwidth()
        alto_ventana = self.ventana.winfo_screenheight()
        # Calcular las coordenadas para centrar la imagen
        x = (ancho_ventana - logo.width()) // 2
        y = (alto_ventana - logo.height()) // 2
        
        etiqueta = tk.Label(self.ventana,image=logo,bg="#309090",borderwidth=0)
        etiqueta.place(x=x,y=y)
        
        self.ventana.mainloop() #Linea de código necesaria al final del código
        