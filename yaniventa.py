from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import sqlite3


ventana= Tk()
ventana.state('zoomed')
ventana.title("Programa de Yanina")
frameOpen=0
ventanaClose=0


def sacarFrame():
    if(frameOpen==1):
        frIngreso.pack_forget()
    elif(frameOpen==2):
        frPrincipal.pack_forget()
    elif(frameOpen==3):
        frStock.pack_forget()
    elif(frameOpen==4):
        frCompras.pack_forget()
    elif(frameOpen==5):
        frCompras.pack_forget()
    elif(frameOpen==6):
        frCompraRopa.pack_forget()
    elif(frameOpen==7):
        frConsultaCompra.pack_forget()
    elif(frameOpen==8):
        frVentas.pack_forget()
    elif(frameOpen==9):
        frVentas.pack_forget()
    elif(frameOpen==10):
        frVentaRopa.pack_forget()
    elif(frameOpen==11):
        frConsultaVenta.pack_forget()
    elif(frameOpen==12):
        frPago.pack_forget()
    elif(frameOpen==13):
        frCobro.pack_forget()
    elif(frameOpen==14):
        frpagos.pack_forget()
    elif(frameOpen==15):
        frSaldoCliente.pack_forget()
    elif(frameOpen==16):
        frSaldoProv.pack_forget()
        
def cerrarVentana():
    if(ventanaClose==1):
        ventanaModB.destroy()
    elif(ventanaClose==2):
        ventanalistar.destroy()
    elif(ventanaClose==3):
        ventanaNuevo.destroy()
    elif(ventanaClose==4):
        ventanalistarCliente.destroy()
    elif(ventanaClose==5):
        nuevoCliente.destroy()
    elif(ventanaClose==6):
        ventanalistarVta.destroy()

def center(toplevel): 
    toplevel.update_idletasks() 
    w = toplevel.winfo_screenwidth() 
    h = toplevel.winfo_screenheight() 
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x')) 
    x = w/2 - size[0]/2 
    y = h/2 - size[1]/2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

def frameSalir():
    ventana.destroy()

def listarproductosVta(a):

    global ventanalistarVta
    ventanalistarVta=Tk()
    global ventanaClose
    ventanaClose=6
    ventanalistarVta.config(bg="#F7A998")
    ventanalistarVta.title("Lista de Stock")
    ventanalistarVta.geometry("400x300")
    lbListar=Label(ventanalistarVta,text="Lista de productos",font=('Helvetica',15,"bold"),bg="#F7A998",fg="white")
    lbListar.place(x=100,y=10)
    global treelistarVta
    treelistarVta=ttk.Treeview(ventanalistarVta,style="miStyle.Treeview")
    treelistarVta.place(x=50,y=50)
    treelistarVta["columns"]=("one")
    treelistarVta.column("#0", width=100, minwidth=100,stretch=NO)
    treelistarVta.column("one", width=200, minwidth=200,stretch=NO)
    treelistarVta.heading("#0",text="Código")
    treelistarVta.heading("one", text="Producto")
    def pasarProdVenta(evento):
        global indiceVta
        indiceVta =((treelistarVta.index(treelistarVta.selection())+1),)
        print (indiceVta)
        if (a=="bagues"):
            conexion=sqlite3.connect("yanina.db")
            tabla = conexion.cursor()
            tabla.execute("SELECT * FROM StockBagues WHERE id=?",indiceVta)
            conexion.commit()
            datos = tabla.fetchall()
            tabla.close()
            print (datos)
            print (datos[0][1])
        if (a=="ropa"):
            conexion=sqlite3.connect("yanina.db")
            tabla = conexion.cursor()
            tabla.execute("SELECT * FROM StockRopa WHERE id=?",indiceVta)
            conexion.commit()
            datos = tabla.fetchall()
            tabla.close()
            print (datos)
            print (datos[0][1])
        entryCodVenta.config(state="normal")
        entryNombre.config(state="normal")
        entryCodVenta.delete(0,END)
        entryNombre.delete(0,END)
        entryCodVenta.insert(0,datos[0][0])
        entryNombre.insert(0,datos[0][1])
        entryCodVenta.config(state="readonly")
        entryNombre.config(state="readonly")
    treelistarVta.bind ("<<TreeviewSelect>>",pasarProdVenta)
    if(a=="bagues"):
        conexion=sqlite3.connect("yanina.db")
        cursor=conexion.cursor()
        cursor.execute("SELECT * FROM StockBagues")
        conexion.commit()
        productos=cursor.fetchall()
        for p in productos:
            nivel1=treelistarVta.insert("", "end", text=p[0],values=(p[1],p[2]))
    elif(a=="ropa"):
        conexion=sqlite3.connect("yanina.db")
        cursor=conexion.cursor()
        cursor.execute("SELECT * FROM StockRopa")
        conexion.commit()
        productos=cursor.fetchall()
        for p in productos:
            nivel1=treelistarVta.insert("", "end", text=p[0],values=(p[1],p[2]))
    conexion.close()
    center(ventanalistarVta)
    ventanalistarVta.mainloop()

def listarproductos(a):
    global ventanalistar
    ventanalistar=Tk()
    global ventanaClose
    ventanaClose=2
    ventanalistar.config(bg="#F7A998")
    ventanalistar.title("Lista de Stock")
    ventanalistar.geometry("400x300")
    lbListar=Label(ventanalistar,text="Lista de productos",font=('Helvetica',15,"bold"),bg="#F7A998",fg="white")
    lbListar.place(x=100,y=10)
    global treelistar
    treelistar=ttk.Treeview(ventanalistar,style="miStyle.Treeview")
    treelistar.place(x=50,y=50)
    treelistar["columns"]=("one")
    treelistar.column("#0", width=100, minwidth=100,stretch=NO)
    treelistar.column("one", width=200, minwidth=200,stretch=NO)
    treelistar.heading("#0",text="Código")
    treelistar.heading("one", text="Producto")
    def pasarProdCompra(evento):
        global indiceCompra
        indiceCompra =((treelistar.index(treelistar.selection())+1),)
        print (indiceCompra)
        if (a=="bagues"):
            conexion=sqlite3.connect("yanina.db")
            tabla = conexion.cursor()
            tabla.execute("SELECT * FROM StockBagues WHERE id=?",indiceCompra)
            conexion.commit()
            datos = tabla.fetchall()
            tabla.close()
            print (datos)
            print (datos[0][1])
        if (a=="ropa"):
            conexion=sqlite3.connect("yanina.db")
            tabla = conexion.cursor()
            tabla.execute("SELECT * FROM StockRopa WHERE id=?",indiceCompra)
            conexion.commit()
            datos = tabla.fetchall()
            tabla.close()
            print (datos)
            print (datos[0][1])
        entryCodCompra.config(state="normal")
        entryNombre.config(state="normal")
        entryCodVenta.delete(0,END)
        entryNombre.delete(0,END)
        entryCodCompra.insert(0,datos[0][0])
        entryNombre.insert(0,datos[0][1])
        entryCodCompra.config(state="readonly")
        entryNombre.config(state="readonly")
    treelistar.bind ("<<TreeviewSelect>>",pasarProdCompra)
    if(a=="bagues"):
        conexion=sqlite3.connect("yanina.db")
        cursor=conexion.cursor()
        cursor.execute("SELECT * FROM StockBagues")
        conexion.commit()
        productos=cursor.fetchall()
        for p in productos:
            nivel1=treelistar.insert("", "end", text=p[0],values=(p[1],p[2]))
    elif(a=="ropa"):
        conexion=sqlite3.connect("yanina.db")
        cursor=conexion.cursor()
        cursor.execute("SELECT * FROM StockRopa")
        conexion.commit()
        productos=cursor.fetchall()
        for p in productos:
            nivel1=treelistar.insert("", "end", text=p[0],values=(p[1],p[2]))
    conexion.close()
    center(ventanalistar)
    ventanalistar.mainloop()

#función para validar datos



#####################################################AQUI COMIENZA EL MÓDULO DE PAGOS############################################################################

