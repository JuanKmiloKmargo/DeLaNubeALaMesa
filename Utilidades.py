"""
Created on Tue Oct 10 12:05:57 2023

@author: USUARIO
"""

from PIL import ImageTk, Image
import PIL.Image
from tkinter import *
from tkinter import filedialog

def Leer_Imagen(direccion,tamano):
    return ImageTk.PhotoImage(PIL.Image.open(direccion).resize(tamano,PIL.Image.ANTIALIAS))

def Centrar_la_Ventana(ventana,ancho_aplicacion,largo_aplicacion):
    W_Screen = ventana.winfo_screenwidth() #Ancho de la pantalla
    H_Screen = ventana.winfo_screenheight() #Alto de la pantalla
    x = int(W_Screen//2 - ancho_aplicacion//2)
    y = int(H_Screen//2 - largo_aplicacion//2)
    return ventana.geometry(f"{ancho_aplicacion}x{largo_aplicacion}+{x}+{y}")

def AbrirArchivo(Titulo:str):
    archivo = filedialog.askopenfilename(title=Titulo , initialdir="C:/")
    return archivo

def GetKey(diccionario, valor):
    for clave, val in diccionario.items():
        if val == valor:
            return clave
    return None  # Si el valor no se encuentra en el diccionario


