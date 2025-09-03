import tkinter as tk
from tkinter import messagebox, ttk
from tablas.tabla_inventario import llenar_tabla_inventario
from tablas.tabla_busqueda import llenar_tabla_busqueda
from tablas.tabla_principal import llenar_tabla_principal




def main():
    root = tk.Tk()
    root.title("Comercio Laura")

    #---------------------- widgets principales--------------------

    label_nombre_cliente = tk.Label(root, text="Nombre :")
    label_nombre_cliente.grid(row=0, column=0, padx=10, pady=10)
    
    entry_nombre_cliente = ttk.Entry()
    entry_nombre_cliente.grid(row=0, column=1, padx=10, pady=10)

    label_codigo =  tk.Label(root, text="Codigo :")
    label_codigo.grid(row=1, column=0, padx=10, pady=10)
    
    entry_codigo = ttk.Entry()
    entry_codigo.bind("<Return>", lambda event: llenar_tabla_principal(
                treeview_tabla_principal, entry_codigo.get(),entry_cantidad.get(), 
                entry_codigo, entry_cantidad, label_total_1))
    entry_codigo.grid(row=1, column=1, padx=10, pady=10)

    label_cantidad = tk.Label(root, text="Cantidad :")
    label_cantidad.grid(row=2, column=0, padx=10, pady=10)
    
    entry_cantidad = ttk.Entry()
    entry_cantidad.grid(row=2, column=1, padx=10, pady=10)
    entry_cantidad.bind("<Return>", lambda event: llenar_tabla_principal(
                treeview_tabla_principal, entry_codigo.get(),entry_cantidad.get(), 
                entry_codigo, entry_cantidad, label_total_1))
    entry_cantidad.insert(0,1)

    boton_agregar = ttk.Button(root, text="Agregar", 
                command= lambda: llenar_tabla_principal(
                treeview_tabla_principal, entry_codigo.get(), 
                entry_cantidad.get(), entry_codigo, entry_cantidad, label_total_1))   
    boton_agregar.grid(row= 2, column=2, padx=10, pady=10)

    boton_quitar = ttk.Button(root, text="Quitar")
    boton_quitar.grid(row= 2, column=3, padx=10, pady=10)

    boton_confirmar = ttk.Button(root, text="Confirmar")
    boton_confirmar.grid(row= 2, column=4, padx=10, pady=10)

    boton_cancelar = ttk.Button(root, text="Cancelar")
    boton_cancelar.grid(row= 2, column=5, padx=10, pady=10)

    label_total_1 = tk.Label(root, text= "Total : ")
    label_total_1.grid(row=1, column=2, columnspan=2, padx=10, pady=10)
    label_total_1.config(font=("Arial", 14, "bold"), fg="black")

    treeview_tabla_principal = ttk.Treeview(root, columns=("id", "nombre", "cantidad",
                "precio", "total"), show="headings")
    treeview_tabla_principal.grid(row=3, column=0, rowspan=10 , columnspan=6, padx=10, pady=10)
    treeview_tabla_principal.heading("id", text="ID")
    treeview_tabla_principal.heading("nombre", text="Nombre")
    treeview_tabla_principal.heading("cantidad", text="Cantidad")
    treeview_tabla_principal.heading("precio", text="Precio")
    treeview_tabla_principal.heading("total", text="Total")
    treeview_tabla_principal.column("id", width=50)
    treeview_tabla_principal.column("cantidad", width=50)
    treeview_tabla_principal.column("precio", width=100)
    treeview_tabla_principal.column("total", width=100)

    #------------------------ RadioButonn ----------------------

    radiobuton_var = tk.IntVar()
    radiobuton_var.set(1)

    radiobuton_efectivo = ttk.Radiobutton(root, text="Efectivo", variable=radiobuton_var, value=1)
    radiobuton_efectivo.grid(row=13, column=0, padx=10, pady=10)

    
    radiobuton_efectivo_transferencia = ttk.Radiobutton(root, text="Efectivo-tranferencia", 
                variable=radiobuton_var, value=2)
    radiobuton_efectivo_transferencia.grid(row=13, column=1, padx=10, pady=10)

    
    radiobuton_transferencia = ttk.Radiobutton(root, text="Tranferencia", 
                variable=radiobuton_var, value=3)
    radiobuton_transferencia.grid(row=13, column=2, padx=10, pady=10)

        
    label_efectivo = ttk.Label(root, text="Monto :")
    label_efectivo.grid(row=14, column=0, padx=10, pady=10)

    entry_efectivo = ttk.Entry()
    entry_efectivo.grid(row=14, column=1, padx=10, pady=10)

    label_transferencia = ttk.Label(root, text="Transferencia :")
    label_transferencia.grid(row=14, column=2, padx=10, pady=10)

    entry_transferencia = ttk.Entry(root)
    entry_transferencia.grid(row=14, column=3, padx=10, pady=10)

    label_vuelto = tk.Label(root, text= "Vuelto: 0")
    label_vuelto.grid(row=14, column=4, padx=10, pady=10)
    label_vuelto.config(font=("Arial", 14, "bold"), fg="red")

    label_total = tk.Label(root, text= "Total : ")
    label_total.grid(row=13, column=4, padx=10, pady=10)
    label_total.config(font=("Arial", 14, "bold"), fg="red")


    #------------------------Segunda tabla derecha --------------------------------

    frame1 = ttk.Labelframe(root, text="Tabla STOCK-PRECIO")
    frame1.grid(row=0, column=7, rowspan=15, columnspan=5, padx=10, pady=10)

    notebook =ttk.Notebook(frame1)
    notebook.pack(padx=10, pady=10, fill="both", expand=True)

    frame_notebook1 = ttk.Frame(notebook, padding=10)
    frame_notebook2 = ttk.Frame(notebook, padding=10)

    notebook.add(frame_notebook1, text="Precios-Stock")
    notebook.add(frame_notebook2, text="Consultas")

    #---------------- PRIMER PESTAÑA---------------------------------------------------

    boton_actualizar_tabla_stock_precio = ttk.Button(frame_notebook1, text="Actualizar", 
                command=lambda: llenar_tabla_inventario(treeview_tabla_stcok_precio))
    boton_actualizar_tabla_stock_precio.pack()

    treeview_tabla_stcok_precio = ttk.Treeview(frame_notebook1, columns=(" ", "id", "codigo", 
                                            "nombre", "stock", "precio"), show="headings")
    treeview_tabla_stcok_precio.pack(padx=10, pady=10)
    treeview_tabla_stcok_precio.heading(" ", text=" ", anchor="center")
    treeview_tabla_stcok_precio.heading("id", text="ID", anchor="center")
    treeview_tabla_stcok_precio.heading("codigo", text="codigo", anchor="center")
    treeview_tabla_stcok_precio.heading("nombre", text="Nombre", anchor="center")
    treeview_tabla_stcok_precio.heading("stock", text="Stock", anchor="center")
    treeview_tabla_stcok_precio.heading("precio", text="Precio", anchor="center")
    treeview_tabla_stcok_precio.column(" ", width=25)
    treeview_tabla_stcok_precio.column("id", width=50, anchor="center")
    treeview_tabla_stcok_precio.column("codigo", width=80, anchor="center")
    treeview_tabla_stcok_precio.column("stock", width=50, anchor="center")
    treeview_tabla_stcok_precio.column("precio", width=100, anchor="center")

    llenar_tabla_inventario(treeview_tabla_stcok_precio)

    frame_botones1 = ttk.Frame(frame_notebook1)
    frame_botones1.pack()

    boton_agregar_tabla_principal = ttk.Button(frame_botones1, text="Agregar a la lista")
    boton_agregar_tabla_principal.grid(row=0, column=0, padx=10, pady=10)
    
    boton_modificar_precio = ttk.Button(frame_botones1, text="Modificar Precio")
    boton_modificar_precio.grid(row=0, column=1, padx=10, pady=10)

  

    #------------------------------- segunda PESTAÑA ---------------------------------------

    frame_busqueda = ttk.Frame(frame_notebook2)
    frame_busqueda.pack(anchor="n")

    label_busqueda = ttk.Label(frame_busqueda, text="Codigo:")
    label_busqueda.pack(anchor="ne", side="left", padx=10, pady=10)

    entry_busqueda_codigo = ttk.Entry(frame_busqueda)
    entry_busqueda_codigo.pack(anchor="ne", side="left", padx=10, pady=10)

    boton_actualizar_consulta = ttk.Button(frame_busqueda, text="Actualizar", command= lambda: llenar_tabla_busqueda(entry_busqueda_codigo.get(), treeview_tabla_resultado_busqueda))
    boton_actualizar_consulta.pack(padx=10, pady=10)  

    
    treeview_tabla_resultado_busqueda = ttk.Treeview(frame_notebook2, columns=("id", "codigo", 
                                            "nombre", "stock", "precio"), show="headings")
    treeview_tabla_resultado_busqueda.configure(height=3)
    treeview_tabla_resultado_busqueda.pack(padx=10, pady=10)
    treeview_tabla_resultado_busqueda.heading("id", text="ID", anchor="center")
    treeview_tabla_resultado_busqueda.heading("codigo", text="codigo", anchor="center")
    treeview_tabla_resultado_busqueda.heading("nombre", text="Nombre", anchor="center")
    treeview_tabla_resultado_busqueda.heading("stock", text="Stock", anchor="center")
    treeview_tabla_resultado_busqueda.heading("precio", text="Precio", anchor="center")
    treeview_tabla_resultado_busqueda.column("id", width=50, anchor="center")
    treeview_tabla_resultado_busqueda.column("nombre", anchor="center")
    treeview_tabla_resultado_busqueda.column("codigo", width=150, anchor="center")
    treeview_tabla_resultado_busqueda.column("stock", width=50, anchor="center")
    treeview_tabla_resultado_busqueda.column("precio", width=100, anchor="center")  



    root.mainloop()


if __name__ == "__main__":
    main()