"""def frameSaldoProv():
    sacarFrame()
    global frSaldoProv
    frSaldoProv=Frame(ventana)
    frSaldoProv.pack(expand=1,fill='both')
    global frameOpen
    frameOpen=16
    global imgFondoB
    imgFondoB=ImageTk.PhotoImage(Image.open("bagues22.png"))
    canvas = Canvas(frSaldoProv, width=2000, height=800)
    canvas.place(x=0,y=0)
    canvas.create_image(0,0,image=imgFondoB,anchor=NW)
    canvas.create_text(700,100, text="SALDO PROVEEDORES",font=('Helvetica',45,"underline","bold"),fill="#F34B2C")
    canvas.create_text(465,200, text="Número de proveedor:",font=('Helvetica',15,"bold"),fill="#F34B2C",anchor="w")
    canvas.create_text(465,235, text="Proveedor:",font=('Helvetica',15,"bold"),fill="#F34B2C",anchor="w")
    entryCodProv=Entry(frSaldoProv,width="5",font=('Helvetica',14))
    entryCodProv.place(x=680,y=185)
    entryNombreProv=Entry(frSaldoProv,width="20",font=('Helvetica',14),state="readonly")
    entryNombreProv.place(x=575,y=220)
    btVerCod=Button(frSaldoProv,text="Ver Cod",width='8',font=("Helvetica",12),bg="#F7A998")
    btVerCod.place(x=750,y=182)
    btVerSaldo=Button(frSaldoProv,text="Ver saldo",width='15',font=("Helvetica",15),bg="#F7A998")
    btVerSaldo.place(x=475,y=255)
    btMenuPagos=Button(frSaldoProv,text="Menu pagos",width='15',font=("Helvetica",15),bg="#F7A998",command=framePagos)
    btMenuPagos.place(x=675,y=255)
    listSaldo=Listbox(frSaldoProv,width=100,height=20)
    listSaldo.place (x=350,y=300)
"""
def frameSaldoCliente():
    sacarFrame()
    global frSaldoCliente
    frSaldoCliente=Frame(ventana)
    frSaldoCliente.pack(expand=1,fill='both')
    global frameOpen
    frameOpen=15
    global imgFondoB
    imgFondoB=ImageTk.PhotoImage(Image.open("bagues22.png"))
    canvas = Canvas(frSaldoCliente, width=2000, height=800)
    canvas.place(x=0,y=0)
    canvas.create_image(0,0,image=imgFondoB,anchor=NW)
    canvas.create_text(700,100, text="SALDO CLIENTES",font=('Helvetica',45,"underline","bold"),fill="#F34B2C")
    treelistarSaldos=ttk.Treeview(frSaldoCliente,style="miStyle.Treeview")
    treelistarSaldos.place(x=450,y=200)
    treelistarSaldos["columns"]=("one","two")
    treelistarSaldos.column("#0", width=100, minwidth=100,stretch=NO)
    treelistarSaldos.column("one", width=200, minwidth=200,stretch=NO)
    treelistarSaldos.column("two", width=200, minwidth=100,stretch=NO)
    treelistarSaldos.heading("#0",text="Código")
    treelistarSaldos.heading("one", text="Cliente")
    treelistarSaldos.heading("two", text="Saldo")
    conexion=sqlite3.connect("yanina.db")
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM Cliente")
    conexion.commit()
    clientes=cursor.fetchall()
    for c in clientes:
        print (c)
        nivel1=treelistarSaldos.insert("", "end", text=c[0],values=(c[1],c[2]))
    conexion.close()
    btMenuPagos=Button(frSaldoCliente,text="Menu Principal",width='15',font=("Helvetica",15),bg="#F7A998",command=framePrincipal)
    btMenuPagos.place(x=600,y=450)
    
    
"""def framePago():
    sacarFrame()
    global frpagos
    frpagos=Frame(ventana)
    frpagos.pack(expand=1,fill='both')
    global frameOpen
    frameOpen=14
    global imgFondoB
    imgFondoB=ImageTk.PhotoImage(Image.open("bagues22.png"))
    canvas = Canvas(frpagos, width=2000, height=800)
    canvas.place(x=0,y=0)
    canvas.create_image(0,0,image=imgFondoB,anchor=NW)
    canvas.create_text(700,100, text="P A G O S",font=('Helvetica',45,"underline","bold"),fill="#F34B2C")
    canvas.create_text(500,200, text="Carga de pago:",font=('Helvetica',15,"bold","underline"),fill="#F34B2C",anchor='w')
    canvas.create_text(500,235, text="Fecha(dd/mm/aaaa):",font=('Helvetica',15,"bold"),fill="#F34B2C",anchor="w")
    canvas.create_text(500,270, text="Número de proveedor:",font=('Helvetica',15,"bold"),fill="#F34B2C",anchor="w")
    canvas.create_text(500,305, text="Proveedor:",font=('Helvetica',15,"bold"),fill="#F34B2C",anchor="w")
    canvas.create_text(500,340, text="Saldo:",font=('Helvetica',15,"bold"),fill="#F34B2C",anchor="w")
    canvas.create_text(500,375, text="Monto:",font=('Helvetica',15,"bold"),fill="#F34B2C",anchor="w")
    entryFecha=Entry(frpagos,width="10",font=('Helvetica',14))
    entryFecha.place(x=695,y=220)
    entryCodProv=Entry(frpagos,width="5",font=('Helvetica',14))
    entryCodProv.place(x=720,y=255)
    entryNombreProv=Entry(frpagos,width="20",font=('Helvetica',14),state="readonly")
    entryNombreProv.place(x=610,y=290)
    btVerCod=Button(frpagos,text="Ver Cod",width='8',font=("Helvetica",12),bg="#F7A998")
    btVerCod.place(x=790,y=250)
    entrySaldo=Entry(frpagos,width='6',font=('Helvetica',14),state="readonly")
    entrySaldo.place(x=565,y=325)
    entryMonto=Entry(frpagos,width='6',font=('Helvetica',14))
    entryMonto.place(x=570,y=360)
    btPagar=Button(frpagos,text="Pagar",width='15',font=("Helvetica",15),bg="#F7A998")
    btPagar.place(x=400,y=420)
    btCancelar=Button(frpagos,text="Cancelar",width='15',font=("Helvetica",15),bg="#F7A998")
    btCancelar.place(x=600,y=420)
    btMenuPagos=Button(frpagos,text="Menu pagos",width='15',font=("Helvetica",15),bg="#F7A998",command=framePagos)
    btMenuPagos.place(x=800,y=420)
    
def frameCobro():
    sacarFrame()
    global frCobro
    frCobro=Frame(ventana)
    frCobro.pack(expand=1,fill='both')
    global frameOpen
    frameOpen=13
    global imgFondoB
    imgFondoB=ImageTk.PhotoImage(Image.open("bagues22.png"))
    canvas = Canvas(frCobro, width=2000, height=800)
    canvas.place(x=0,y=0)
    canvas.create_image(0,0,image=imgFondoB,anchor=NW)
    canvas.create_text(700,100, text="C O B R O S",font=('Helvetica',45,"underline","bold"),fill="#F34B2C")
    canvas.create_text(500,200, text="Carga de pago:",font=('Helvetica',15,"bold","underline"),fill="#F34B2C",anchor='w')
    canvas.create_text(500,235, text="Fecha(dd/mm/aaaa):",font=('Helvetica',15,"bold"),fill="#F34B2C",anchor="w")
    canvas.create_text(500,270, text="Número de cliente:",font=('Helvetica',15,"bold"),fill="#F34B2C",anchor="w")
    canvas.create_text(500,305, text="Cliente:",font=('Helvetica',15,"bold"),fill="#F34B2C",anchor="w")
    canvas.create_text(500,340, text="Saldo:",font=('Helvetica',15,"bold"),fill="#F34B2C",anchor="w")
    canvas.create_text(500,375, text="Monto:",font=('Helvetica',15,"bold"),fill="#F34B2C",anchor="w")
    entryFecha=Entry(frCobro,width="10",font=('Helvetica',14))
    entryFecha.place(x=695,y=220)
    entryCodCliente=Entry(frCobro,width="5",font=('Helvetica',14))
    entryCodCliente.place(x=680,y=255)
    entryNombreCliente=Entry(frCobro,width="20",font=('Helvetica',14),state="readonly")
    entryNombreCliente.place(x=575,y=290)
    btVerCod=Button(frCobro,text="Ver Cod",width='8',font=("Helvetica",12),bg="#F7A998")
    btVerCod.place(x=750,y=250)
    entrySaldo=Entry(frCobro,width='6',font=('Helvetica',14),state="readonly")
    entrySaldo.place(x=565,y=325)
    entryMonto=Entry(frCobro,width='6',font=('Helvetica',14))
    entryMonto.place(x=570,y=360)
    btCobrar=Button(frCobro,text="Cobrar",width='15',font=("Helvetica",15),bg="#F7A998")
    btCobrar.place(x=400,y=420)
    btCancelar=Button(frCobro,text="Cancelar",width='15',font=("Helvetica",15),bg="#F7A998")
    btCancelar.place(x=600,y=420)
    btMenuPagos=Button(frCobro,text="Menu pagos",width='15',font=("Helvetica",15),bg="#F7A998",command=framePagos)
    btMenuPagos.place(x=800,y=420)

def framePagos():
    sacarFrame()
    global frPago
    frPago=Frame(ventana)
    frPago.pack(expand=1,fill='both')
    global frameOpen
    frameOpen=12
    global imgFondoB
    imgFondoB=ImageTk.PhotoImage(Image.open("bagues22.png"))
    canvas = Canvas(frPago, width=2000, height=800)
    canvas.place(x=0,y=0)
    canvas.create_image(0,0,image=imgFondoB,anchor=NW)
    canvas.create_text(670,100, text="MÓDULO PAGOS",font=('Helvetica',45,"underline","bold"),fill="#F34B2C")
    btIngCobro=Button(frPago, text="Ingresar Cobro",width='20',font=('Helvetica',15),bg="#F7A998",command=frameCobro)
    btIngCobro.place(x=70,y=200)
    btIngPago=Button(frPago, text="Ingresar Pago",width='20',font=('Helvetica',15),bg="#F7A998",command=framePago)
    btIngPago.place(x=320,y=200)
    btSaldoCliente=Button(frPago, text="Saldo Clientes",width='20',font=('Helvetica',15),bg="#F7A998",command=frameSaldoCliente)
    btSaldoCliente.place(x=570,y=200)
    btSaldoProv=Button(frPago, text="Saldo Proveedores",width='20',font=('Helvetica',15),bg="#F7A998",command=frameSaldoProv)
    btSaldoProv.place(x=820,y=200)
    btMenu=Button(frPago, text="Menú Principal",width='20',font=('Helvetica',15),bg="#F7A998",command=framePrincipal)
    btMenu.place(x=1070,y=200)
"""
#####################################################AQUI COMIENZA EL MÓDULO DE VENTAS############################################################################

