from consultas_mysql.conexion_mysql import obtener_conexion_db
from consultas_mysql.consultas_db import insert_venta, insert_venta_producto, reducir_stock
from button.button_cancelar import limpiar_treeview, label_cero
from datetime import datetime
import tkinter as tk
from tkinter import ttk,messagebox
from tablas.tabla_principal import suma_total


def confirmar(treeview, entry_nombre_cliente, label_total_1, 
                label_total, label_vuelto, entry_efectivo):
    """Recorre treeview para obtener los datos y guardar en la db, ventas y stock"""
    conn = obtener_conexion_db()
    cursor = conn.cursor()
    if treeview.get_children():
        fecha_hora = datetime.now()
        total = suma_total(treeview)
        nombre = entry_nombre_cliente.get()
        id_venta = insert_venta(cursor, nombre, fecha_hora, total)
        for row in treeview.get_children():
            values = treeview.item(row, "values")
            id_producto = values[0]
            cantidad = values[2]
            precio = values[3].replace("$","").replace(",","").strip()
            precio = float(precio)
            insert_venta_producto(cursor, id_venta,id_producto, cantidad, precio)
            reducir_stock(cursor, cantidad, id_producto)
        conn.commit()
        limpiar_treeview(treeview)
        label_cero(label_total_1, label_total, label_vuelto, entry_efectivo)
        conn.close()
    else:
        messagebox.showinfo("Aviso", "Tabla vacia.")







