import tkinter as tk
from tkinter import messagebox
from consultas_mysql.consultas_db import consultar_un_producto
from validacion.validar import format_currency




def llenar_tabla_principal(treeview, cod, cantidad, entry_cod, entry_cant, label):
    try:
        cod = int(cod)
        cantidad = int(cantidad)
    except ValueError:
        messagebox.showerror("Error", "Número incorecto")
        return
    producto = consultar_un_producto(cod)
    if producto:
        id = producto[0]
        nombre = producto[2]
        precio = producto[4]
        total = cantidad * precio
        precio = format_currency(precio)
        total = format_currency(total)
        treeview.insert("", tk.END, values=(id, nombre, cantidad, precio, total))
        limpiar_campos(treeview, entry_cod, entry_cant)
        suma_total(treeview, label)

def limpiar_campos(treeview, entry_cod, entry_cant):
    entry_cod.delete(0,tk.END)   
    entry_cant.delete(0,tk.END)
    entry_cant.insert(0,1)

def suma_total(treeview, label):
    total_compra = 0
    for item in treeview.get_children():
        valores = treeview.item(item, "values")
        precio = valores[4]
        precio = float(precio.replace("$", "").replace(",", "").strip())
        total_compra += precio
    label.config(text=f"Total: ${total_compra:,.2f}")
    return total_compra