# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 21:27:33 2023

@author: espit
"""

import tkinter as tk
from tkinter import PhotoImage

# Función para calcular el total
def calcular_total():
    total_sin_iva = 0
    for plato, precio in precios.items():
        cantidad = entry_platos[plato].get()
        if cantidad.strip(): 
            cantidad = int(cantidad)
            total_sin_iva += cantidad * precio

    iva = total_sin_iva * 0.08
    total_con_iva = round(total_sin_iva + iva, -1) 
    label_total.config(text=f"Total (con 8% de IVA): ${total_con_iva}", fg="red")

ventana = tk.Tk()
ventana.title("Caja Restaurante De la nube a la mesa")

ancho_ventana = ventana.winfo_screenwidth()
alto_ventana = ventana.winfo_screenheight()
ventana.geometry(f'{ancho_ventana}x{alto_ventana}')
ventana.configure(bg="#a9ddf3")  # Fondo azul claro

precios = {
    "Carne binaria": 20000,
    "Pollo en bucle": 17000,
    "Cerdo en salsa de algoritmos": 26000,
    "Arroz con python": 10000,
    "Postre de tres lenguajes": 5000
}

contenido_marco = tk.Frame(ventana, bg="#a9ddf3")
contenido_marco.pack(side="left", fill="both", expand=True)

entry_platos = {}

row = 0
for plato, precio in precios.items():
    label = tk.Label(contenido_marco, text=plato, font=("Helvetica", 24, "bold"), bg="#a9ddf3")
    label.grid(row=row, column=0, sticky='w', padx=20, pady=20)
    entry_plato = tk.Entry(contenido_marco)
    entry_plato.grid(row=row, column=1)
    entry_platos[plato] = entry_plato
    row += 1

calcular_button = tk.Button(contenido_marco, text="Calcular Total", command=calcular_total, font=("Helvetica", 18, "bold"), bg="#007ACC", fg="white")
calcular_button.grid(row=row + 1, column=0, columnspan=2, pady=20)

icono_path = "C:/Users/espit/OneDrive/Escritorio/Universidad/2S/Programación de computadores/Proyecto(De la nube a la mesa)/Logotipo-Icono.ico"
ventana.iconbitmap(icono_path)

imagen_path = "C:/Users/espit/Downloads/Logotipo-Icono.png"
imagen = PhotoImage(file=imagen_path)

imagen_marco = tk.Frame(ventana, bg="#1E3C72")
imagen_marco.pack(side="right", fill="both", expand=True)
imagen_label = tk.Label(imagen_marco, image=imagen, bg="#1E3C72")
imagen_label.pack(fill="both", expand=True)

label_total = tk.Label(contenido_marco, text="Total (con 8% de IVA): $0", font=("Helvetica", 24, "bold"), fg="red", bg="#a9ddf3")
label_total.grid(row=row, column=0, columnspan=2, pady=20, padx=20)

ventana.mainloop()