def consultaVenta():
    sacarFrame()
    global frConsultaVenta
    frConsultaVenta=Frame(ventana)
    frConsultaVenta.pack(expand=1,fill='both')
    global frameOpen
    frameOpen=11
    global imgFondoB
    imgFondoB=ImageTk.PhotoImage(Image.open("bagues22.png"))
    canvas = Canvas(frConsultaVenta, width=2000, height=800)
    canvas.place(x=0,y=0)
    canvas.create_image(0,0,image=imgFondoB,anchor=NW)
    canvas.create_text(700,100, text="MÓDULO VENTAS",font=('Helvetica',45,"underline","bold"),fill="#F34B2C")
    canvas.create_text(400,200, text="Desde(dd/mm/aaaa):",font=('Helvetica',15,"underline","bold"),fill="#F34B2C")
    canvas.create_text(800,200, text="Hasta(dd/mm/aaaa):",font=('Helvetica',15,"underline","bold"),fill="#F34B2C")
    entryDesde=Entry(frConsultaVenta,width="10",font=('Helvetica',14))
    entryDesde.place(x=500,y=187)
    entryHasta=Entry(frConsultaVenta,width="10",font=('Helvetica',14))
    entryHasta.place(x=900,y=187)
    btConsultar=Button(frConsultaVenta, text="Consultar",width='15',font=('Helvetica',15),bg="#F7A998")
    btConsultar.place(x=1010,y=300)
    listStock=Listbox(frConsultaVenta,width=100,height=20)
    listStock.place (x=370,y=240)
    btMenuVenta=Button(frConsultaVenta,text="Menu Ventas",width='15',font=("Helvetica",15),bg="#F7A998",command=frameVentas)
    btMenuVenta.place(x=1010,y=380)

def agregarClienteNuevo():
    entryCodCliente.config(state="normal")
    entryNombreCliente.config(state="normal")
    entryCodCliente.delete(0,END)
    entryCodCliente.insert(0,codNuevoCliente.get())
    entryNombreCliente.delete(0,END)
    entryNombreCliente.insert(0,nombreClienteNuevo.get())
    entryCodCliente.config(state="readonly")
    entryNombreCliente.config(state="readonly")
    cliente=(nombreClienteNuevo.get(),0)
    conexion=sqlite3.connect("yanina.db")
    cursor=conexion.cursor()
    cursor.execute("INSERT INTO Cliente (nombre,saldo) VALUES(?,?)",cliente)
    conexion.commit()
    conexion.close()

def clienteNuevo():
    global nuevoCliente
    nuevoCliente=Tk()
    global ventanaClose
    ventanaClose=5
    nuevoCliente.config(bg="#F7A998")
    nuevoCliente.title("Nuevo Cliente")
    nuevoCliente.geometry("600x300")
    center(nuevoCliente)
    lbCodigo=Label(nuevoCliente, text="Código de Cliente: ",font=('Helvetica',15),bg="#F7A998",fg="white")
    lbCodigo.place(x=10,y=50)
    global codNuevoCliente
    codNuevoCliente=Entry(nuevoCliente,width="5",font=('Helvetica',15))
    codNuevoCliente.place(x=300,y=50)
    conexion=sqlite3.connect("yanina.db")
    cursor=conexion.cursor()
    cursor.execute("SELECT id FROM Cliente")
    conexion.commit()
    datos=cursor.fetchall()
    conexion.close()
    idClienteNuevo=len (datos)+1
    codNuevoCliente.delete(0,END)
    codNuevoCliente.insert(0,idClienteNuevo)
    codNuevoCliente.config(state="readonly")
    lbCliente=Label(nuevoCliente,text="Nombre:",font=('Helvetica',15),bg="#F7A998",fg="white")
    lbCliente.place(x=175,y=80)
    global nombreClienteNuevo
    nombreClienteNuevo=Entry(nuevoCliente,width="20",font=('Helvetica',15))
    nombreClienteNuevo.place(x=300,y=80)
    btGuardar=Button(nuevoCliente,text="Guardar",width='10',font=('Helvetica',15),command=agregarClienteNuevo)
    btGuardar.place(x=120,y=210)
    btSalir=Button(nuevoCliente,text="Salir",width='10',font=('Helvetica',15),command=cerrarVentana)
    btSalir.place(x=350,y=210)
    nuevoCliente.mainloop()

def listarClientes():
    global ventanalistarCliente
    ventanalistarCliente=Tk()
    global ventanaClose
    ventanaClose=4
    ventanalistarCliente.config(bg="#F7A998")
    ventanalistarCliente.title("Lista de Clientes")
    ventanalistarCliente.geometry("400x300")
    lbListar=Label(ventanalistarCliente,text="Lista de clientes",font=('Helvetica',15,"bold"),bg="#F7A998",fg="white")
    lbListar.place(x=100,y=10)
    global treelistarClientes
    treelistarClientes=ttk.Treeview(ventanalistarCliente,style="miStyle.Treeview")
    treelistarClientes.place(x=50,y=50)
    treelistarClientes["columns"]=("one")
    treelistarClientes.column("#0", width=100, minwidth=100,stretch=NO)
    treelistarClientes.column("one", width=200, minwidth=200,stretch=NO)
    treelistarClientes.heading("#0",text="Código")
    treelistarClientes.heading("one", text="Cliente")
    def pasarCliente(evento):
        global indiceCliente
        indiceCliente =((treelistarClientes.index(treelistarClientes.selection())+1),)
        print (indiceCliente)
        conexion=sqlite3.connect("yanina.db")
        tabla = conexion.cursor()
        tabla.execute("SELECT * FROM Cliente WHERE id=?",indiceCliente)
        conexion.commit()
        datos = tabla.fetchall()
        tabla.close()
        print (datos)
        print (datos[0][1])
        entryCodCliente.config(state="normal")
        entryNombreCliente.config(state="normal")
        entryCodCliente.delete(0,END)
        entryNombreCliente.delete(0,END)
        entryCodCliente.insert(0,datos[0][0])
        entryNombreCliente.insert(0,datos[0][1])
        entryCodCliente.config(state="readonly")
        entryNombreCliente.config(state="readonly")
    treelistarClientes.bind ("<<TreeviewSelect>>",pasarCliente)
    conexion=sqlite3.connect("yanina.db")
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM Cliente")
    conexion.commit()
    clientes=cursor.fetchall()
    for c in clientes:
        print (c)
        nivel1=treelistarClientes.insert("", "end", text=c[0],values=(c[1],c[2]))
    conexion.close()
    center(ventanalistarCliente)
    ventanalistarCliente.mainloop()

