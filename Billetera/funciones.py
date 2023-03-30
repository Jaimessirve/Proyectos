"""LISTA DE ERRORES A CORREGIR
_Al crear cuenta nueva se debería abrir el archivo creado automáticamente
_Revisar la barra de herramientas
"""

from tkinter import *

# Create an instance of tkinter frame or window
root=Tk()
win = Frame(root)

# Set the size of the window
root.geometry("700x350")

def show_msg(event):
   label["text"]="Sale Up to 50% Off!"
   print("hola")

# Create a label widget
label=Label(win, text="Press Enter Key" ,font="TkMenuFont 20")
label.pack(pady=30)

# Bind the Enter Key to the window
win.bind('<Return>', show_msg)

root.mainloop()