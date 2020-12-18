from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3


def validarFloat(numero):
    b=0
    while (b==0):
        for a in numero:
            if (a==""):
                messagebox.showinfo("Error","Complete todos los campos")
                b=1
                break
            else:
                try:
                    if float(a):
                        b=2
                except ValueError:
                    messagebox.showinfo("Error","Ingrese datos numéricos por favor")
                    b=1
                    break
    if(b==1):
        print("no cumplió con los requisitos")
    elif(b==2):
        print("Requisitos correctos")

ventana=Tk()
ventana.geometry("400x400")
ventana.config(bg="blue")
entry=Entry(ventana, width="10")
entry.place(x=10,y=20)
entry2=Entry(ventana, width="10")
entry2.place(x=10,y=40)

boton=Button(ventana,text="probar", command=lambda:validarFloat([entry.get(),entry2.get()]))
boton.place(x=10,y=60)


ventana.mainloop()
