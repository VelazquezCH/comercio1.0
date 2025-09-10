
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from consultas_mysql.conexion_mysql import obtener_conexion_db
from consultas_mysql.consultas_db import consultar_un_producto_1
from validacion.validar import format_currency, parse_float_currency
from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox



def agregar_producto_db():
#---------------------------FUNCIONES----------------------

    def limpiar_campos():
        entry_codigo.delete(0,tk.END)
        entry_nombre.delete(0,tk.END)
        entry_precio.delete(0,tk.END)
        entry_cantidad.delete(0,tk.END)


    def agregar_producto_tabla(event=None):        
        try:
            codigo = entry_codigo.get()
            precio = float(entry_precio.get())
            cantidad = int(entry_cantidad.get())
        except ValueError:
            messagebox.showerror("Error", "Número incorrecto")
            return
        if consultar_un_producto_1(codigo):
            messagebox.showinfo("Aviso", "Producto existente")
            limpiar_campos()
            return
        nombre = entry_nombre.get().strip()
        precio = format_currency(precio)
        if not nombre:
            messagebox.showerror("Error", "Nombre de producto vacio.")
            return
        treeviews_tabla.insert("", tk.END, values=(codigo, nombre, precio, cantidad))
        limpiar_campos()
        

    def insertar_prudcto_db():
        conn = obtener_conexion_db()
        cursor = conn.cursor()
        if treeviews_tabla.get_children():
            fecha_hora = datetime.now()
            for row in treeviews_tabla.get_children():
                values = treeviews_tabla.item(row, "values")
                codigo = values[0]
                nombre = values[1]
                precio = parse_float_currency(values[2])
                cantidad = values[3]
                cursor.execute("INSERT INTO productos VALUES (0,%s,%s,%s);", (codigo, nombre, precio))
                cursor.execute("SELECT LAST_INSERT_ID();")
                id_producto = cursor.fetchone()[0]
                cursor.execute("INSERT INTO stock VALUES (%s,%s);", (id_producto, cantidad))
                cursor.execute("INSERT INTO movimiento_stock VALUES (%s,%s,%s);", (id_producto, fecha_hora, cantidad))
                cursor.execute("INSERT INTO movimiento_precio VALUES (%s,%s,%s);", (id_producto, fecha_hora, precio))
            conn.commit()
            cursor.close()
            conn.close()
            limpiar_treeview()


        else:
            messagebox.showerror("Error", "La lista/tabla esta vacia")
            cursor.close()
            conn.close()
            return


    def borrar_select():
        try:
            seleccionados = treeviews_tabla.selection()  # Obtiene los ítems seleccionados
            if not seleccionados:  # Verifica si hay selección
                raise ValueError("No hay elementos seleccionados")
            respuesta = messagebox.askyesno(title="Confirmación", message="¿Seguro que quieres borrar los elementos seleccionados?")
            if respuesta:  
                for item in seleccionados:
                    treeviews_tabla.delete(item)
        except ValueError:
            messagebox.showwarning(title="Aviso", message="Selecciona un elemento para borrar.")
    

    def limpiar_treeview():
        for item in treeviews_tabla.get_children():
            treeviews_tabla.delete(item)


#—————————————————————————————————————————————————————————————————————
#---------------FIN DE LAS FUNCIONES----------------------------------
#—————————————————————————————————————————————————————————————————————

#-------------------Creacion de la ventana--------------------------
    root = tk.Tk()
    root.title("Agregar")
    root.geometry("530x600")
    root.resizable(True, True)

    #--------------- Frame titulo --------------------
    frame_titulo = tk.Frame(root)
    frame_titulo.pack(pady=10)

    label_titulo = tk.Label(frame_titulo, text="Agregar Productos", font=("Arial", 16, "bold"))
    label_titulo.pack()

    #------------------- Frame codigo -----------------
    frame_codigo = tk.Frame(root)
    frame_codigo.pack(anchor="nw", padx=10)

    #--------------------- introducir codigo en el frame------------------
    label_codigo = tk.Label(frame_codigo,text="Código:" )
    label_codigo.pack(side="left")

    entry_codigo = tk.Entry(frame_codigo)
    entry_codigo.pack(side="left", padx=17, pady=10)

    #--------------------- FRAME nombre producto------------------
    frame_nombre = tk.Frame(root)
    frame_nombre.pack(anchor="nw")

    label_nombre = tk.Label(frame_nombre, text="Nombre:")
    label_nombre.pack(side="left", padx=10, pady=10)

    entry_nombre = tk.Entry(frame_nombre)
    entry_nombre.pack(pady=10, padx=2)

    #--------------------- FRAME precio producto------------------
    frame_precio = tk.Frame(root)
    frame_precio.pack(anchor="nw")

    label_precio = tk.Label(frame_precio, text="Precio:")
    label_precio.pack(side="left", padx=10)

    entry_precio = tk.Entry(frame_precio)
    entry_precio.config(width=10)
    entry_precio.pack( padx=13, pady=10)

        #--------------------- FRAME cantidad producto------------------
    frame_cantidad = tk.Frame(root)
    frame_cantidad.pack(anchor="nw")

    label_cantidad = tk.Label(frame_cantidad, text="cantidad:")
    label_cantidad.pack(side="left", padx=10)

    entry_cantidad = tk.Entry(frame_cantidad)
    entry_cantidad.config(width=10)
    entry_cantidad.pack(side="left", pady=10)

    button_agregar = ttk.Button(frame_cantidad, text="Agrear a la lista", command=agregar_producto_tabla)
    button_agregar.pack(padx=10, pady=10)


    # ------------------- FRAME TABLA treeviews ------------------------
    frame_tabla = tk.LabelFrame(root,text="Lista de productos a agregar.")
    frame_tabla.configure(highlightthickness=5)
    frame_tabla.pack(expand=True, padx=10, pady=10, anchor="nw")

    ##----------------------TABLA treeviews ----------------------------
    treeviews_tabla = ttk.Treeview(frame_tabla, columns=("codigo_producto", "nombre_producto", "precio_producto", "stock_producto"), show="headings")
    treeviews_tabla.pack(expand=True, padx=10, pady=10)

    # --------------------------Configurar encabezados de la TABLA TREEVIEWS--------------------------
    treeviews_tabla.heading("codigo_producto", text="Codigo")
    treeviews_tabla.heading("nombre_producto", text="Nombre")
    treeviews_tabla.heading("precio_producto", text="Precio")
    treeviews_tabla.heading("stock_producto", text="Cantidad")

    #----------------------- Configuracio tamaño de las columnas de la TABLA TREEVIEWS----------------
    treeviews_tabla.column("codigo_producto", width=150)
    treeviews_tabla.column("nombre_producto", width=150)
    treeviews_tabla.column("precio_producto", width=75, anchor="center")
    treeviews_tabla.column("stock_producto", width=75, anchor="center")

    #-------------- FRAME BUTTON ---------------------------------------------
    frame_button = tk.Frame(root)
    frame_button.pack(anchor="nw", padx=10, pady=10)

    button_confirmar = ttk.Button(frame_button, text="Confirmar", command=insertar_prudcto_db)
    button_confirmar.pack(side="left", padx=10, pady=10)

    button_quitar = ttk.Button(frame_button, text="Quitar", command=borrar_select)
    button_quitar.pack(side="left", padx=10, pady=10)

    button_cancelar = ttk.Button(frame_button, text="Cancelar", command=root.quit)
    button_cancelar.pack(side="left", padx=10, pady=10)

    root.mainloop()
