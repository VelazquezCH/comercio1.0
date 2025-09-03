import tkinter as tk
from tkinter import messagebox



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
    

# print("desde validar")
# print(pasar_int(1010.256))