# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 14:09:37 2023

@author: espit
"""

import tkinter as tk
from tkinter import ttk

mesero_nombre = ""
platos = {
    "Carne binaria": 0,
    "Pollo en bucle": 0,
    "Cerdo en salsa de algoritmos": 0,
    "Arroz con python": 0,
    "Postre de tres lenguajes": 0
}

def capturar_nombre_mesero():
    global mesero_nombre
    mesero_nombre = nombre_mesero_entry.get()
    nombre_mesero_entry.config(state=tk.DISABLED)  
    nombre_mesero_label.config(text=f"Nombre del Mesero: {mesero_nombre}", font=("Helvetica", 12, "bold"), fg="black")

def tomar_pedido():
    mesa_text = mesa_entry.get()

    for plato, cantidad_entry in cantidad_entries.items():
        cantidad = cantidad_entry.get()
        if cantidad:
            pedido_info = f"Mesa {mesa_text}: {cantidad} {plato}"
            lista_pedidos.insert(tk.END, pedido_info)

    mesa_entry.delete(0, tk.END)
    for cantidad_entry in cantidad_entries.values():
        cantidad_entry.delete(0, tk.END)

def eliminar_pedido():
    if lista_pedidos.size() > 0:
        lista_pedidos.delete(tk.END)

def imprimir_recibo():
    recibo_window = tk.Toplevel(root)
    recibo_window.title("Recibo")
    recibo_label = tk.Label(recibo_window, text=f"Nombre del Mesero: {mesero_nombre}", font=("Helvetica", 12, "bold"), fg="black")
    recibo_label.pack(pady=10)
    for item in lista_pedidos.get(0, tk.END):
        recibo_text = tk.Label(recibo_window, text=item, font=("Helvetica", 12, "bold"), fg="black")
        recibo_text.pack()

root = tk.Tk()
root.title("Meser@ Restaurante de la nube a la mesa")
root.geometry("800x600")

root.configure(bg="#a9ddf3")

root.iconbitmap("C:/Users/espit/OneDrive/Escritorio/Universidad/2S/Programación de computadores/Proyecto(De la nube a la mesa)/Logotipo-Icono.ico")

style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12, "bold"), foreground="black")
style.configure("TLabel", font=("Helvetica", 12, "bold"), foreground="black")
style.configure("TEntry", font=("Helvetica", 12, "bold"), foreground="black")

frame_izquierda = ttk.Frame(root)
frame_izquierda.grid(row=0, column=0, padx=10, pady=10, rowspan=3, columnspan=1, sticky="nsew")

frame_derecha = ttk.Frame(root, style='Derecha.TFrame')
frame_derecha.grid(row=0, column=1, padx=10, pady=10, rowspan=3, columnspan=1, sticky="nsew")

style.configure('Derecha.TFrame', background="#1E3C72")

nombre_mesero_label = ttk.Label(frame_izquierda, text="Nombre del Mesero:")
nombre_mesero_label.grid(row=0, column=0, padx=5, pady=5)
nombre_mesero_entry = ttk.Entry(frame_izquierda)
nombre_mesero_entry.grid(row=0, column=1, padx=5, pady=5)
nombre_mesero_button = ttk.Button(frame_izquierda, text="Capturar Nombre", command=capturar_nombre_mesero)
nombre_mesero_button.grid(row=0, column=2, padx=5, pady=5)

mesa_label = ttk.Label(frame_izquierda, text="Número de Mesa:")
mesa_label.grid(row=1, column=0, padx=5, pady=5)
mesa_entry = ttk.Entry(frame_izquierda)
mesa_entry.grid(row=1, column=1, padx=5, pady=5)

cantidad_entries = {}
row_counter = 2
for plato in platos:
    cantidad_label = ttk.Label(frame_izquierda, text=f"Cantidad de {plato}:")
    cantidad_label.grid(row=row_counter, column=0, padx=5, pady=5)
    cantidad_entry = ttk.Entry(frame_izquierda)
    cantidad_entry.grid(row=row_counter, column=1, padx=5, pady=5)
    cantidad_entries[plato] = cantidad_entry
    row_counter += 1

tomar_pedido_button = ttk.Button(frame_izquierda, text="Tomar Pedido", command=tomar_pedido)
tomar_pedido_button.grid(row=row_counter, column=0, columnspan=3, padx=5, pady=10)

nombre_mesero_label = ttk.Label(frame_izquierda, text="")
nombre_mesero_label.grid(row=row_counter + 1, column=0, columnspan=3, padx=5, pady=5)

lista_pedidos = tk.Listbox(frame_derecha, font=("Helvetica", 12, "bold"), fg="black")
lista_pedidos.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

eliminar_pedido_button = ttk.Button(frame_izquierda, text="Eliminar Último Pedido", command=eliminar_pedido)
eliminar_pedido_button.grid(row=row_counter + 2, column=0, columnspan=3, padx=5, pady=5)

imprimir_recibo_button = ttk.Button(frame_izquierda, text="Imprimir Recibo", command=imprimir_recibo)
imprimir_recibo_button.grid(row=row_counter + 3, column=0, columnspan=3, padx=5, pady=10)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

root.mainloop()
