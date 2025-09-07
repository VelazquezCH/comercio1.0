import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from consultas_mysql.conexion_mysql import obtener_conexion_db
import tkinter as tk
from tkinter import messagebox
from validacion.validar import pasar_int

    

def consultar_un_producto(cod):
    codigo = pasar_int(cod)
    try:
        conn = obtener_conexion_db()
    except Exception:
        messagebox.showerror("Error", "No se pudo establecer conexion a la base de datos")
        return
    cursor = conn.cursor()
    cursor.execute("SELECT p.ID_producto, p.codigo, p.nombre, s.stock, p.precio \
                   FROM productos AS p LEFT JOIN stock s ON s.ID_producto = p.ID_producto\
                    WHERE p.codigo = %s ;", (codigo,))
    resultado_consulta = cursor.fetchall()
    if resultado_consulta:
        id = resultado_consulta[0][0]
        nombre = resultado_consulta[0][2]
        stock = resultado_consulta[0][3]
        precio = resultado_consulta[0][4]
        conn.close()
        return id, codigo, nombre, stock, precio #retorna una tupla con id cod, nom, stock, precio
    else:
        messagebox.showerror("Error", "Producto no encontrado.")
    
def consultar_inventario():
    try:
        conn = obtener_conexion_db()
    except Exception:
        messagebox.showerror("Error", "No se pudo establecer conexion a la base de datos")
        return
    cursor = conn.cursor()
    cursor.execute("SELECT p.ID_producto, p.codigo, p.nombre, s.stock, p.precio \
                   FROM productos AS p LEFT JOIN stock s ON p.ID_producto = s.ID_producto\
                   ORDER BY p.nombre ;")
    resultado = cursor.fetchall()
    if resultado:
        return resultado# devuelve una lista con tuplas
    conn.close()


def insert_venta(cursor, nombre, fecha_hora, total):
    """Agrega nombre, fecha, total de la compra a la tabla venta retorna 
    ID_venta para hacer referancia en la tabla venta_producto"""
    cursor.execute("INSERT INTO ventas (nombre, fecha, total) VALUES( %s, %s, %s)",
                (nombre, fecha_hora,total))
    cursor.execute("SELECT LAST_INSERT_ID();")
    id_venta = cursor.fetchone()[0]
    return id_venta

def insert_venta_producto(cursor, id_venta, id_producto, cantidad, precio):
    """Agrega id de venta, id producto, cantidad y precio a la tabla venta_producto"""
    cursor.execute("INSERT INTO venta_producto (ID_venta, ID_producto, \
                   cantidad, precio) VALUES (%s, %s, %s, %s)",
                (id_venta, id_producto, cantidad, precio))

def reducir_stock(cursor, cantidad, id):
    """Actudaliza tabla de stock, desde la funcion confirmar,
     ingresar cursor, cantidad e id_producto"""
    cursor.execute("UPDATE stock SET stock = stock - %s where ID_producto = %s;",(cantidad, id))
