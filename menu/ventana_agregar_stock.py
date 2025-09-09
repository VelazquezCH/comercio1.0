import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import messagebox, ttk
from consultas_mysql.consultas_db import consultar_un_producto, insert_movimiento_producto_stock, agregar_stock,obtener_cursor
from datetime import datetime





def ventana_agregar_stock():
    def aceptar():
        try:
            cod = int(entry_codigo.get())
            cantidad = int(entry_cantidad.get())
        except ValueError:
            messagebox.showerror("Error", "Solo nhúmeros")
        producto = consultar_un_producto(cod)
        if producto and cantidad > 0:
            nombre = producto[2]
            tabla.insert("", tk.END, values=(cod, nombre, cantidad)) 
            entry_codigo.delete(0,tk.END)   
            entry_cantidad.delete(0,tk.END)
            entry_cantidad.insert(0,1)
        
    def quitar_select():
        try:
            seleccionados = tabla.selection()#devuelve tupla (I001,)
            respuesta = messagebox.askyesno("Aviso", "Esta por quitar, ¿Desea continuar?")
            if respuesta:
                for item in seleccionados:
                    tabla.delete(item)
        except ValueError:
            messagebox.showerror("Error", "Debe seleccionar un elemento a quitar.")

    def actualizar_stock():
        conexion = obtener_cursor()
        conn = conexion[0]
        cursor = conexion[1]
        fecha_hora = datetime.now()
        if tabla.get_children():
            for item in tabla.get_children():
                valores = tabla.item(item, "values")
                cod = valores[0]
                cantidad = valores[2]
                id_producto = consultar_un_producto(cod)
                id_producto = id_producto[0]
                insert_movimiento_producto_stock(cursor, id_producto, fecha_hora, cantidad)
                agregar_stock(cursor, cantidad, id_producto)
            conn.commit()
            messagebox.showinfo("Exitoso", message="Se guardaron los cambios con exito")
            root.destroy()
        else:
            messagebox.showinfo("Aviso", message="Tabla vacia")


    root = tk.Tk()
    root.title("Agregar Stock de Varios Productos")
    root.geometry("400x300")
    root.resizable(False, False)

    # ───────────── Frame Título ─────────────
    frame_titulo = tk.Frame(root)
    frame_titulo.pack(pady=10)

    label_titulo = tk.Label(frame_titulo, text="Agregar Stock", font=("Arial", 16, "bold"))
    label_titulo.pack()

    # ───────────── Frame Formulario ─────────────
    frame_formulario = tk.Frame(root)
    frame_formulario.pack(padx=20, pady=10)

    # Usamos grid dentro del frame_formulario
    label_codigo = tk.Label(frame_formulario, text="Código del producto:")
    label_codigo.grid(row=0, column=0, sticky="e", pady=5)

    entry_codigo = tk.Entry(frame_formulario)
    entry_codigo.grid(row=0, column=1, pady=5)

    label_cantidad = tk.Label(frame_formulario, text="Cantidad a agregar:")
    label_cantidad.grid(row=1, column=0, sticky="e", pady=5)

    entry_cantidad = tk.Entry(frame_formulario)
    entry_cantidad.grid(row=1, column=1, pady=5)
    entry_cantidad.insert(0,1)

    # ───────────── Frame Botones ─────────────
    frame_botones = tk.Frame(root)
    frame_botones.pack(pady=20, side="top")

    boton_aceptar = tk.Button(frame_botones, text="Aceptar", width=10, command=aceptar)
    boton_aceptar.pack(side="left", padx=10)

    boton_cancelar = tk.Button(frame_botones, text="Cancelar", width=10, command=root.destroy)
    boton_cancelar.pack(side="left", padx=10)

    boton_quitar = tk.Button(frame_botones, text="Quitar", width=10, command= lambda:quitar_select())
    boton_quitar.pack(side="left", padx=10)

    boton_guardar_db = tk.Button(frame_botones, text="Guardar lista/stock", command=actualizar_stock)
    boton_guardar_db.pack(side="left", padx=10)

    #------------Frame tabla ---------------

    frame_tabla = tk.Frame(root)
    frame_tabla.pack(padx=20, pady=10, fill="both", expand=True)

    #-----------Tabla Treeview -----------

    tabla = ttk.Treeview(frame_tabla, columns=("codigo","nombre", "cantidad"), 
                    show="headings")
    tabla.heading("codigo", text="Código")
    tabla.heading("nombre", text="Nombre Producto")
    tabla.heading("cantidad", text="Cantidad")
    tabla.column("codigo", width=120)
    tabla.column("nombre", width=150)
    tabla.column("cantidad", width=100)
    tabla.pack(side="left", fill="both", expand=True)

    root.mainloop()

#ventana_agregar_stock()


