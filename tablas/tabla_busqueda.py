import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from consultas_mysql.consultas_db import consultar_un_producto
from validacion.validar import format_currency


def llenar_tabla_busqueda(cod, treeview):
    try:
        cod = int(cod)
    except ValueError:
        return
    limpiar_grid(treeview)
    producto = consultar_un_producto(cod)
    if producto:
        id_producto = producto[0]
        codigo = producto[1]
        nombre = producto[2]
        stock = producto[3]
        precio = format_currency(producto[4])
        treeview.insert("", tk.END, values=(id_producto, codigo, nombre, stock, precio))
    

def limpiar_grid(tabla_treeview):
    for item in tabla_treeview.get_children():
        tabla_treeview.delete(item)




print("desde tabla_busqueda")