carroVenta=[]
carropStockVta=[]

def condiciones():
    s=c.get()
    print(s)
    global condicionVenta
    if(s== 0):
        condicionVenta = "contado"
    elif(s== 1):
        condicionVenta = "cuenta corriente"

def terminarVenta(a):
    print(condicionVenta)
    print(carroVenta)
    if (a == "bagues"):
        for venta in carroVenta:
            venta.insert(4, condicionVenta)
            conexion = sqlite3.connect("yanina.db")
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO Ventas (fecha,codigo,nombre,detalle,condicion,cantidad,punitario,ptotal) VALUES(?,?,?,?,?,?,?,?)", venta)
            conexion.commit()
            conexion.close()
        conexion2 = sqlite3.connect("yanina.db")
        cursor2 = conexion2.cursor()
        cursor2.execute("SELECT id FROM StockBagues")
        conexion2.commit()
        datos = cursor2.fetchall()
        conexion2.close()
        idDeStock = []
        for dato in datos:
            idDeStock.append(dato[0])
        print(idDeStock)
        print(carropStockVta, " hola")
        for venta in carropStockVta:
            if venta[1] in idDeStock:
                idd = (venta[1],)
                extraerStock = sqlite3.connect("yanina.db")
                cursorExt = extraerStock.cursor()
                cursorExt.execute(
                    "SELECT cantidad FROM StockBagues WHERE id=?", idd)
                extraerStock.commit()
                stock = cursorExt.fetchall()
                print(stock)
                print(stock[0][0])
                extraerStock.close()
                stockNuevo = int(stock[0][0])-int(venta[0])
                venta[0] = stockNuevo
                conexion = sqlite3.connect("yanina.db")
                cursor = conexion.cursor()
                print(venta)
                cursor.execute(
                    "UPDATE StockBagues SET cantidad=? WHERE id=?", venta)
                conexion.commit()
                conexion.close()
    else:
        for venta in carroVenta:
            venta.insert(4, condicionVenta)
            conexion = sqlite3.connect("yanina.db")
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO Ventas (fecha,codigo,nombre,detalle,condicion,cantidad,punitario,ptotal) VALUES(?,?,?,?,?,?,?,?)", venta)
            conexion.commit()
            conexion.close()
        conexion2 = sqlite3.connect("yanina.db")
        cursor2 = conexion2.cursor()
        cursor2.execute("SELECT id FROM StockRopa")
        conexion2.commit()
        datos = cursor2.fetchall()
        conexion2.close()
        idDeStock = []
        for dato in datos:
            idDeStock.append(dato[0])
        print(idDeStock)
        print(carropStockVta, " hola")
        for venta in carropStockVta:
            if venta[1] in idDeStock:
                idd = (venta[1],)
                extraerStock = sqlite3.connect("yanina.db")
                cursorExt = extraerStock.cursor()
                cursorExt.execute(
                    "SELECT cantidad FROM StockRopa WHERE id=?", idd)
                extraerStock.commit()
                stock = cursorExt.fetchall()
                print(stock)
                print(stock[0][0])
                extraerStock.close()
                stockNuevo = int(stock[0][0])-int(venta[0])
                venta[0] = stockNuevo
                conexion = sqlite3.connect("yanina.db")
                cursor = conexion.cursor()
                print(venta)
                cursor.execute(
                    "UPDATE StockRopa SET cantidad=? WHERE id=?", venta)
                conexion.commit()
                conexion.close()
    if(condicionVenta=="cuenta corriente"):
        idCliente=int(entryCodVenta.get())
        idC=(idCliente,)
        extraerSaldo=sqlite3.connect("yanina.db")
        cursor3=extraerSaldo.cursor()
        cursor3.execute("SELECT saldo FROM Cliente WHERE id=?",idC)
        extraerSaldo.commit()
        saldoAnterior=cursor3.fetchall()
        extraerSaldo.close()
        saldoNuevo=float(saldoAnterior[0][0])-float(entryTotalVta.get())
        saldoActualizar=(saldoNuevo,idCliente,)
        conexion4=sqlite3.connect("yanina.db")
        cursor4=conexion4.cursor()
        cursor4.execute("UPDATE Cliente SET saldo=? WHERE id=?",saldoActualizar)
        conexion4.commit()
        conexion4.close()


    del carroVenta[:]
    del carropStockVta[:]
    for i in treeVenta.get_children():
        treeVenta.delete(i)

def agregarVenta():
    datos=[entryFechaVta.get(),entryCodCliente.get(),entryNombreCliente.get(),entryCodVenta.get(),entryNombre.get(),entryCantidadVta.get(),entryPrecioVta.get()]
    datos2=[entryCodCliente.get(), entryCodVenta.get(),entryCantidadVta.get(), entryPrecioVta.get()]

    b=0
    while (b==0):
        for a in datos:
            if (a==""):
                messagebox.showinfo("Error","Complete todos los campos")
                b=1
                break
            else:
                b=2
    if(b==1):
        print("no cumplió con los requisitos")
    elif(b==2):
        b2=0
        while (b2==0):
            for a in datos2:
                try:
                    if float(a):
                        b2=1
                except ValueError:
                    messagebox.showinfo("Error","Ingrese datos numéricos por favor")
                    b2=2
                    break
        if(b2==2):
            print("no cumplió con los requisitos")
        elif(b2==1):
            listaAgregarVta=[]
            listaAgregarVta.append(entryFechaVta.get())
            listaAgregarVta.append(int(entryCodCliente.get()))
            listaAgregarVta.append(entryNombreCliente.get())
            listaAgregarVta.append(entryNombre.get())
            listaAgregarVta.append(int(entryCantidadVta.get()))
            listaAgregarVta.append(float(entryPrecioVta.get()))
            subtotal=int(entryCantidadVta.get())*float(entryPrecioVta.get())
            subtotalInicial=float(entryTotalVta.get())
            subtotalNuevo=subtotalInicial+subtotal
            entryTotalVta.config(state="normal")
            entryTotalVta.delete(0,END)
            entryTotalVta.insert(0,subtotalNuevo)
            entryTotalVta.config(state="readonly")
            listaAgregarVta.append(subtotal)
            listapStockVta=[]
            listapStockVta.append(int(entryCantidadVta.get()))
            listapStockVta.append(int(entryCodVenta.get()))
            print (listaAgregarVta)
            carroVenta.append(listaAgregarVta)
            carropStockVta.append(listapStockVta)
            nivel1=treeVenta.insert("", "end", text=entryNombre.get(),values=(entryCantidadVta.get(),entryPrecioVta.get(),subtotal))
            entryCodVenta.delete(0,END)
            entryNombre.delete(0,END)
            entryCantidadVta.delete(0,END)
            entryPrecioVta.delete(0,END)

