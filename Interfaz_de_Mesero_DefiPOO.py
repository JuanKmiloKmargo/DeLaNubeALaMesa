# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 14:11:03 2023

@author: espit
"""

import tkinter as tk
from tkinter import ttk

class RestauranteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Meser@ Restaurante de la nube a la mesa")
        self.root.geometry("800x600")
        self.root.configure(bg="#a9ddf3")
        self.root.iconbitmap("C:/Users/espit/OneDrive/Escritorio/Universidad/2S/Programación de computadores/Proyecto(De la nube a la mesa)/Logotipo-Icono.ico")

        self.style = ttk.Style()
        self.style.configure("TButton", font=("Helvetica", 12, "bold"), foreground="black")
        self.style.configure("TLabel", font=("Helvetica", 12, "bold"), foreground="black")
        self.style.configure("TEntry", font=("Helvetica", 12, "bold"), foreground="black")

        self.frame_izquierda = ttk.Frame(self.root)
        self.frame_izquierda.grid(row=0, column=0, padx=10, pady=10, rowspan=3, columnspan=1, sticky="nsew")

        self.frame_derecha = ttk.Frame(self.root, style='Derecha.TFrame')
        self.frame_derecha.grid(row=0, column=1, padx=10, pady=10, rowspan=3, columnspan=1, sticky="nsew")

        self.style.configure('Derecha.TFrame', background="#1E3C72")

        self.mesero_nombre = ""
        self.platos = {
            "Carne binaria": 0,
            "Pollo en bucle": 0,
            "Cerdo en salsa de algoritmos": 0,
            "Arroz con python": 0,
            "Postre de tres lenguajes": 0
        }

        self.row_counter = 2  # Inicializamos row_counter

        self.create_left_frame()

    def create_left_frame(self):
        # ... (código existente)

        self.cantidad_entries = {}

        for plato in self.platos:
            cantidad_label = ttk.Label(self.frame_izquierda, text=f"Cantidad de {plato}:")
            cantidad_label.grid(row=self.row_counter, column=0, padx=5, pady=5)
            
            cantidad_entry = ttk.Entry(self.frame_izquierda)
            cantidad_entry.grid(row=self.row_counter, column=1, padx=5, pady=5)
            
            self.cantidad_entries[plato] = cantidad_entry
            self.row_counter += 1

        # ... (resto del código)

        self.tomar_pedido_button = ttk.Button(self.frame_izquierda, text="Tomar Pedido", command=self.tomar_pedido)
        self.tomar_pedido_button.grid(row=self.row_counter, column=0, columnspan=3, padx=5, pady=10)

        self.nombre_mesero_label = ttk.Label(self.frame_izquierda, text="")
        self.nombre_mesero_label.grid(row=self.row_counter + 1, column=0, columnspan=3, padx=5, pady=5)

        self.lista_pedidos = tk.Listbox(self.frame_derecha, font=("Helvetica", 12, "bold"), fg="black")
        self.lista_pedidos.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.eliminar_pedido_button = ttk.Button(self.frame_izquierda, text="Eliminar Último Pedido", command=self.eliminar_pedido)
        self.eliminar_pedido_button.grid(row=self.row_counter + 2, column=0, columnspan=3, padx=5, pady=5)

        self.imprimir_recibo_button = ttk.Button(self.frame_izquierda, text="Imprimir Recibo", command=self.imprimir_recibo)
        self.imprimir_recibo_button.grid(row=self.row_counter + 3, column=0, columnspan=3, padx=5, pady=10)

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

    def tomar_pedido(self):
        mesa_text = self.mesa_entry.get()

        for plato, cantidad_entry in self.cantidad_entries.items():
            cantidad = cantidad_entry.get()
            if cantidad:
                pedido_info = f"Mesa {mesa_text}: {cantidad} {plato}"
                self.lista_pedidos.insert(tk.END, pedido_info)

        self.mesa_entry.delete(0, tk.END)
        for cantidad_entry in self.cantidad_entries.values():
            cantidad_entry.delete(0, tk.END)

    def eliminar_pedido(self):
        if self.lista_pedidos.size() > 0:
            self.lista_pedidos.delete(tk.END)

    def imprimir_recibo(self):
        recibo_window = tk.Toplevel(self.root)
        recibo_window.title("Recibo")
        recibo_label = tk.Label(recibo_window, text=f"Nombre del Mesero: {self.mesero_nombre}", font=("Helvetica", 12, "bold"), fg="black")
        recibo_label.pack(pady=10)
        for item in self.lista_pedidos.get(0, tk.END):
            recibo_text = tk.Label(recibo_window, text=item, font=("Helvetica", 12, "bold"), fg="black")
            recibo_text.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = RestauranteApp(root)
    root.mainloop()
