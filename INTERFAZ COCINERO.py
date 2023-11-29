# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 19:47:27 2023

@author: JOHN TUPAZ
"""

import tkinter as tk
from tkinter import ttk

class CocineroGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simulación de Cocina")
        self.geometry("1000x600")
        
        self.marco = tk.Frame(self)
        self.marco.pack(fill=tk.BOTH, expand=True)

        # Creamos una función para actualizar el tamaño del lienzo
        self.canvas = tk.Canvas(self.marco)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.actualizar_tamano_lienzo()  # Llamamos a la función una vez para ajustar el tamaño inicial

        self.bind("<Configure>", lambda event: self.actualizar_tamano_lienzo()) 
        
        #icono_path = "C:/Users/JOHN TUPAZ/proyecto programacion/Logotipo-Icono.ico"
        #self.iconbitmap(icono_path)# Detectamos cambios en el tamaño de la ventana

        self.cocinero = Cocinero(self.marco)

    def actualizar_tamano_lienzo(self):
        # Borramos cualquier elemento en el lienzo para evitar superposiciones
        self.canvas.delete("all")
        
        # Dibujamos el fondo degradado con el nuevo tamaño de la ventana
        for i in range(self.winfo_height()):
            r = int(0 + i * (0 - 0) / self.winfo_height())
            g = int(0 + i * (0 - 0) / self.winfo_height())
            b = int(0 + i * (255 - 0) / self.winfo_height())
            color = f"#{r:02x}{g:02x}{b:02x}"
            self.canvas.create_line(0, i, self.winfo_width(), i, fill=color)

        # Volvemos a traer a la vista el resto de los elementos
        self.canvas.lower("all")  # Para que el lienzo esté detrás del resto de los elementos

class Cocinero:
    def __init__(self, ventana):
        self.ventana = ventana

        titulo_label = tk.Label(ventana, text="Interfaz de Cocinero", font=("Times", 28), background="#000000", foreground="#ffffff")
        titulo_label.place(relx=0.5, rely=0.1, anchor="center")

        self.boton_salir = ttk.Button(ventana, text="Salir", command=ventana.master.destroy)
        self.boton_salir.place(relx=0.5, rely=0.9, anchor="center")

        self.platos = ["carne binaria", "pollo en bucle", "cerdo en salsa de algoritmo", "arroz con python", "postre de tres lenguajes"]
        self.pedidos = []

        self.label_plato = tk.Label(ventana, text="Nombre del plato:", font=("Times", 15), background="gray")
        self.label_plato.place(relx=0.5, rely=0.3, anchor="center",)

        self.entry_plato = tk.Entry(ventana)
        self.entry_plato.place(relx=0.5, rely=0.4, anchor="center")
        self.entry_plato.bind("<Return>", self.preparar_y_servir)

        self.label_mesa = tk.Label(ventana, text="Número de mesa:", font=("Times", 15), background="gray")
        self.label_mesa.place(relx=0.5, rely=0.5, anchor="center")

        self.entry_mesa = tk.Entry(ventana)
        self.entry_mesa.place(relx=0.5, rely=0.6, anchor="center")
        self.entry_mesa.bind("<Return>", self.preparar_y_servir)

        self.boton_siguiente = tk.Button(ventana, text="Siguiente Pedido", command=self.siguiente_pedido, bg="gray", font=("Times", 12))
        self.boton_siguiente.place(relx=0.5, rely=0.7, anchor="center")

        self.resultado = tk.Label(ventana, text="", font=("Times", 12), background="#00008b", foreground="#ffffff")
        self.resultado.place(relx=0.5, rely=0.8, anchor="center")
        self.indice_pedido = 0

    def preparar_y_servir(self, event):
        plato = self.entry_plato.get()
        mesa = self.entry_mesa.get()
        if plato in self.platos:
            self.pedidos.append((plato, mesa))
            resultado = f"Cocinero está preparando y sirviendo {plato} en la mesa {mesa}."
            self.resultado.config(text=resultado)
            self.entry_plato.delete(0, tk.END)
            self.entry_mesa.delete(0, tk.END)
        else:
            resultado = "Plato no disponible en el menú."
            self.resultado.config(text=resultado)
            self.entry_plato.delete(0, tk.END)
            self.entry_mesa.delete(0, tk.END)

    def siguiente_pedido(self):
        if self.indice_pedido < len(self.pedidos):
            plato, mesa = self.pedidos[self.indice_pedido]
            resultado = f" pendiente: {plato} en la mesa {mesa}."
            self.resultado.config(text=resultado)
            self.indice_pedido += 1
        else:
            resultado = "No hay más pedidos."
            self.resultado.config(text=resultado)

def main():
    app = CocineroGUI()
    app.mainloop()

if __name__ == "__main__":
    main()