def ventaProducto(a):
    sacarFrame()
    global frVentas
    frVentas=Frame(ventana)
    frVentas.pack(expand=1,fill='both')
    global frameOpen
    frameOpen=9
    global imgFondoB
    imgFondoB=ImageTk.PhotoImage(Image.open("bagues22.png"))
    canvas = Canvas(frVentas, width=2000, height=800)
    canvas.place(x=0,y=0)
    canvas.create_image(0,0,image=imgFondoB,anchor=NW)
    canvas.create_text(700,100, text="VENTAS",font=('Helvetica',45,"underline","bold"),fill="#F34B2C")
    canvas.create_text(200,150, text="Carga de productos:",font=('Helvetica',15,"bold","underline"),fill="#F34B2C")
    canvas.create_text(100,185, text="Fecha(dd/mm/aaaa):",font=('Helvetica',15,"bold"),fill="#F34B2C",anchor="w")
    canvas.create_text(100,220, text="Número de cliente:",font=('Helvetica',15,"bold"),fill="#F34B2C",anchor="w")
    canvas.create_text(100,255, text="Cliente:",font=('Helvetica',15,"bold"),fill="#F34B2C",anchor="w")
    canvas.create_text(100,290, text="Código de producto:",font=('Helvetica',15,"bold"),fill="#F34B2C",anchor="w")
    canvas.create_text(100,325, text="Nombre del producto:",font=('Helvetica',15,"bold"),fill="#F34B2C",anchor="w")
    canvas.create_text(100,360, text="Cantidad de productos:",font=('Helvetica',15,"bold"),fill="#F34B2C",anchor="w")
    canvas.create_text(100,395, text="Precio unitario:",font=('Helvetica',15,"bold"),fill="#F34B2C",anchor="w")
    global entryFechaVta
    entryFechaVta=Entry(frVentas,width="10",font=('Helvetica',14))
    entryFechaVta.place(x=310,y=170)
    global entryCodCliente
    entryCodCliente=Entry(frVentas,width="5",font=('Helvetica',14),state="readonly")
    entryCodCliente.place(x=280,y=205)
    global entryNombreCliente
    entryNombreCliente=Entry(frVentas,width="20",font=('Helvetica',14),state="readonly")
    entryNombreCliente.place(x=180,y=240)
    btVerCodCliente=Button(frVentas,text="Ver Cod",width='8',font=("Helvetica",12),bg="#F7A998",command=listarClientes)
    btVerCodCliente.place(x=350,y=200)
    btNuevoCliente=Button(frVentas,text="Nuevo",width='8',font=("Helvetica",12),bg="#F7A998", command=clienteNuevo)
    btNuevoCliente.place(x=440,y=200)
    global entryCodVenta
    entryCodVenta=Entry(frVentas,width='5',font=('Helvetica',14),state="readonly")
    entryCodVenta.place(x=300,y=275)
    btVerCodVenta=Button(frVentas,text="Ver Cod",width='8',font=("Helvetica",12),bg="#F7A998",command=lambda:listarproductosVta(a))
    btVerCodVenta.place(x=370,y=275)
    global entryNombre
    entryNombre=Entry(frVentas,width='20',font=('Helvetica',14),state="readonly")
    entryNombre.place(x=310,y=310)
    global entryCantidadVta
    entryCantidadVta=Entry(frVentas,width='5',font=('Helvetica',14))
    entryCantidadVta.place(x=325,y=345)
    global entryPrecioVta
    entryPrecioVta=Entry(frVentas,width='5',font=('Helvetica',14))
    entryPrecioVta.place(x=250,y=380)
    global c
    c=IntVar()
    contado=Radiobutton(frVentas,text='Contado',value=0,variable=c,bg='#cdcac3',font=('Helvetica',15),command=condiciones)
    contado.place(x=750,y=400)
    cuentacorriente=Radiobutton(frVentas,text='Cta.Cte.',value=1,variable=c,bg='#cdcac3',font=('Helvetica',15),command=condiciones)
    cuentacorriente.place(x=900,y=400)
    btAgregarVenta=Button(frVentas,text="Agregar",width='15',font=("Helvetica",15),bg="#F7A998",command=agregarVenta)
    btAgregarVenta.place(x=150,y=470)
    canvas.create_text(700,150, text="Resumen:",font=('Helvetica',15,"bold","underline"),fill="#F34B2C")
    global treeVenta
    treeVenta=ttk.Treeview(frVentas,style="miStyle.Treeview")
    treeVenta.place(x=650,y=170)
    treeVenta["columns"]=("one","two","three")
    treeVenta.column("#0", width=280, minwidth=100,stretch=NO)
    treeVenta.column("one", width=100, minwidth=200,stretch=NO)
    treeVenta.column("two", width=100, minwidth=100,stretch=NO)
    treeVenta.column("three", width=80, minwidth=80,stretch=NO)
    treeVenta.heading("#0",text="Producto")
    treeVenta.heading("one", text="Cantidad")
    treeVenta.heading("two", text="Precio unit")
    treeVenta.heading("three", text="Subtotal")
    canvas.create_text(1060,415, text="TOTAL:",font=('Helvetica',15,"bold"),fill="#F34B2C")
    global entryTotalVta
    entryTotalVta=Entry(frVentas,width='8',font=('Helvetica',14))
    entryTotalVta.place(x=1110,y=400)
    entryTotalVta.insert(0,0)
    entryTotalVta.config(state="readonly")
    btVender=Button(frVentas,text="Vender",width='15',font=("Helvetica",15),bg="#F7A998",command=lambda:terminarVenta(a))
    btVender.place(x=610,y=450)
    btCancelar=Button(frVentas,text="Cancelar",width='15',font=("Helvetica",15),bg="#F7A998")
    btCancelar.place(x=810,y=450)
    btMenuVenta=Button(frVentas,text="Menu ventas",width='15',font=("Helvetica",15),bg="#F7A998",command=frameVentas)
    btMenuVenta.place(x=1010,y=450)

def frameVentas():
    sacarFrame()
    global frVentas
    frVentas=Frame(ventana)
    frVentas.pack(expand=1,fill='both')
    global frameOpen
    frameOpen=8
    global imgFondoB
    imgFondoB=ImageTk.PhotoImage(Image.open("bagues22.png"))
    canvas = Canvas(frVentas, width=2000, height=800)
    canvas.place(x=0,y=0)
    canvas.create_image(0,0,image=imgFondoB,anchor=NW)
    canvas.create_text(700,100, text="MÓDULO VENTAS",font=('Helvetica',45,"underline","bold"),fill="#F34B2C")
    btVentaNuevaB=Button(frVentas, text="Vender Bagués",width='20',font=('Helvetica',15),bg="#F7A998",command=lambda:ventaProducto("bagues"))
    btVentaNuevaB.place(x=200,y=200)
    btVentaNuevaR=Button(frVentas, text="Vender Ropa",width='20',font=('Helvetica',15),bg="#F7A998",command=lambda:ventaProducto("ropa"))
    btVentaNuevaR.place(x=450,y=200)
    btVentaConsulta=Button(frVentas, text="Consultar Ventas",width='20',font=('Helvetica',15),bg="#F7A998",command=consultaVenta)
    btVentaConsulta.place(x=700,y=200)
    btMenuBagues=Button(frVentas, text="Menú Principal",width='20',font=('Helvetica',15),bg="#F7A998",command=framePrincipal)
    btMenuBagues.place(x=950,y=200)
    
#####################################################AQUI COMIENZA EL MÓDULO DE COMPRAS############################################################################
def consultaCompra():
    sacarFrame()
    global frConsultaCompra
    frConsultaCompra=Frame(ventana)
    frConsultaCompra.pack(expand=1,fill='both')
    global frameOpen
    frameOpen=7
    global imgFondoB
    imgFondoB=ImageTk.PhotoImage(Image.open("bagues22.png"))
    canvas = Canvas(frConsultaCompra, width=2000, height=800)
    canvas.place(x=0,y=0)
    canvas.create_image(0,0,image=imgFondoB,anchor=NW)
    canvas.create_text(700,100, text="MÓDULO COMPRAS",font=('Helvetica',45,"underline","bold"),fill="#F34B2C")
    canvas.create_text(400,200, text="Desde(dd/mm/aaaa):",font=('Helvetica',15,"underline","bold"),fill="#F34B2C")
    canvas.create_text(800,200, text="Hasta(dd/mm/aaaa):",font=('Helvetica',15,"underline","bold"),fill="#F34B2C")
    entryDesde=Entry(frConsultaCompra,width="10",font=('Helvetica',14))
    entryDesde.place(x=500,y=187)
    entryHasta=Entry(frConsultaCompra,width="10",font=('Helvetica',14))
    entryHasta.place(x=900,y=187)
    btConsultar=Button(frConsultaCompra, text="Consultar",width='15',font=('Helvetica',15),bg="#F7A998")
    btConsultar.place(x=1010,y=300)
    listStock=Listbox(frConsultaCompra,width=100,height=20)
    listStock.place (x=370,y=240)
    btMenuCompra=Button(frConsultaCompra,text="Menu compras",width='15',font=("Helvetica",15),bg="#F7A998",command=frameCompras)
    btMenuCompra.place(x=1010,y=380)
