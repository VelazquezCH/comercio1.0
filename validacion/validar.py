import tkinter as tk
from tkinter import messagebox

porcentaje = 10

def pasar_int(num):
    try:
        entero = int(num)
        return entero
    except ValueError:
        messagebox.showerror("Error", "Número incorrecto.")
        return
    

def format_currency(value):
    try:
        return f"$ {float(value):,.2f}"  # Permite decimales con dos dígitos
    except ValueError:
        return value
    
def calcular_con_transferencia(radiobutton_var, funcion, monto_entry, label_total, label_vuelto):
    total = funcion
    try:
        monto = float(monto_entry.get())
    except ValueError:
        monto = 0

    seleccion = radiobutton_var.get()

    if seleccion == 1:
        resultado = monto - total
        label_total.config(text=f"Total: ${total:,.2f}")
        label_vuelto.config(text=f"Vuelto: ${resultado:,.2f}")
        return total

    elif seleccion == 2:
        resultado_efectivo = total - monto
        resultado_transferencia = resultado_efectivo + (resultado_efectivo * porcentaje / 100)
        label_total.config(text=f"Total: ${total:,.2f}")
        label_vuelto.config(text=f"Transferencia: ${resultado_transferencia:,.2f}")
        return resultado_efectivo, resultado_transferencia

    elif seleccion == 3:
        resultado_transferencia = total + (total * porcentaje / 100)
        label_total.config(text=f"Total: ${total:,.2f}")
        label_vuelto.config(text=f"Transferencia: ${resultado_transferencia:,.2f}")
        return 0, resultado_transferencia
# print("desde validar")
# print(pasar_int(1010.256))