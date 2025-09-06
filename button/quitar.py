from tkinter import messagebox
from tablas.tabla_principal import suma_total




def quitar_select(treeview, label):
    try:
        seleccionados = treeview.selection()#devuelve tupla (I001,)
        respuesta = messagebox.askyesno("Aviso", "Esta por quitar, ¿Desea continuar?")
        if respuesta:
            for item in seleccionados:
                treeview.delete(item)
            suma_total(treeview, label)
    except ValueError:
        messagebox.showerror("Error", "Debe seleccionar un elemento a quitar.")






