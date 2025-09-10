import mysql.connector
from tkinter import ttk
import tkinter as tk
from tkcalendar import DateEntry




def estadistica():
    def tomar_fecha():
        if tabla_estadistica.get_children():
            for item in tabla_estadistica.get_children():
                tabla_estadistica.delete(item)
        fec_inicio = f"{fecha_inicio.get()} 00:00:00"
        fec_hasta = f"{fecha_hasta.get()} 23:59:59"

        cursor.execute("""SELECT 
        p.nombre AS nombre_producto,
            SUM(vp.cantidad) AS total_vendido
        FROM 
            venta_producto vp
        JOIN 
            ventas v ON vp.ID_venta = v.ID_venta
        LEFT JOIN 
            productos p ON vp.ID_producto = p.ID_producto
        WHERE 
            v.fecha BETWEEN %s AND %s
        GROUP BY 
            vp.ID_producto, p.nombre ORDER BY total_vendido DESC;""", (fec_inicio, fec_hasta)
        )
        datos = cursor.fetchall()
        for nombre, cantidad in datos:  
            tabla_estadistica.insert("", tk.END, values=(nombre, cantidad))

    conn = mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        passwd = "juanolijaz",
        database = "laura"
    )
    cursor = conn.cursor()

    

    root = tk.Tk()
    root.title("Estadistica por producto")
    root.geometry("600x500")
    root.resizable(True,True)

    #--------------- INGRESAR FECHA ------------------
    frame_fecha = tk.Frame(root)
    frame_fecha.pack(pady=20)

    label_fecha = tk.Label(frame_fecha, text="Fecha desde:")
    label_fecha.grid(row=0, column=0)
    fecha_inicio = DateEntry(frame_fecha, width=12, background='darkblue',foreground='white', borderwidth=2, year=2025, date_pattern='yyyy-mm-dd')
    fecha_inicio.grid(row=0,column=1, padx=20, pady=10)

    label_fecha_hasta = tk.Label(frame_fecha, text="Fecha desde:")
    label_fecha_hasta.grid(row=0, column=2)
    fecha_hasta = DateEntry(frame_fecha, date_pattern='yyyy-mm-dd')
    fecha_hasta.grid(row=0,column=3, padx=20, pady=10)


    

    #--------------- Frame titulo --------------------
    frame_titulo = tk.Frame(root)
    frame_titulo.pack(padx=10)

    label_titulo = tk.Label(frame_titulo,text="Estadistica de productos vendidos", font=("Arial", 16, "bold"))
    label_titulo.pack()

    frame_tabla = tk.Frame(root)
    frame_tabla.pack(padx=20, pady=10, fill="both", expand=True)

    tabla_estadistica = ttk.Treeview(frame_tabla, columns=("nombre", "cantidad"), show="headings")

    tabla_estadistica.heading("nombre", text="Nombre producto")
    tabla_estadistica.heading("cantidad", text="Cantidad vendida")
    tabla_estadistica.column("nombre", width=150)
    tabla_estadistica.column("cantidad", width=80)
    tabla_estadistica.pack(side="left", fill="both", expand=True)

    

    frame_boton = tk.Frame(root)
    frame_boton.pack(padx=10, pady=20)
    boton_buscar = tk.Button(frame_boton, text="Buscar", command=tomar_fecha)
    boton_buscar.pack(padx=10, pady=20)

    

    root.mainloop()
    cursor.close()
    conn.close()