carroCompra=[]
carropStock=[]
def terminarCompra(a):
    print(carroCompra)
    if (a=="bagues"):
        for compra in carroCompra:
            conexion=sqlite3.connect("yanina.db")
            cursor=conexion.cursor()
            cursor.execute("INSERT INTO ComprasBagues (fecha,codigo,producto,cantidad,punitario,ptotal) VALUES(?,?,?,?,?,?)",compra)
            conexion.commit()
            conexion.close()
        conexion2=sqlite3.connect("yanina.db")
        cursor2=conexion2.cursor()
        cursor2.execute("SELECT id FROM StockBagues")
        conexion2.commit()
        datos=cursor2.fetchall()
        conexion2.close()
        idDeStock=[]
        for dato in datos:
            idDeStock.append(dato[0])
        print (idDeStock)
        print(carropStock," hola")
        for compra in carropStock:
            if compra[3] in idDeStock:
                idd=(compra[3],)
                extraerStock=sqlite3.connect("yanina.db")
                cursorExt=extraerStock.cursor()
                cursorExt.execute("SELECT cantidad FROM StockBagues WHERE id=?",idd)
                extraerStock.commit()
                stock=cursorExt.fetchall()
                print (stock)
                print (stock[0][0])
                extraerStock.close()
                stockNuevo=int(stock[0][0])+int(compra[1])
                compra[1]=stockNuevo
                compra.pop(0)
                conexion=sqlite3.connect("yanina.db")
                cursor=conexion.cursor()
                print (compra)
                cursor.execute("UPDATE StockBagues SET cantidad=?,preciounitario=? WHERE id=?",compra)
                conexion.commit()
                conexion.close()
            else:
                compra.pop()
                print(compra)
                conexion=sqlite3.connect("yanina.db")
                cursor=conexion.cursor()
                cursor.execute("INSERT INTO StockBagues (nombre,cantidad,preciounitario) VALUES(?,?,?)",compra)
                conexion.commit()
                conexion.close()
    else:
        for compra in carroCompra:
            conexion=sqlite3.connect("yanina.db")
            cursor=conexion.cursor()
            cursor.execute("INSERT INTO ComprasRopa (fecha,codigo,producto,cantidad,punitario,ptotal) VALUES(?,?,?,?,?,?)",compra)
            conexion.commit()
            conexion.close()
        conexion2=sqlite3.connect("yanina.db")
        cursor2=conexion2.cursor()
        cursor2.execute("SELECT id FROM StockRopa")
        conexion2.commit()
        datos=cursor2.fetchall()
        conexion2.close()
        idDeStock=[]
        for dato in datos:
            idDeStock.append(dato[0])
        print (idDeStock)
        print(carropStock," hola")
        for compra in carropStock:
            if compra[3] in idDeStock:
                idd=(compra[3],)
                extraerStock=sqlite3.connect("yanina.db")
                cursorExt=extraerStock.cursor()
                cursorExt.execute("SELECT cantidad FROM StockRopa WHERE id=?",idd)
                extraerStock.commit()
                stock=cursorExt.fetchall()
                print (stock)
                print (stock[0][0])
                extraerStock.close()
                stockNuevo=int(stock[0][0])+int(compra[1])
                compra[1]=stockNuevo
                compra.pop(0)
                conexion=sqlite3.connect("yanina.db")
                cursor=conexion.cursor()
                print (compra)
                cursor.execute("UPDATE StockRopa SET cantidad=?,preciounitario=? WHERE id=?",compra)
                conexion.commit()
                conexion.close()
            else:
                compra.pop()
                print(compra)
                conexion=sqlite3.connect("yanina.db")
                cursor=conexion.cursor()
                cursor.execute("INSERT INTO StockRopa (nombre,cantidad,preciounitario) VALUES(?,?,?)",compra)
                conexion.commit()
                conexion.close()
    
    del carroCompra[:]
    del carropStock[:]
    for i in treeCompra.get_children():
            treeCompra.delete(i)

def agregarComprar():
    listaAgregar=[]
    listaAgregar.append(entryFecha.get())
    listaAgregar.append(int(entryCodCompra.get()))
    listaAgregar.append(entryNombre.get())
    listaAgregar.append(int(entryCantidad.get()))
    listaAgregar.append(int(entryPrecioCompra.get()))
    subtotal=int(entryCantidad.get())*int(entryPrecioCompra.get())
    listaAgregar.append(subtotal)
    listapStock=[]
    listapStock.append(entryNombre.get())
    listapStock.append(int(entryCantidad.get()))
    listapStock.append(int(entryPrecioCompra.get()))
    listapStock.append(int(entryCodCompra.get()))
    print (listaAgregar)
    carroCompra.append(listaAgregar)
    carropStock.append(listapStock)
    nivel1=treeCompra.insert("", "end", text=entryNombre.get(),values=(entryCantidad.get(),entryPrecioCompra.get(),subtotal))
    entryCodCompra.delete(0,END)
    entryNombre.delete(0,END)
    entryCantidad.delete(0,END)
    entryPrecioCompra.delete(0,END)
def agregarNuevo():
    entryCodCompra.config(state="normal")
    entryNombre.config(state="normal")
    entryCodCompra.delete(0,END)
    entryCodCompra.insert(0,codNuevo.get())
    entryNombre.delete(0,END)
    entryNombre.insert(0,prodNuevo.get())
    entryCantidad.delete(0,END)
    entryCantidad.insert(0,cantNuevo.get())
    entryPrecioCompra.delete(0,END)
    entryPrecioCompra.insert(0,precioNuevo.get())
    entryCodCompra.config(state="readonly")
    entryNombre.config(state="readonly")
    entryCantidad.config(state="readonly")
    entryPrecioCompra.config(state="readonly")

def productoNuevo(a):
    global ventanaNuevo
    ventanaNuevo=Tk()
    global ventanaClose
    ventanaClose=3
    ventanaNuevo.config(bg="#F7A998")
    ventanaNuevo.title("Nuevo Stock")
    ventanaNuevo.geometry("600x300")
    center(ventanaNuevo)
    lbCodigo=Label(ventanaNuevo, text="Código del producto: ",font=('Helvetica',15),bg="#F7A998",fg="white")
    lbCodigo.place(x=10,y=50)
    global codNuevo
    codNuevo=Entry(ventanaNuevo,width="5",font=('Helvetica',15))
    codNuevo.place(x=300,y=50)
    if(a=="bagues"):
        conexion=sqlite3.connect("yanina.db")
        cursor=conexion.cursor()
        cursor.execute("SELECT id FROM StockBagues")
        conexion.commit()
        datos=cursor.fetchall()
        conexion.close()
    elif(a=="ropa"):
        conexion=sqlite3.connect("yanina.db")
        cursor=conexion.cursor()
        cursor.execute("SELECT id FROM StockRopa")
        conexion.commit()
        datos=cursor.fetchall()
        conexion.close()
    idNuevo=len (datos)+1
    codNuevo.delete(0,END)
    codNuevo.insert(0,idNuevo)
    lbProducto=Label(ventanaNuevo,text="Producto:",font=('Helvetica',15),bg="#F7A998",fg="white")
    lbProducto.place(x=175,y=80)
    global prodNuevo
    prodNuevo=Entry(ventanaNuevo,width="20",font=('Helvetica',15))
    prodNuevo.place(x=300,y=80)
    lbCantidad=Label(ventanaNuevo,text="Cantidad",font=('Helvetica',15),bg="#F7A998",fg="white")
    lbCantidad.place(x=105,y=110)
    global cantNuevo
    cantNuevo=Entry(ventanaNuevo,width="20",font=('Helvetica',15))
    cantNuevo.place(x=300,y=110)
    lbprecio=Label(ventanaNuevo,text="Precio Unitario:",font=('Helvetica',15),bg="#F7A998",fg="white")
    lbprecio.place(x=110,y=140)
    global precioNuevo
    precioNuevo=Entry(ventanaNuevo,width="20",font=('Helvetica',15))
    precioNuevo.place(x=300,y=140)
    btGuardar=Button(ventanaNuevo,text="Guardar",width='10',font=('Helvetica',15),command=agregarNuevo)
    btGuardar.place(x=120,y=210)
    btSalir=Button(ventanaNuevo,text="Salir",width='10',font=('Helvetica',15),command=cerrarVentana)
    btSalir.place(x=350,y=210)
    ventanaNuevo.mainloop()

