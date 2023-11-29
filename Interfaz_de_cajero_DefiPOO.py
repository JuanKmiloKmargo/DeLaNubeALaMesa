# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 14:08:58 2023

@author: espit
"""

import tkinter as tk
from tkinter import PhotoImage

class RestauranteApp:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Caja Restaurante De la nube a la mesa")

        ancho_ventana = ventana.winfo_screenwidth()
        alto_ventana = ventana.winfo_screenheight()
        self.ventana.geometry(f'{ancho_ventana}x{alto_ventana}')
        self.ventana.configure(bg="#a9ddf3")

        self.precios = {
            "Carne binaria": 20000,
            "Pollo en bucle": 17000,
            "Cerdo en salsa de algoritmos": 26000,
            "Arroz con python": 10000,
            "Postre de tres lenguajes": 5000
        }

        self.create_widgets()

    def create_widgets(self):
        self.contenido_marco = tk.Frame(self.ventana, bg="#a9ddf3")
        self.contenido_marco.pack(side="left", fill="both", expand=True)

        self.entry_platos = {}
        row = 0

        for plato, precio in self.precios.items():
            label = tk.Label(self.contenido_marco, text=plato, font=("Helvetica", 24, "bold"), bg="#a9ddf3")
            label.grid(row=row, column=0, sticky='w', padx=20, pady=20)
            entry_plato = tk.Entry(self.contenido_marco)
            entry_plato.grid(row=row, column=1)
            self.entry_platos[plato] = entry_plato
            row += 1

        self.calcular_button = tk.Button(self.contenido_marco, text="Calcular Total", command=self.calcular_total,
                                         font=("Helvetica", 18, "bold"), bg="#007ACC", fg="white")
        self.calcular_button.grid(row=row + 1, column=0, columnspan=2, pady=20)

        icono_path = "C:/Users/espit/OneDrive/Escritorio/Universidad/2S/Programación de computadores/Proyecto(De la nube a la mesa)/Logotipo-Icono.ico"
        self.ventana.iconbitmap(icono_path)

        imagen_path = "C:/Users/espit/Downloads/Logotipo-Icono.png"
        self.imagen = PhotoImage(file=imagen_path)

        self.imagen_marco = tk.Frame(self.ventana, bg="#1E3C72")
        self.imagen_marco.pack(side="right", fill="both", expand=True)
        self.imagen_label = tk.Label(self.imagen_marco, image=self.imagen, bg="#1E3C72")
        self.imagen_label.pack(fill="both", expand=True)

        self.label_total = tk.Label(self.contenido_marco, text="Total (con 8% de IVA): $0",
                                    font=("Helvetica", 24, "bold"), fg="red", bg="#a9ddf3")
        self.label_total.grid(row=row, column=0, columnspan=2, pady=20, padx=20)

    def calcular_total(self):
        total_sin_iva = 0
        for plato, precio in self.precios.items():
            cantidad = self.entry_platos[plato].get()
            if cantidad.strip():
                cantidad = int(cantidad)
                total_sin_iva += cantidad * precio

        iva = total_sin_iva * 0.08
        total_con_iva = round(total_sin_iva + iva, -1)
        self.label_total.config(text=f"Total (con 8% de IVA): ${total_con_iva}", fg="red")

if __name__ == "__main__":
    ventana_principal = tk.Tk()
    app = RestauranteApp(ventana_principal)
    ventana_principal.mainloop()
