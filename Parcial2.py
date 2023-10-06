# Parcial 2 fisica 3
# descripcion: Realice una interfaz grafica para obtener propiedades físicas de tres tipos de capacitores de placas paralelas (placas paralelas, capacitor esferico, capacitor de cilintros)
# autores:  Francis Aguilar #222432
#           Angela García   #22869
# recursos: python 3.10
# fecha de entrega: 5/10/2023
# sin modificaciones
"""
ANTES DE CORRER EL PROGRAMA: 
asegurese de tener instalada la libreria de: sympy

"""

# librerias:
from tkinter import * 
from tkinter import messagebox
from math import sin, cos, tan 
from math import pi 
from sympy import *  #libreria para las derivadas e integrales

class app(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._root = Frame() #crea el frame principal
        self.geometry("1400x1400")
        self.title("🤑 Parcial 2 🤑")
        self.config(bg="#ffafcc")

        #objetos
        self.l1=Label(text="Altura (m):");self.l1.place(x=10,y=10); self.l1.config(bg="#ffc2d1")
        self.e1=Entry(self);self.e1.place(x=110,y=10)

        self.l2=Label(text="Longitud (m):");self.l2.place(x=10,y=50); self.l2.config(bg="#ffddd2")
        self.e2=Entry(self);self.e2.place(x=110,y=50)

        self.l3=Label(text="Carga (q):");self.l3.place(x=10,y=90); self.l3.config(bg="#ff8fab")
        self.e3=Entry(self);self.e3.place(x=110,y=90)
        
        #btn1= Button(self, text="Anillo", width=15,command=self.Anillo, bg="#ffc2d1");btn1.place(x=330,y=10)
        #btn2=Button(self, text="Disco", width=15, command=self.Disco, bg="#ffddd2");btn2.place(x=330,y=50)
        #btn3=Button(self, text="Linea de carga", width=15, command=self.LineaDeCarga,bg="#ff8fab");btn3.place(x=330,y=90)

        self.l4=Label(text="Placas Paralelas:");self.l4.place(x=10,y=130); self.l4.config(bg="#ffc2d1")
        self.l5=Label(text="");self.l5.place(x=10,y=170); self.l5.config(bg="#ff8fab")
        self.l6=Label(text="resultado anillo:");self.l6.place(x=10,y=210); self.l6.config(bg="#ffc2d1")
        self.l7=Label(text="");self.l7.place(x=10,y=250); self.l7.config(bg="#ff8fab")

        self.l8=Label(text="integral disco:");self.l8.place(x=10,y=290); self.l8.config(bg="#ffc2d1")
        self.l9=Label(text="");self.l9.place(x=10,y=320); self.l9.config(bg="#ff8fab")
        self.l10=Label(text="resultado disco:");self.l10.place(x=10,y=350); self.l10.config(bg="#ffc2d1")
        self.l11=Label(text="");self.l11.place(x=10,y=390); self.l11.config(bg="#ff8fab")

        self.l12=Label(text="integral linea de carga:");self.l12.place(x=10,y=450); self.l12.config(bg="#ffc2d1")
        self.l13=Label(text="");self.l13.place(x=10,y=480); self.l13.config(bg="#ff8fab")
        self.l14=Label(text="resultado linea de carga:");self.l14.place(x=10,y=510); self.l14.config(bg="#ffc2d1")
        self.l15=Label(text="");self.l15.place(x=10,y=550); self.l15.config(bg="#ff8fab")

        #canvas
        self.c1 = Canvas(self, width=800, height=500, bg="white")
        self.c1.place(x=450, y=150)
        self.c1.config(bg="misty rose")

    #pedir: dimensiones, voltaje y si es dielectrico

    #propiedades fisicas: 
    #capacitancia, carga del capacitor, energia almacenada del capacitor, 
    #si tiene dielectrico: valor de la carga libre y ligada

    def PlacasParalelas(self):
        pass

    def Esferico(self):
        pass

    def Cilindrico(self):
        pass

    def grafica(self):
        def f(x):
            return x**3 #x*tan(x), sin(x), cos(x)
        lix= -10#float(self.e1.get())
        lsx= 10 #float(self.e2.get())
        paso= (lsx-lix)/1000.0
        x = lix
        y = f(x)
        liy = lsy = y
        while (x<lsx):
            x = x+ paso
            y = f(x)
            if (y < liy):
                liy= y
            if ( y> lsy):
                lsy = y
        print(lix, lsx)
        def xp(vx):
            return int(( vx-lix) * self.c1.winfo_width() / (lsx-lix))
        def yp(vy):
            return int ((lsy - vy) * self.c1.winfo_height()/(lsy-liy))   
        self.c1.delete("all")
    
        #ejes
        self.c1.create_line(0, yp(0),self.c1.winfo_width(),yp(0), fill="red", width="2")
        self.c1.create_line(xp(0),0, xp(0), self.c1.winfo_height(), fill="red", width="2") 
        

    

    
        
   
        


    def limpiar(self):
        self.c1.delete("all")


            

    


app().mainloop()