def compras(a):
    sacarFrame()
    global frCompras
    frCompras=Frame(ventana)
    frCompras.pack(expand=1,fill='both')
    global frameOpen
    frameOpen=5
    global imgFondoB
    imgFondoB=ImageTk.PhotoImage(Image.open("bagues22.png"))
    canvas = Canvas(frCompras, width=2000, height=800)
    canvas.place(x=0,y=0)
    canvas.create_image(0,0,image=imgFondoB,anchor=NW)
    canvas.create_text(700,100, text="COMPRAS",font=('Helvetica',45,"underline","bold"),fill="#F34B2C")
    canvas.create_text(200,150, text="Carga de productos:",font=('Helvetica',15,"bold","underline"),fill="#F34B2C")
    canvas.create_text(100,185, text="Fecha(dd/mm/aaaa):",font=('Helvetica',15,"bold"),fill="#F34B2C",anchor="w")
    canvas.create_text(100,220, text="Código de producto:",font=('Helvetica',15,"bold"),fill="#F34B2C",anchor="w")
    canvas.create_text(100,255, text="Nombre de producto:",font=('Helvetica',15,"bold"),fill="#F34B2C",anchor="w")
    canvas.create_text(100,290, text="Cantidad de productos:",font=('Helvetica',15,"bold"),fill="#F34B2C",anchor="w")
    canvas.create_text(100,325, text="Precio unitario:",font=('Helvetica',15,"bold"),fill="#F34B2C",anchor="w")
    global entryFecha
    entryFecha=Entry(frCompras,width="10",font=('Helvetica',14))
    entryFecha.place(x=310,y=170)
    global entryCodCompra
    entryCodCompra=Entry(frCompras,width="5",font=('Helvetica',14))
    entryCodCompra.place(x=300,y=205)
    global entryNombre
    entryNombre=Entry(frCompras,width="20",font=('Helvetica',14))
    entryNombre.place(x=305,y=240)
    global entryCantidad
    entryCantidad=Entry(frCompras,width='5',font=('Helvetica',14))
    entryCantidad.place(x=325,y=275)
    global entryPrecioCompra
    entryPrecioCompra=Entry(frCompras,width='8',font=('Helvetica',14))
    entryPrecioCompra.place(x=250,y=310)
    btVerCodCompra=Button(frCompras,text="Ver Cod",width='8',font=("Helvetica",12),bg="#F7A998",command=lambda: listarproductos(a))
    btVerCodCompra.place(x=370,y=200)
    btNuevoprod=Button(frCompras,text="Nuevo",width='8',font=("Helvetica",12),bg="#F7A998", command=lambda: productoNuevo(a))
    btNuevoprod.place(x=460,y=200)
    btAgregarCompra=Button(frCompras,text="Agregar",width='13',font=("Helvetica",15),bg="#F7A998",command=agregarComprar)
    btAgregarCompra.place(x=150,y=350)
    canvas.create_text(700,150, text="Resumen:",font=('Helvetica',15,"bold","underline"),fill="#F34B2C")
    global treeCompra
    treeCompra=ttk.Treeview(frCompras,style="miStyle.Treeview")
    treeCompra.place(x=650,y=170)
    treeCompra["columns"]=("one","two","three")
    treeCompra.column("#0", width=100, minwidth=100,stretch=NO)
    treeCompra.column("one", width=200, minwidth=200,stretch=NO)
    treeCompra.column("two", width=100, minwidth=100,stretch=NO)
    treeCompra.column("three", width=80, minwidth=80,stretch=NO)
    treeCompra.heading("#0",text="Producto")
    treeCompra.heading("one", text="Cantidad")
    treeCompra.heading("two", text="Precio unit")
    treeCompra.heading("three", text="Subtotal")
    canvas.create_text(1000,425, text="TOTAL:",font=('Helvetica',15,"bold"),fill="#F34B2C")
    entryTotal=Entry(frCompras,width='8',font=('Helvetica',14),state='readonly')
    entryTotal.place(x=1040,y=410)
    btComprar=Button(frCompras,text="Comprar",width='13',font=("Helvetica",15),bg="#F7A998",command=lambda: terminarCompra(a))
    btComprar.place(x=610,y=450)
    btCancelar=Button(frCompras,text="Cancelar",width='13',font=("Helvetica",15),bg="#F7A998")
    btCancelar.place(x=810,y=450)
    btMenuCompra=Button(frCompras,text="Menu compras",width='13',font=("Helvetica",15),bg="#F7A998",command=frameCompras)
    btMenuCompra.place(x=1010,y=450)
    
def frameCompras():
    sacarFrame()
    global frCompras
    frCompras=Frame(ventana)
    frCompras.pack(expand=1,fill='both')
    global frameOpen
    frameOpen=4
    global imgFondoB
    imgFondoB=ImageTk.PhotoImage(Image.open("bagues22.png"))
    canvas = Canvas(frCompras, width=2000, height=800)
    canvas.place(x=0,y=0)
    canvas.create_image(0,0,image=imgFondoB,anchor=NW)
    canvas.create_text(700,100, text="MÓDULO COMPRAS",font=('Helvetica',45,"underline","bold"),fill="#F34B2C")
    btCompraNuevaB=Button(frCompras, text="Comprar Bagués",width='20',font=('Helvetica',15),bg="#F7A998",command=lambda:compras("bagues"))
    btCompraNuevaB.place(x=200,y=200)
    btCompraNuevaR=Button(frCompras, text="Comprar Ropa",width='20',font=('Helvetica',15),bg="#F7A998",command=lambda:compras("ropa"))
    btCompraNuevaR.place(x=450,y=200)
    btCompraConsulta=Button(frCompras, text="Consultar Compras",width='20',font=('Helvetica',15),bg="#F7A998",command=consultaCompra)
    btCompraConsulta.place(x=700,y=200)
    btMenuBagues=Button(frCompras, text="Menú Principal",width='20',font=('Helvetica',15),bg="#F7A998",command=framePrincipal)
    btMenuBagues.place(x=950,y=200)
    
##################################################### AQUI COMIENZA EL MÓDULO DE STOCK ############################################################################    
def modificador(a):
    if(a=="bagues"):
        datos=(entryStockVerd.get(),entryCod.get())
        conexion=sqlite3.connect("yanina.db")
        cursor=conexion.cursor()
        cursor.execute("UPDATE StockBagues SET cantidad=? WHERE id=?",datos)
        conexion.commit()
        conexion.close()
        messagebox.showinfo("Modificar stock","Articulo modificado")
        cerrarVentana()

    elif(a=="ropa"):
        datos=(entryStockVerd.get(),entryCod.get())
        conexion=sqlite3.connect("yanina.db")
        cursor=conexion.cursor()
        cursor.execute("UPDATE StockRopa SET cantidad=? WHERE id=?",datos)
        conexion.commit()
        conexion.close()
        messagebox.showinfo("Modificar stock","Articulo modificado")
        cerrarVentana()
    frameListarStock(a)
