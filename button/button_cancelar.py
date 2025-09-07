import tkinter as tk
from tkinter import messagebox


def button_cancelar(treeview, label_1, label_2, label_3, monto_entry):
    respuesta = messagebox.askyesno("Aviso", "Esta por cancelar, ¿Desea continuar?")
    if respuesta:
        limpiar_treeview(treeview)
    label_cero(label_1, label_2, label_3, monto_entry)
    
def limpiar_treeview(treeview):
    for item in treeview.get_children():
            treeview.delete(item)

def label_cero(label_1, label_2, label_3, monto_entry):
    label_1.config(text=f"Total: ${0:,.2f}")
    label_2.config(text=f"Total: ${0:,.2f}")
    label_3.config(text=f"Vuelto: ${0:,.2f}")
    monto_entry.delete(0,tk.END)
    monto_entry.insert(0,0)

