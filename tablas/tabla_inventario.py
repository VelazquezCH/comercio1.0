import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from consultas_mysql.consultas_db import consultar_inventario
from validacion.validar import format_currency



def llenar_tabla_inventario(treeview):
    limpiar_treeview(treeview)
    productos = consultar_inventario()
    contador = 1
    for producto in productos:
        id = producto[0]
        codigo = producto[1]
        nombre = producto[2]
        stock = producto[3]
        precio = format_currency(producto[4])
        treeview.insert("", tk.END, values=(contador, id, codigo, nombre, stock, precio))
        contador += 1

def limpiar_treeview(tabla_treeview):
    for item in tabla_treeview.get_children():
        tabla_treeview.delete(item)