def modificarStock(a):
    print (indice,"hola soy el indice a cambiar")
    global ventanaModB
    ventanaModB=Tk()
    global ventanaClose
    ventanaClose=1
    ventanaModB.config(bg="#F7A998")
    ventanaModB.title("Modificar Stock {}".format(a))
    ventanaModB.geometry("600x300")
    center(ventanaModB)
    lbCodigo=Label(ventanaModB, text="Ingrese código del producto: ",font=('Helvetica',15),bg="#F7A998",fg="white")
    lbCodigo.place(x=10,y=50)
    global entryCod
    entryCod=Entry(ventanaModB,width="5",font=('Helvetica',15))
    entryCod.place(x=300,y=50)
    lbProducto=Label(ventanaModB,text="Producto:",font=('Helvetica',15),bg="#F7A998",fg="white")
    lbProducto.place(x=175,y=80)
    entryProducto=Entry(ventanaModB,width="20",font=('Helvetica',15))
    entryProducto.place(x=300,y=80)
    lbStockAct=Label(ventanaModB,text="Stock en sistema:",font=('Helvetica',15),bg="#F7A998",fg="white")
    lbStockAct.place(x=105,y=110)
    entryStockAct=Entry(ventanaModB,width="20",font=('Helvetica',15))
    entryStockAct.place(x=300,y=110)
    lbStockVerd=Label(ventanaModB,text="Stock verdadero:",font=('Helvetica',15),bg="#F7A998",fg="white")
    lbStockVerd.place(x=110,y=140)
    if (a=="bagues"):
        conexion=sqlite3.connect("yanina.db")
        tabla = conexion.cursor()
        tabla.execute("SELECT * FROM StockBagues WHERE id=?",indice)
        conexion.commit()
        datos = tabla.fetchall()
        tabla.close()
        print (datos)
        print (datos[0][1])
    if (a=="ropa"):
        conexion=sqlite3.connect("yanina.db")
        tabla = conexion.cursor()
        tabla.execute("SELECT * FROM StockRopa WHERE id=?",indice)
        conexion.commit()
        datos = tabla.fetchall()
        tabla.close()
        print (datos)
        print (datos[0][1])
    entryCod.insert(0,datos[0][0])
    entryProducto.insert(0,datos[0][1])
    entryStockAct.insert(0,datos[0][2])
    entryCod.config(state="readonly")
    entryProducto.config(state="readonly")
    entryStockAct.config(state="readonly")
    global entryStockVerd
    entryStockVerd=Entry(ventanaModB,width="20",font=('Helvetica',15))
    entryStockVerd.place(x=300,y=140)
    btGuardar=Button(ventanaModB,text="Guardar",width='10',font=('Helvetica',15), command=lambda:modificador(a))
    btGuardar.place(x=120,y=210)
    btSalir=Button(ventanaModB,text="Salir",width='10',font=('Helvetica',15),command=cerrarVentana)
    btSalir.place(x=350,y=210)
    ventanaModB.mainloop()
def frameListarStock(a):
    if (a=="bagues"):
        for i in tree.get_children():
            tree.delete(i)
        conexion=sqlite3.connect("yanina.db")
        cursor=conexion.cursor()
        cursor.execute("SELECT * FROM StockBagues")
        conexion.commit()
        productos=cursor.fetchall()
        for p in productos:
            nivel1=tree.insert("", "end", text=p[0],values=(p[1],p[2],p[3]))
        conexion.close()
        btModifStockB=Button(frStock, text="Modificar Bagués",width='20',font=('Helvetica',15),bg="#F7A998",command=lambda:modificarStock("bagues"))
        btModifStockB.place(x=900,y=400)
    elif (a=="ropa"):
        for i in tree.get_children():
            tree.delete(i)
        conexion=sqlite3.connect("yanina.db")
        cursor=conexion.cursor()
        cursor.execute("SELECT * FROM StockRopa")
        conexion.commit()
        productos=cursor.fetchall()
        for p in productos:
            nivel1=tree.insert("", "end", text=p[0],values=(p[1],p[2],p[3]))
        conexion.close()
        btModifStockR=Button(frStock, text="Modificar Ropa",width='20',font=('Helvetica',15),bg="#F7A998",command=lambda:modificarStock("ropa"))
        btModifStockR.place(x=900,y=400)

#Stock de Bagués
def frameStock():
    sacarFrame()
    global frStock
    frStock=Frame(ventana)
    frStock.pack(expand=1,fill='both')
    global frameOpen
    frameOpen=3
    global imgFondoB
    imgFondoB=ImageTk.PhotoImage(Image.open("bagues22.png"))
    canvas = Canvas(frStock, width=2000, height=800)
    canvas.place(x=0,y=0)
    canvas.create_image(0,0,image=imgFondoB,anchor=NW)
    canvas.create_text(670,100, text="STOCK",font=('Helvetica',45,"underline","bold"),fill="#F34B2C")
    global treeStyle
    treeStyle=ttk.Style()
    treeStyle.configure("miStyle.Treeview",background="red")
    treeStyle.configure("miStyle.Treeview.Heading",font=("Helvetica",15),bg="red")
    global tree
    tree=ttk.Treeview(frStock,style="miStyle.Treeview")
    tree.place(x=370,y=300)
    tree["columns"]=("one","two","three")
    tree.column("#0", width=100, minwidth=100,stretch=NO)
    tree.column("one", width=200, minwidth=200,stretch=NO)
    tree.column("two", width=100, minwidth=100,stretch=NO)
    tree.column("three", width=80, minwidth=80,stretch=NO)
    tree.heading("#0",text="Código")
    tree.heading("one", text="Producto")
    tree.heading("two", text="Cantidad")
    tree.heading("three", text="Precio")
    def pasarproducto(evento):
        global indice
        indice =((tree.index(tree.selection())+1),)
        print (indice)
    tree.bind ("<<TreeviewSelect>>",pasarproducto)
    btStockB=Button(frStock, text="Stock Bagués",width='20',font=('Helvetica',15),bg="#F7A998",command=lambda:frameListarStock("bagues"))
    btStockB.place(x=300,y=200)
    btStockR=Button(frStock, text="Stock Ropa",width='20',font=('Helvetica',15),bg="#F7A998",command=lambda:frameListarStock("ropa"))
    btStockR.place(x=570,y=200)
    btMenuBagues=Button(frStock, text="Menú Principal",width='20',font=('Helvetica',15),bg="#F7A998",command=framePrincipal)
    btMenuBagues.place(x=900,y=200)

##################################################### VENTANA PRINCIPAL #######################################################################################

def framePrincipal():
    sacarFrame()
    global frPrincipal
    frPrincipal=Frame(ventana)
    frPrincipal.pack(expand=1,fill='both')
    global frameOpen
    frameOpen=2
    global imgFondoB
    imgFondoB=ImageTk.PhotoImage(Image.open("bagues22.png"))
    canvas = Canvas(frPrincipal, width=2000, height=800)
    canvas.place(x=0,y=0)
    canvas.create_image(0,0,image=imgFondoB,anchor=NW)
    canvas.create_text(670,100, text="YANINA",font=('Helvetica',45,"underline","bold"),fill="#F34B2C")
    btStockB=Button(frPrincipal, text="Stock",width='20',font=('Helvetica',15),bg="#F7A998",command=frameStock)
    btStockB.place(x=70,y=200)
    btComprasB=Button(frPrincipal, text="Compras",width='20',font=('Helvetica',15),bg="#F7A998",command=frameCompras)
    btComprasB.place(x=320,y=200)
    btVentasB=Button(frPrincipal, text="Ventas",width='20',font=('Helvetica',15),bg="#F7A998", command=frameVentas)
    btVentasB.place(x=570,y=200)
    btClientes = Button(frPrincipal, text="Clientes", width='20', font=('Helvetica', 15), bg="#F7A998", command=frameSaldoCliente)
    btClientes.place(x=820,y=200)
    btSalirB=Button(frPrincipal, text="Salir",width='20',font=('Helvetica',15),bg="#F7A998",command=frameSalir)
    btSalirB.place(x=1070,y=200)

#Frame de ingreso
def frameIngreso():
    sacarFrame()
    global frIngreso
    frIngreso=Frame(ventana)
    frIngreso.pack(expand=1,fill='both')
    global frameOpen
    frameOpen=1
    global imgFondo
    imgFondo=ImageTk.PhotoImage(Image.open("fondo3.png"))
    global lbFondo
    lbFondo=Label(frIngreso,image=imgFondo)
    lbFondo.place(x=0,y=0)
    global imgBagues
    imgBagues=ImageTk.PhotoImage(Image.open("bagues.jpg"))
    global btBagues
    btBagues=Button(frIngreso,image=imgBagues, command=framePrincipal)
    btBagues.place(x=250,y=225)
    global imgRopa
    imgRopa=ImageTk.PhotoImage(Image.open("ropa.png"))
    global btRopa
    btRopa=Button(frIngreso,image=imgRopa)
    btRopa.place(x=750,y=225)
frameIngreso()


ventana.mainloop()

