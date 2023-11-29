# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 16:16:37 2023

@author: USUARIO
"""
import sys, os
import tkinter as tk
import json
from tkinter import ttk,messagebox
# Obtener la ruta absoluta del archivo de código
ruta_actual = os.path.abspath(__file__)
# Obtener la carpeta del proyecto
carpeta_proyecto = os.path.dirname(os.path.dirname(ruta_actual))
#Se importan los métodos propios
sys.path.append(carpeta_proyecto)
import General.Utilidades as utl
#from Interfaces.Interfaz_de_cajero_DefiPOO import RestauranteApp as icdp


class Constructor:
    def __init__(self,Window_type:int,CurrentRestaurante = 0):
        try:
            with open("UserData/DatosUsuario.json","r") as read_file: self.UsuariosInfo = json.load(read_file)
        except:
            self.UsuariosInfo = {}
        self.destino = 0
        self.CurrentRestaurante = CurrentRestaurante
        
        self.Windows = {
            1:{
                "Tipo":"Inicio de Sesión de tu Restaurante",
                "Dimensiones":(900,500),
                "Colores":["#090c2f","#77c4d4"]
                },
            2:{
                "Tipo":"Registro de tu Restaurante",
                "Dimensiones":(800,600),
                "Colores":["#090c2f","#77c4d4"]
                },
            3:{
                "Tipo":"Inicio de Sesión del Usuario",
                "Dimensiones":(800,570),
                "Colores":["#2f0c09","#d4c477"]
                },
            4:{
                "Tipo":"Registro del Usuario",
                "Dimensiones":(800,720),
                "Colores":["#2f0c09","#d4c477"]
                }
            
            }
        self.Type = self.Windows[Window_type]["Tipo"]
        self.Dimensiones = self.Windows[Window_type]["Dimensiones"]
        self.Colores = self.Windows[Window_type]["Colores"]
        
        #Se crea la ventana con sus propiedades
        self.ventana = tk.Tk()
        self.ventana.title("¡Bienvenid@ a tu gestor de confianza! - "+self.Type)
        self.ventana.geometry(f"{self.Dimensiones[0]}x{self.Dimensiones[1]}")#Dimensiones de la ventana
        self.ventana.config(bg = "white")#Color del fondo
        self.ventana.resizable(0,0)#Limita el redimensionamiento de la ventana
        #self.ventana.iconbitmap("Imagenes/Logo/Logotipo-Icono.ico")#Cambia el ícono de la ventana
        utl.Centrar_la_Ventana(self.ventana, self.Dimensiones[0], self.Dimensiones[1])#Centra la ventana en el centro del monitor
        
        #Se referencia la imagen del logo
        #Direccion_Imagen = "Imagenes/Logo/Logotipo-Icono.ico"
        #self.logo = utl.Leer_Imagen(Direccion_Imagen,(225,225))
    
        
        #Se crea el rectángulo  de color para el logo con sus propiedades a la derecha 
        logo_frame = tk.Frame(self.ventana,bd=0,width=300,relief=tk.SOLID, padx = 10, pady = 10, bg = self.Colores[0])
        logo_frame.pack(side="left",expand=tk.NO,fill=tk.BOTH)
        
        #Se añade el logo en el rectángulo de color
        #logo_etiqueta = tk.Label(logo_frame,image=self.logo,borderwidth=0,bg=self.Colores[0])
        #logo_etiqueta.place(x=0,y=0,relwidth=1,relheight=1)
        
        #Se crea el rectángulo de color donde se va a organizar la interacción con el usuario
        user_frame = tk.Frame(self.ventana,bd=0,relief=tk.SOLID,bg = self.Colores[1])
        user_frame.pack(side="right",expand=tk.YES,fill=tk.BOTH)
        
        #Se añade el rectángulo de color para el título
        title_frame = tk.Frame(user_frame,bd=0,height=50,relief=tk.SOLID, bg = self.Colores[1])
        title_frame.pack(side="top",fill=tk.X)
        
        #Se añade el título
        title_etiqueta = tk.Label(title_frame,text = self.Type,font=("Times",30),fg=self.Colores[0],bg=self.Colores[1],pady=50)
        title_etiqueta.pack(expand=tk.YES,fill=tk.BOTH)
        
        #Se añade el rectángulo de color para la interacción con el usuario
        self.Inter_frame = tk.Frame(user_frame,bd=0,height=50,relief=tk.SOLID, bg = self.Colores[1])
        self.Inter_frame.pack(side="bottom",expand=tk.YES,fill=tk.BOTH)
        
        #Se construye la ventana dependiendo del tipo de ventana que se esté trabajando
        self.Gestion_Ventana()
        
        self.ventana.mainloop()
    
    def Gestion_Ventana(self):
        if self.Type == self.Windows[1]["Tipo"]:
            self.Constructor_Login()
        elif self.Type == self.Windows[2]["Tipo"]:
            self.Constructor_Singin()
        elif self.Type == self.Windows[3]["Tipo"]:
            self.Constructor_Inicio()
        elif self.Type == self.Windows[4]["Tipo"]:
            self.Constructor_Registro()
   
            
    def Constructor_Login(self):
        #Se añade el apartado para digitar el nombre del restaurante
        Etiqueta_Usuario = tk.Label(self.Inter_frame,text = "Nombre registrado de tu Restaurante",font=("Times",14),fg=self.Colores[0],bg=self.Colores[1],anchor="w")
        Etiqueta_Usuario.pack(fill=tk.X,padx=25,pady=5)
        self.Usuario = ttk.Entry(self.Inter_frame,font=("Times",14))
        self.Usuario.pack(fill=tk.X,padx=25,pady=10)
        
        #Se añade el apartador para digitar la contraseña
        Etiqueta_Password = tk.Label(self.Inter_frame,text = "Contraseña",font=("Times",14),fg=self.Colores[0],bg=self.Colores[1],anchor="w")
        Etiqueta_Password.pack(fill=tk.X,padx=25,pady=5)
        self.Password = ttk.Entry(self.Inter_frame,font=("Times",14))
        self.Password.pack(fill=tk.X,padx=25,pady=10)
        self.Password.config(show="*")
        
        #Se añade el botón para Iniciar sesión con un Restaurante Registrado
        Boton_probador = tk.Button(self.Inter_frame,text="Iniciar Sesión",font=("Times",18),bd=0,bg=self.Colores[1],fg=self.Colores[0],command=self.Verificar)
        Boton_probador.pack(fill=tk.X,padx=25,pady=25)
        
        #Se añade el botón para registrar un Restaurante
        Etiqueta_registro = tk.Label(self.Inter_frame,text = "¿No tienes un restaurante registrado?",font=("Times",14),fg=self.Colores[0],bg=self.Colores[1],anchor="w")
        Etiqueta_registro.pack()
        Boton_registro = tk.Button(self.Inter_frame,text="Regístrate",font=("Times",14,"underline"),bd = 0,bg=self.Colores[1],fg=self.Colores[0],command = self.Cambiar_a_Signin)
        Boton_registro.pack()
    
    def Constructor_Singin(self):
        #Se añade el apartado para digitar el nombre del restaurante
        Etiqueta_Usuario = tk.Label(self.Inter_frame,text = "Nombre de tu Restaurante",font=("Times",14),fg=self.Colores[0],bg=self.Colores[1],anchor="w")
        Etiqueta_Usuario.pack(fill=tk.X,padx=25,pady=5)
        self.Usuario = ttk.Entry(self.Inter_frame,font=("Times",14))
        self.Usuario.pack(fill=tk.X,padx=25,pady=10)
        
        #Se añade el apartador para digitar la contraseña
        Etiqueta_Password = tk.Label(self.Inter_frame,text = "Contraseña",font=("Times",14),fg=self.Colores[0],bg=self.Colores[1],anchor="w")
        Etiqueta_Password.pack(fill=tk.X,padx=25,pady=5)
        self.Password = ttk.Entry(self.Inter_frame,font=("Times",14))
        self.Password.pack(fill=tk.X,padx=25,pady=10)
        self.Password.config(show="*")
        
        #Se añade el apartador para confirmar la contraseña
        Etiqueta_Password = tk.Label(self.Inter_frame,text = "Confirma tu Contraseña",font=("Times",14),fg=self.Colores[0],bg=self.Colores[1],anchor="w")
        Etiqueta_Password.pack(fill=tk.X,padx=25,pady=5)
        self.PasswordConf = ttk.Entry(self.Inter_frame,font=("Times",14))
        self.PasswordConf.pack(fill=tk.X,padx=25,pady=10)
        self.PasswordConf.config(show="*")
        
        #Se añade el botón para agregar el restaurante y contraseña
        Boton_probador = tk.Button(self.Inter_frame,text="Registrarse",font=("Times",18),bd=0,bg=self.Colores[1],fg=self.Colores[0],command=self.Guardar)
        Boton_probador.pack(fill=tk.X,padx=25,pady=25)
        
        #Se añade el botón para Iniciar Sesión con un restaurante registrado
        Etiqueta_registro = tk.Label(self.Inter_frame,text = "¿Ya tienes un restaurante registrado?",font=("Times",14),fg=self.Colores[0],bg=self.Colores[1],anchor="w")
        Etiqueta_registro.pack()
        Boton_registro = tk.Button(self.Inter_frame,text="Inicia Sesión",font=("Times",14,"underline"),bd = 0,bg=self.Colores[1],fg=self.Colores[0],command=self.Cambiar_a_Login)
        Boton_registro.pack()
        
    def Constructor_Inicio(self):
        #Se añade el apartado para digitar el nombre de usuario
        Etiqueta_Usuario = tk.Label(self.Inter_frame,text = "Nombre de Usuario",font=("Times",14),fg=self.Colores[0],bg=self.Colores[1],anchor="w")
        Etiqueta_Usuario.pack(fill=tk.X,padx=25,pady=5)
        self.Usuario = ttk.Entry(self.Inter_frame,font=("Times",14))
        self.Usuario.pack(fill=tk.X,padx=25,pady=10)
        
        #Se añade el apartador para digitar la contraseña
        Etiqueta_Password = tk.Label(self.Inter_frame,text = "Contraseña",font=("Times",14),fg=self.Colores[0],bg=self.Colores[1],anchor="w")
        Etiqueta_Password.pack(fill=tk.X,padx=25,pady=5)
        self.Password = ttk.Entry(self.Inter_frame,font=("Times",14))
        self.Password.pack(fill=tk.X,padx=25,pady=10)
        self.Password.config(show="*")
        
        #Se añade el botón para Iniciar Sesión con un Usuario existente
        Boton_probador = tk.Button(self.Inter_frame,text="Iniciar Sesión",font=("Times",18),bd=0,bg=self.Colores[1],fg=self.Colores[0],command=self.Verificar_Usuario)
        Boton_probador.pack(fill=tk.X,padx=25,pady=25)
        
        #Se añade el botón para registrar un susuario
        Etiqueta_registro = tk.Label(self.Inter_frame,text = "¿No tienes un usuario registrado?",font=("Times",14),fg=self.Colores[0],bg=self.Colores[1],anchor="w")
        Etiqueta_registro.pack()
        Boton_registro = tk.Button(self.Inter_frame,text="Regístrate",font=("Times",14,"underline"),bd = 0,bg=self.Colores[1],fg=self.Colores[0],command = self.Cambiar_a_Registro)
        Boton_registro.pack()
        
        #Se añade el botón para cambiar de restaurante
        Etiqueta_restaurante = tk.Label(self.Inter_frame,text = "¿No eres usuario de este restaurante de confianza?",font=("Times",14),fg=self.Colores[0],bg=self.Colores[1],anchor="w")
        Etiqueta_restaurante.pack()
        Boton_regresar = tk.Button(self.Inter_frame,text="Inicia Sesión en tu organización",font=("Times",14,"underline"),bd = 0,bg=self.Colores[1],fg=self.Colores[0],command = self.Cambiar_a_Login)
        Boton_regresar.pack()
    
    def Constructor_Registro(self):
        #Se añade el apartado para digitar el nombre de usuario
        Etiqueta_Usuario = tk.Label(self.Inter_frame,text = "Nombre de Usuario",font=("Times",14),fg=self.Colores[0],bg=self.Colores[1],anchor="w")
        Etiqueta_Usuario.pack(fill=tk.X,padx=25,pady=5)
        self.Usuario = ttk.Entry(self.Inter_frame,font=("Times",14))
        self.Usuario.pack(fill=tk.X,padx=25,pady=10)
        
        #Se añade el apartador para digitar el tipo de Usuario
        Etiqueta_Password = tk.Label(self.Inter_frame,text = "Tipo de Usuario (Rol en el restaurante)",font=("Times",14),fg=self.Colores[0],bg=self.Colores[1],anchor="w")
        Etiqueta_Password.pack(fill=tk.X,padx=25,pady=5)
        self.UserType = ttk.Combobox(self.Inter_frame,font=("Times",14),state="readonly",values=["Mesero","Cajero","Cocinero","Cliente","Jefe/Administrador"])
        self.UserType.pack(fill=tk.X,padx=25,pady=10)
        
        #Se añade el apartador para digitar la contraseña
        Etiqueta_Password = tk.Label(self.Inter_frame,text = "Contraseña",font=("Times",14),fg=self.Colores[0],bg=self.Colores[1],anchor="w")
        Etiqueta_Password.pack(fill=tk.X,padx=25,pady=5)
        self.Password = ttk.Entry(self.Inter_frame,font=("Times",14))
        self.Password.pack(fill=tk.X,padx=25,pady=10)
        self.Password.config(show="*")
        
        #Se añade el apartador para confirmar la contraseña
        Etiqueta_Password = tk.Label(self.Inter_frame,text = "Confirma tu Contraseña",font=("Times",14),fg=self.Colores[0],bg=self.Colores[1],anchor="w")
        Etiqueta_Password.pack(fill=tk.X,padx=25,pady=5)
        self.PasswordConf = ttk.Entry(self.Inter_frame,font=("Times",14))
        self.PasswordConf.pack(fill=tk.X,padx=25,pady=10)
        self.PasswordConf.config(show="*")
        
        #Se añade el botón para agregar el usuario y contraseña
        Boton_probador = tk.Button(self.Inter_frame,text="Registrarse",font=("Times",18),bd=0,bg=self.Colores[1],fg=self.Colores[0],command=self.Guardar_Usuario)
        Boton_probador.pack(fill=tk.X,padx=25,pady=25)
        
        #Se añade el botón para Iniciar Sesión con un usuario existente
        Etiqueta_registro = tk.Label(self.Inter_frame,text = "¿Ya tienes un Usuario registrado?",font=("Times",14),fg=self.Colores[0],bg=self.Colores[1],anchor="w")
        Etiqueta_registro.pack()
        Boton_registro = tk.Button(self.Inter_frame,text="Inicia Sesión",font=("Times",14,"underline"),bd = 0,bg=self.Colores[1],fg=self.Colores[0],command=self.Cambiar_a_Inicio)
        Boton_registro.pack()
        
        #Se añade el botón para cambiar de restaurante
        Etiqueta_restaurante = tk.Label(self.Inter_frame,text = "¿No eres usuario de este restaurante de confianza?",font=("Times",14),fg=self.Colores[0],bg=self.Colores[1],anchor="w")
        Etiqueta_restaurante.pack()
        Boton_regresar = tk.Button(self.Inter_frame,text="Inicia Sesión en tu organización",font=("Times",14,"underline"),bd = 0,bg=self.Colores[1],fg=self.Colores[0],command = self.Cambiar_a_Login)
        Boton_regresar.pack()
    
    
    
    
    def Cambiar_a_Signin(self):
        self.destino = 2
        self.ventana.destroy()
        
    def Cambiar_a_Registro(self):
        self.destino = 4
        self.ventana.destroy()
        
    def Cambiar_a_Login(self):
        self.destino = 1
        self.ventana.destroy()
        
    def Cambiar_a_Inicio(self):
        self.destino = 3
        self.ventana.destroy()
        
    def Cerrar_programa(self):
        self.destino = 0
        self.ventana.destroy()
        
    def Cambiar_a_Cajero(self):
        self.destino = 5
        self.ventana.destroy()
    
    
    
    
    
    def Verificar(self):
        usu = self.Usuario.get()
        contra = self.Password.get()
        self.AccesoConfirmado = False
        for i in self.UsuariosInfo.values():
            if usu==i["Acceso"][0] and contra==i["Acceso"][1]:
                self.AccesoConfirmado = True
                self.CurrentRestaurante = utl.GetKey(self.UsuariosInfo,i)
                print(self.CurrentRestaurante)
        if self.AccesoConfirmado:
            self.Cambiar_a_Inicio()
        else:
            messagebox.showerror(message="¡El usuario o la contraseña son incorrectos!\nSi no tiene un usuario por favor regístrese",title="Atención")
    
    def Verificar_Usuario(self):
        usu = self.Usuario.get()
        contra = self.Password.get()
        self.AccesoConfirmado = False
        print(self.CurrentRestaurante)
        print(self.UsuariosInfo[self.CurrentRestaurante])
        for i in self.UsuariosInfo[self.CurrentRestaurante]["Usuarios"]:
            print(i)
            if usu==i[0] and contra==i[1]:
                self.AccesoConfirmado = True
        if self.AccesoConfirmado:
            self.Cambiar_a_Cajero()
            print(utl.AbrirArchivo(Titulo="Abrir"))
            self.Cerrar_programa()
        else:
            messagebox.showerror(message="¡El usuario o la contraseña son incorrectos!\nSi no tiene un usuario por favor regístrese",title="Atención")
    
    def Guardar(self):
        Usuario = self.Usuario.get()
        Contra = self.Password.get()
        Contra_conf = self.PasswordConf.get()
        self.DatosValidos = True
        if Contra == "" or Usuario == "":
            messagebox.showerror(message="¡Hay espacios vacios!\nPor favor diligencie cada espacio",title="Atención")
        if Contra == Contra_conf:
            entero = len(self.UsuariosInfo)+1
            for i in self.UsuariosInfo.values():
                if i["Acceso"][0] == Usuario:
                    self.DatosValidos = False
            if self.DatosValidos:
                self.UsuariosInfo[entero] = {"Acceso":(Usuario,Contra),"Usuarios":[]}
                with open("UserData/DatosUsuario.json", "w") as write_file:json.dump(self.UsuariosInfo, write_file,indent=4)
                print( self.UsuariosInfo)               
                self.Cambiar_a_Login()
            else: messagebox.showerror(message="¡Ese nombre de Usuario ya ha sido tomado!\nIntente con otro nombre o Inicie Sesión",title="Atención")
        else:
            messagebox.showerror(message="¡Las contraseñas no coinciden!\nPor favor verifique para poder registrarse",title="Atención")
            
    def Guardar_Usuario(self):
        Usuario = self.Usuario.get()
        Tipo = self.UserType.get()
        Contra = self.Password.get()
        Contra_conf = self.PasswordConf.get()
        self.DatosValidos = True
        if Contra == "" or Usuario == "":
            messagebox.showerror(message="¡Hay espacios vacios!\nPor favor diligencie cada espacio",title="Atención")
        if Contra == Contra_conf:
            for i in self.UsuariosInfo[self.CurrentRestaurante]["Usuarios"]:
                if i[0] == Usuario and i[3] == Tipo:
                    self.DatosValidos = False
            if self.DatosValidos:
                print("A")
                self.UsuariosInfo[self.CurrentRestaurante]["Usuarios"].append([Usuario,Contra,Tipo])
                with open("UserData/DatosUsuario.json", "w") as write_file:json.dump(self.UsuariosInfo, write_file,indent=4)
                self.Cambiar_a_Inicio()
            else: messagebox.showerror(message="¡Ese nombre de Usuario ya ha sido tomado!\nIntente con otro nombre o Inicie Sesión",title="Atención")
        else:
            messagebox.showerror(message="¡Las contraseñas no coinciden!\nPor favor verifique para poder registrarse",title="Atención")
            #logo
           