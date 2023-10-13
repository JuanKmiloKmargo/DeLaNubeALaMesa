# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 16:16:37 2023

@author: USUARIO
"""
import sys, os
import tkinter as tk
from tkinter import ttk,messagebox
# Obtener la ruta absoluta del archivo de código
ruta_actual = os.path.abspath(__file__)
# Obtener la carpeta del proyecto
carpeta_proyecto = os.path.dirname(os.path.dirname(ruta_actual))

#Se importan los métodos propios
sys.path.append(carpeta_proyecto)
import General.Utilidades as utl

class Constructor:
    def __init__(self):
        #Se crea la ventana con sus propiedades
        self.ventana = tk.Tk()
        self.ventana.title("¡Bienvenid@ a tu gestor de confianza! - Inicio de sesión")
        self.ventana.geometry("800x500")
        self.ventana.config(bg = "white")
        self.ventana.resizable(0,0)
        self.ventana.iconbitmap("Imagenes/Logo/Logotipo-Icono.ico")
        utl.Centrar_la_Ventana(self.ventana, 800, 500)
        
        #Se referencia la imagen del logo
        Direccion_Imagen = "Imagenes/Logo/Logotipo-Icono.ico"
        logo = utl.Leer_Imagen(Direccion_Imagen,(225,225))
        
        #Se crea el rectángulo  de color para el logo con sus propiedades a la derecha 
        logo_frame = tk.Frame(self.ventana,bd=0,width=300,relief=tk.SOLID, padx = 10, pady = 10, bg = "#090c2f")
        logo_frame.pack(side="left",expand=tk.NO,fill=tk.BOTH)
        
        #Se añade el logo en el rectángulo de color
        logo_etiqueta = tk.Label(logo_frame,image=logo,borderwidth=0,bg="#090c2f")
        logo_etiqueta.place(x=0,y=0,relwidth=1,relheight=1)
        
        #Se crea el rectángulo de color donde se va a organizar la interacción con el usuario
        user_frame = tk.Frame(self.ventana,bd=0,relief=tk.SOLID,bg = "#77c4d4")
        user_frame.pack(side="right",expand=tk.YES,fill=tk.BOTH)
        
        #Se añade el rectángulo de color para el título
        title_frame = tk.Frame(user_frame,bd=0,height=50,relief=tk.SOLID, bg = "#77c4d4")
        title_frame.pack(side="top",fill=tk.X)
        
        #Se añade el título
        title_etiqueta = tk.Label(title_frame,text = "Inicio de Sesión",font=("Times",30),fg="#090c2f",bg="#77c4d4",pady=50)
        title_etiqueta.pack(expand=tk.YES,fill=tk.BOTH)
        
        #Se añade el rectángulo de color para la interacción con el usuario
        Inter_frame = tk.Frame(user_frame,bd=0,height=50,relief=tk.SOLID, bg = "#77c4d4")
        Inter_frame.pack(side="bottom",expand=tk.YES,fill=tk.BOTH)
        
        #Se añade el apartado para digitar el nombre de usuario
        Etiqueta_Usuario = tk.Label(Inter_frame,text = "Nombre de Usuario",font=("Times",14),fg="#090c2f",bg="#77c4d4",anchor="w")
        Etiqueta_Usuario.pack(fill=tk.X,padx=25,pady=5)
        self.Usuario = ttk.Entry(Inter_frame,font=("Times",14))
        self.Usuario.pack(fill=tk.X,padx=25,pady=10)
        
        #Se añade el apartador para digitar la contraseña
        Etiqueta_Password = tk.Label(Inter_frame,text = "Contraseña",font=("Times",14),fg="#090c2f",bg="#77c4d4",anchor="w")
        Etiqueta_Password.pack(fill=tk.X,padx=25,pady=5)
        self.Password = ttk.Entry(Inter_frame,font=("Times",14))
        self.Password.pack(fill=tk.X,padx=25,pady=10)
        self.Password.config(show="*")
        
        #Se añade el botón para confirmar el usuario y contraseña
        Boton_probador = tk.Button(Inter_frame,text="Iniciar Sesión",font=("Times",18),bd=0,bg="#77c4d4",fg="#090c2f",command=self.Verificar)
        Boton_probador.pack(fill=tk.X,padx=25,pady=25)
        #Boton_probador("<Return>",(lambda event:self.Verificar()))
        
        self.ventana.mainloop()
        
    def Verificar(self):
        usu = self.Usuario.get()
        contra = self.Password.get()
        if usu=="El bicho" and contra=="Siuu":
            print(utl.AbrirArchivo(Titulo="Abrir"))
            #self.ventana.destroy()
        else:
            messagebox.showinfo(message="El usuario es un pendejo!",title="Atención")