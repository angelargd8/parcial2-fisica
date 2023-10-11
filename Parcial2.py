# Parcial 2 fisica 3
# descripcion: Realice una interfaz grafica para obtener propiedades físicas de tres tipos de capacitores de placas paralelas (placas paralelas, capacitor esferico, capacitor de cilintros)
# autores:  Francis Aguilar #222432
#           Angela García   #22869
# recursos: python 3.10
# fecha de entrega: 9/10/2023
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
from math import log
from tkinter.ttk import Combobox 
#from sympy import *  #libreria para las derivadas e integrales

class app(Tk):
    def __init__(self): 
        Tk.__init__(self)
        self._root = Frame() #crea el frame principal
        self.geometry("250x250")
        self.title("🤑 Parcial 2 🤑")
        self.config(bg="#ffafcc")
        self.l=Label(text=" Elija una de las variables: ");self.l.place(x=20,y=20); self.l.config(bg="#ffc2d1")
        self.caja = Combobox(self, state="readonly",values=["Placas paralelas", "Esferico", "Cilindrico"], width=20)
        self.caja.place(x=20, y =50)
        
        #self.ld=Label(text="Tendra dielectrico?");self.ld.place(x=10,y=70); self.ld.config(bg="#ffc2d1")
        #self.caja2 = Combobox(self,state="readonly",values=["SI", "NO"])
        #self.caja2.place(x=10, y =100)

        #self.lv=Label(text="Ingrese el voltaje");self.lv.place(x=10,y=130); self.lv.config(bg="#ffc2d1")
        #self.ev=Entry(self);self.ev.place(x=10,y=160)

        self.b = Button(self, text = "Crear",command= self.llamar, width=20, bg="#ff8fab"); self.b.place(x=10, y =190)



    def llamar(self): # para llamar a las diferentes pantallas
        if(self.caja.get()=="Placas paralelas"):
            self.PlacasGUI()
        elif (self.caja.get()=="Esferico"):
            self.EsfericoGUI()
        else:
            self.CilindricoGUI()



    def PlacasGUI(self):

        self.ventana = Toplevel(self)
        self.ventana.geometry("1400x1400")
        self.ventana.config(bg="#ffafcc")
        #objetos

        self.l1=Label(self.ventana,text="Distancia entre placas(m):");self.l1.place(x=10,y=10); self.l1.config(bg="#ffc2d1")
        self.e1=Entry(self.ventana);self.e1.place(x=160,y=10)

        self.l2=Label(self.ventana,text="Largo (m):");self.l2.place(x=10,y=50); self.l2.config(bg="#ffddd2")
        self.e2=Entry(self.ventana);self.e2.place(x=160,y=50)

        self.l4=Label(self.ventana,text="ancho (m):");self.l4.place(x=10,y=90); self.l4.config(bg="#ff8fab")
        self.e4=Entry(self.ventana);self.e4.place(x=160,y=90)

        self.l3=Label(self.ventana,text="voltaje (V):");self.l3.place(x=10,y=130); self.l3.config(bg="#f08080")
        self.e3=Entry(self.ventana);self.e3.place(x=160,y=130)
        
        self.btn1= Button(self.ventana, text="Placas Paralelas", width=35,command=self.PlacasParalelas, bg="#ffc2d1");self.btn1.place(x=350,y=10)
        self.btn2= Button(self.ventana, text="Placas Paralelas con dielectrico a la mitad", width=35,command=self.PlacasParalelasDielectricoMitad, bg="#ffb3c6");self.btn2.place(x=350,y=40)
        self.btn3= Button(self.ventana, text="Placas Paralelas con dielectrico completo", width=35,command=self.PlacasParalelasDielectricoCompleto, bg="#ff8fab");self.btn3.place(x=350,y=70)       
        
        #self.l5=Label(self.ventana, text="");self.l5.place(x=10,y=170); self.l5.config(bg="#ff8fab")
        self.l6=Label(self.ventana, text="capacitancia (F):");self.l6.place(x=10,y=170); self.l6.config(bg="#ffc2d1")
        self.l7=Label(self.ventana, text="");self.l7.place(x=10,y=210); self.l7.config(bg="#ff8fab")

        self.l8=Label(self.ventana, text="");self.l8.place(x=10,y=250); self.l8.config(bg="#ffc2d1")
        self.l9=Label(self.ventana, text="");self.l9.place(x=10,y=290); self.l9.config(bg="#ff8fab")
        self.l10=Label(self.ventana, text="");self.l10.place(x=10,y=320); self.l10.config(bg="#ffc2d1")
        self.l11=Label(self.ventana, text="");self.l11.place(x=10,y=350); self.l11.config(bg="#ff8fab")
        self.l12=Label(self.ventana, text="");self.l12.place(x=10,y=390); self.l12.config(bg="#ffc2d1")
        self.l13=Label(self.ventana, text="");self.l13.place(x=10,y=430); self.l13.config(bg="#ff8fab")
        self.l14=Label(self.ventana, text="");self.l14.place(x=10,y=470); self.l14.config(bg="#ffc2d1")
        self.l15=Label(self.ventana, text="");self.l15.place(x=10,y=510); self.l15.config(bg="#ff8fab")
        self.l16=Label(self.ventana, text="");self.l16.place(x=10,y=550); self.l16.config(bg="#ffc2d1")
        self.l17=Label(self.ventana, text="");self.l17.place(x=10,y=590); self.l17.config(bg="#ff8fab")

        #canvas
        self.c1 = Canvas(self.ventana, width=800, height=500, bg="white")
        self.c1.place(x=350, y=150)
        self.c1.config(bg="misty rose")


    def EsfericoGUI(self):
        self.ventana2 = Toplevel(self)
        self.ventana2.geometry("1400x1400")
        self.ventana2.config(bg="#ffafcc")
        #objetos

        self.l1=Label(self.ventana2,text="Radio A interno (m):");self.l1.place(x=10,y=10); self.l1.config(bg="#ffc2d1")
        self.e1=Entry(self.ventana2);self.e1.place(x=160,y=10)

        self.l2=Label(self.ventana2,text="Radio B externo (m):");self.l2.place(x=10,y=50); self.l2.config(bg="#ffddd2")
        self.e2=Entry(self.ventana2);self.e2.place(x=160,y=50)

        self.l3=Label(self.ventana2,text="voltaje (V):");self.l3.place(x=10,y=90); self.l3.config(bg="#ff8fab")
        self.e3=Entry(self.ventana2);self.e3.place(x=160,y=90)
        
        self.btn1= Button(self.ventana2, text="Capacitor esférico", width=35,command=self.Esferico, bg="#ffc2d1");self.btn1.place(x=350,y=10)
        self.btn2= Button(self.ventana2, text="Capacitor esférico con dielectrico a la mitad", width=35,command=self.EsfericoMitad, bg="#ffb3c6");self.btn2.place(x=350,y=40)
        self.btn3= Button(self.ventana2, text="Capacitor esférico con dielectrico completo", width=35,command=self.EsfericoCompleto, bg="#ff8fab");self.btn3.place(x=350,y=70)       
        
        #self.l5=Label(self.ventana, text="");self.l5.place(x=10,y=170); self.l5.config(bg="#ff8fab")
        self.l6=Label(self.ventana2, text="capacitancia (F):");self.l6.place(x=10,y=170); self.l6.config(bg="#ffc2d1")
        self.l7=Label(self.ventana2, text="");self.l7.place(x=10,y=210); self.l7.config(bg="#ff8fab")
        self.l8=Label(self.ventana2, text="carga del capacitor");self.l8.place(x=10,y=250); self.l8.config(bg="#ffc2d1")
        self.l9=Label(self.ventana2, text="");self.l9.place(x=10,y=290); self.l9.config(bg="#ff8fab")
        self.l10=Label(self.ventana2, text="energía almacenada");self.l10.place(x=10,y=320); self.l10.config(bg="#ffc2d1")
        self.l11=Label(self.ventana2, text="");self.l11.place(x=10,y=350); self.l11.config(bg="#ff8fab")
        self.l12=Label(self.ventana2, text="");self.l12.place(x=10,y=390); self.l12.config(bg="#ffc2d1")
        self.l13=Label(self.ventana2, text="");self.l13.place(x=10,y=430); self.l13.config(bg="#ff8fab")
        self.l14=Label(self.ventana2, text="");self.l14.place(x=10,y=470); self.l14.config(bg="#ffc2d1")
        self.l15=Label(self.ventana2, text="");self.l15.place(x=10,y=510); self.l15.config(bg="#ff8fab")
        self.l16=Label(self.ventana2, text="");self.l16.place(x=10,y=550); self.l16.config(bg="#ffc2d1")
        self.l17=Label(self.ventana2, text="");self.l17.place(x=10,y=590); self.l17.config(bg="#ff8fab")

        self.l18=Label(self.ventana2, text="");self.l18.place(x=170,y=170); self.l18.config(bg="#ffc2d1")
        self.l19=Label(self.ventana2, text="");self.l19.place(x=170,y=210); self.l19.config(bg="#ff8fab")
        self.l20=Label(self.ventana2, text="");self.l20.place(x=170,y=250); self.l20.config(bg="#ffc2d1")
        self.l21=Label(self.ventana2, text="");self.l21.place(x=170,y=290); self.l21.config(bg="#ff8fab")
        self.l22=Label(self.ventana2, text="");self.l22.place(x=170,y=320); self.l22.config(bg="#ffc2d1")
        self.l23=Label(self.ventana2, text="");self.l23.place(x=170,y=360); self.l23.config(bg="#ff8fab")
        #canvas
        self.c1 = Canvas(self.ventana2, width=800, height=500, bg="white")
        self.c1.place(x=370, y=150)
        self.c1.config(bg="misty rose")

    def CilindricoGUI(self):
        self.ventana3 = Toplevel(self)
        self.ventana3.geometry("1400x1400")
        self.ventana3.config(bg="#ffafcc")
        #objetos

        self.l1=Label(self.ventana3,text="Radio A interno (m):");self.l1.place(x=10,y=10); self.l1.config(bg="#ffc2d1")
        self.e1=Entry(self.ventana3);self.e1.place(x=160,y=10)

        self.l2=Label(self.ventana3,text="Radio B externo (m):");self.l2.place(x=10,y=50); self.l2.config(bg="#ffddd2")
        self.e2=Entry(self.ventana3);self.e2.place(x=160,y=50)

        self.l3=Label(self.ventana3,text="largo (m):");self.l3.place(x=10,y=90); self.l3.config(bg="#ff8fab")
        self.e3=Entry(self.ventana3);self.e3.place(x=160,y=90)

        self.l4=Label(self.ventana3,text="voltaje (V):");self.l4.place(x=10,y=130); self.l4.config(bg="#f08080")
        self.e4=Entry(self.ventana3);self.e4.place(x=160,y=130)
        
        self.btn1= Button(self.ventana3, text="Capacitor cilindrico", width=35,command=self.Cilindrico, bg="#ffc2d1");self.btn1.place(x=350,y=10)
        self.btn2= Button(self.ventana3, text="Capacitor cilindrico con dielectrico a la mitad", width=35,command=self.CilindricoMitad, bg="#ffb3c6");self.btn2.place(x=350,y=40)
        self.btn3= Button(self.ventana3, text="Capacitor cilindrico con dielectrico completo", width=35,command=self.CilindricoCompleto, bg="#ff8fab");self.btn3.place(x=350,y=70)       
        
        #self.l5=Label(self.ventana, text="");self.l5.place(x=10,y=170); self.l5.config(bg="#ff8fab")
        self.l6=Label(self.ventana3, text="capacitancia (F):");self.l6.place(x=10,y=170); self.l6.config(bg="#ffc2d1")
        self.l7=Label(self.ventana3, text="");self.l7.place(x=10,y=210); self.l7.config(bg="#ff8fab")
        self.l8=Label(self.ventana3, text="carga del capacitor");self.l8.place(x=10,y=250); self.l8.config(bg="#ffc2d1")
        self.l9=Label(self.ventana3, text="");self.l9.place(x=10,y=290); self.l9.config(bg="#ff8fab")
        self.l10=Label(self.ventana3, text="energia almacenada");self.l10.place(x=10,y=320); self.l10.config(bg="#ffc2d1")
        self.l11=Label(self.ventana3, text="");self.l11.place(x=10,y=350); self.l11.config(bg="#ff8fab")
        self.l12=Label(self.ventana3, text="");self.l12.place(x=10,y=390); self.l12.config(bg="#ffc2d1")
        self.l13=Label(self.ventana3, text="");self.l13.place(x=10,y=430); self.l13.config(bg="#ff8fab")
        self.l14=Label(self.ventana3, text="");self.l14.place(x=10,y=470); self.l14.config(bg="#ffc2d1")
        self.l15=Label(self.ventana3, text="");self.l15.place(x=10,y=510); self.l15.config(bg="#ff8fab")
        self.l16=Label(self.ventana3, text="");self.l16.place(x=10,y=550); self.l16.config(bg="#ffc2d1")
        self.l17=Label(self.ventana3, text="");self.l17.place(x=10,y=590); self.l17.config(bg="#ff8fab")
        self.l18=Label(self.ventana3, text="");self.l18.place(x=170,y=170); self.l18.config(bg="#ffc2d1")
        self.l19=Label(self.ventana3, text="");self.l19.place(x=170,y=210); self.l19.config(bg="#ff8fab")
        self.l20=Label(self.ventana3, text="");self.l20.place(x=170,y=250); self.l20.config(bg="#ffc2d1")
        self.l21=Label(self.ventana3, text="");self.l21.place(x=170,y=290); self.l21.config(bg="#ff8fab")
        self.l22=Label(self.ventana3, text="");self.l22.place(x=170,y=320); self.l22.config(bg="#ffc2d1")
        self.l23=Label(self.ventana3, text="");self.l23.place(x=170,y=360); self.l23.config(bg="#ff8fab")
        
        #canvas
        self.c1 = Canvas(self.ventana3, width=800, height=500, bg="white")
        self.c1.place(x=350, y=150)
        self.c1.config(bg="misty rose")



    #pedir: dimensiones, voltaje y si es dielectrico
    #propiedades fisicas: 
    #capacitancia, carga del capacitor, energia almacenada del capacitor, 
    #si tiene dielectrico: valor de la carga libre y ligada

    def PlacasParalelas(self):
        """
        Ecuaciones utiles: 
        C= E0*(A/d)
        C=Q/Vab
        E= sigma/E0
        E = Q/E0A
        """
        try:

            self.EpsilonCero = 8.85*10**-12
            self.longitud= float(self.e2.get())
            self.distancia= float(self.e1.get())
            self.ancho= float(self.e4.get())

            self.area = self.longitud*self.ancho
            if (self.longitud > 0 and self.distancia > 0 and  self.ancho > 0):
                #-----limpiar canvas-----
                self.limpiar()
                #-----calculo de capacitancia------
                """
                C= E0*(A/d)
                """
                self.Capacitancia= (self.EpsilonCero * self.area )/self.distancia
                self.l7.config(text=str( self.Capacitancia))

                #------carga en cada placa------
                """
                C=Q/Vab 
                Q=C*Vab
                """
                self.voltaje= float(self.e3.get())
                self.carga= self.Capacitancia *  self.voltaje   
                self.l8.config(text="carga del capacitor (C):")
                self.l9.config(text=str(self.carga))

                #------energia------
                """
                E= (1/2)*CV^2
                """
                self.Energia = (1/2)*(self.Capacitancia*(self.voltaje**2) )
                self.l10.config(text="energia almacenada (J):")
                self.l11.config(text=str(self.Energia))

                self.l12.config(text=" ")
                self.l13.config(text=" ")
                self.l14.config(text=" ")
                self.l15.config(text=" ")
                self.l16.config(text=" ")
                self.l17.config(text=" ")

                #------ parte de la grafica -----------   
                self.c1.create_rectangle((self.c1.winfo_width()-(200*self.longitud) ) / 2, (self.c1.winfo_height()- (90*self.ancho) )/2,(self.c1.winfo_width()+(200*self.longitud) )/2 , (self.c1.winfo_height()-(90) )/2, outline='red', width="3")
                
                self.c1.create_rectangle(((self.c1.winfo_width()-(200*self.longitud) ) / 2 ), ((self.c1.winfo_height()- (90*self.ancho) )/2)+ (100*self.distancia),(self.c1.winfo_width()+(200*self.longitud) )/2 , (self.c1.winfo_height()-(90) )/2 + (100*self.distancia), outline='red', width="3")



            else: 
                messagebox.showerror("Error", "Ingrese valores validos para la distancia y longitud")
        except Exception as msg: 
            messagebox.showerror("error", "asegurese de ingresar un número válido y todos los valores ")
                       

    def PlacasParalelasDielectricoMitad(self):
        """
        Ecuaciones utiles: 
        C= (K*E0*A) / 2d
        C= E0*(A/2d)
        Q= C*V
        E= (1/2)*CV^2
        E= (((1/2*C0*V^2)/2) + ((1/2*C*(V/K)^2)/2))

        """
        try:

            self.EpsilonCero = 8.85*10**-12
            self.longitud= float(self.e2.get())
            self.distancia= float(self.e1.get())
            self.ancho= float(self.e4.get())
            self.plexiglas= float(3.40)
            self.area = self.longitud*self.ancho
            self.voltaje= float(self.e3.get())

            if (self.longitud > 0 and self.distancia > 0 and  self.ancho > 0):
                #-----limpiar canvas-----
                self.limpiar()
                #---------calculo de capacitancia----------

                #parte con dielectrico
                """
                C= (K*E0*A) / 2d
                """
                self.CapacitanciaMitadCon= (self.plexiglas * self.EpsilonCero * self.area )/(2* self.distancia)
                #parte sin dielectrico
                """
                C= E0*(A/2d)
                """
                self.CapacitanciaMitadSin= (self.EpsilonCero * self.area )/(2* self.distancia)
                                
                #suma de estos C1+C2, porque estan en paralelo 
                self.CapacitanciaMitad= (self.CapacitanciaMitadCon + self.CapacitanciaMitadSin)
                self.l7.config(text=str( self.CapacitanciaMitad))

                #------carga del capacitor ------
                """ Q= C*V"""
                #///////////////////////////////////////
                # La carga no variará independientemente que se le introduzca un dieléctrico (ya sea mitad o full) al capacitor.
                # 
                self.Capacitancia= (self.EpsilonCero * self.area )/self.distancia
                self.carga= self.Capacitancia *  self.voltaje   
                self.l8.config(text="carga del capacitor (C):")
                self.l9.config(text=str(self.carga))
                #  
                #///////////////////////////////////////
                #self.cargaTotal= self.CapacitanciaMitad* self.voltaje
                #self.l8.config(text="carga del capacitor (C):")
                #self.l9.config(text=str(self.cargaTotal)) 

                #------energia almacenada------
                """
                E= (1/2)*CV^2
                E= (((1/2*C0*V^2)/2) + ((1/2*C*(V/K)^2)/2))
                """
                self.EnergiaCon = (1/2)*(self.CapacitanciaMitadCon*((self.voltaje/self.plexiglas)**2) )
                self.EnergiaSin = (1/2)*(self.CapacitanciaMitadSin*(self.voltaje**2)  )

                self.energia= self.EnergiaCon+ self.EnergiaSin
                self.l10.config(text="energia almacenada (J):")
                self.l11.config(text=str(self.energia)) 

                # Para el capacitor de placas paralelas con dieléctrico hasta la mitad tendrá:
                # Dos densidades de carga libre
                # Una densidad de carga ligada

                #------ carga libre de aire ------
                """
                Qaire= (2Q)/(K+1)*A
                """
                #Qaire= ((self.CapacitanciaMitadSin) * self.voltaje)
                         
                self.Qaire= ((2* self.carga)/ ((self.plexiglas+1) *self.area))
                
                self.l12.config(text="carga libre de Aire:")
                self.l13.config(text=str(self.Qaire))

                #------  carga libre de plexiglas------
                """
                Qdielectrico=(2QK)/(K+1)*A
                
                """
                self.Qdielectrico= ((2* self.carga * self.plexiglas )/ ((self.plexiglas+1) *self.area))
                self.l14.config(text="carga libre de plexigas:")
                self.l15.config(text=str(self.Qdielectrico))

                #------ carga ligada de plexigas------
                """
                Qligada=Q-Qdielectrico
                """
                self.Qligada= self.Qdielectrico -self.Qaire 
                self.l16.config(text="carga ligada de plexiglas:")
                self.l17.config(text=str(self.Qligada))

                #------ parte de la grafica -----------   
                self.c1.create_rectangle((self.c1.winfo_width()-(200*self.longitud) ) / 2, (self.c1.winfo_height()- (90*self.ancho) )/2,(self.c1.winfo_width()+(200*self.longitud) )/2 , (self.c1.winfo_height()-(90) )/2, outline='red', width="3")
                
                self.c1.create_rectangle(((self.c1.winfo_width()-(200*self.longitud) ) / 2 ), ((self.c1.winfo_height()- (90*self.ancho) )/2)+ (100*self.distancia),(self.c1.winfo_width()+(200*self.longitud) )/2 , (self.c1.winfo_height()-(90) )/2 + (100*self.distancia), outline='red', width="3")

                self.c1.create_rectangle((self.c1.winfo_width()-(200*self.longitud) ) / 2, (self.c1.winfo_height()-(90) )/2,(self.c1.winfo_width()+(1*self.longitud) )/2 , (self.c1.winfo_height()-(90*self.ancho) )/2 + (100*self.distancia), outline='purple', width="3")
                               

            else: 
                messagebox.showerror("Error", "Ingrese valores validos para la distancia y longitud")
        except Exception as msg: 
            messagebox.showerror("error", "asegurese de ingresar un número válido y todos los valores ")

    def PlacasParalelasDielectricoCompleto(self):
        """
        Ecuaciones utiles: 
        
        """
        try:

            self.EpsilonCero = 8.85*10**-12
            self.longitud= float(self.e2.get())
            self.distancia= float(self.e1.get())
            self.ancho= float(self.e4.get())
            self.plexiglas= float(3.40)
            self.voltaje= float(self.e3.get())
            self.area = self.longitud*self.ancho

            if (self.longitud > 0 and self.distancia > 0 and  self.ancho > 0):
                #-----limpiar canvas-----
                self.limpiar()
                #---------calculo de capacitancia----------
                """
                C= (K*E0*A) / d
                """
                self.capacitancia= (self.plexiglas * self.EpsilonCero * self.area )/(self.distancia)               
                self.l7.config(text=str( self.capacitancia))             

                #---------carga del capacitor ----------
                """ Q= C*V"""

                #///////////////////////////////////////
                # La carga no variará independientemente que se le introduzca un dieléctrico (ya sea mitad o full) al capacitor.
                # 
                self.Capacitancia= (self.EpsilonCero * self.area )/self.distancia
                self.carga= self.Capacitancia *  self.voltaje   
                self.l8.config(text="carga del capacitor (C):")
                self.l9.config(text=str(self.carga))
                #  
                #///////////////////////////////////////
                #self.cargaTotal= self.capacitancia* self.voltaje
                #self.l8.config(text="carga del capacitor (C):")
                #self.l9.config(text=str(self.cargaTotal)) 

                #---------energia almacenada ----------
                """
                E= (1/2*C*(V/K)^2)
                """
                self.Energia = (1/2)*(self.capacitancia*((self.voltaje/self.plexiglas)**2) )
                self.l10.config(text="energia almacenada (J):")
                self.l11.config(text=str(self.Energia)) 

                #--------- densidad carga libre ----------
                """
                densidadLibre= Q/A
                """
                #self.CargaLibre= self.capacitancia * self.voltaje
                self.densidadLibre= self.carga/ self.area
                self.l12.config(text=" carga libre :")
                self.l13.config(text=str(self.densidadLibre))


                #--------- densidad carga ligada ----------
                """
                densidadPlexiglas= Q/KA
                densidadLigada= densidadLibre-densidadPlexiglas
                """
                #self.Qligada= self.carga - self.CargaLibre
                self.densidadPlexiglas= self.carga/ (self.plexiglas * self.area)
                self.densidadLigada= self.densidadLibre-self.densidadPlexiglas 
                self.l14.config(text="carga ligada de plexigas:")
                self.l15.config(text=str(self.densidadLigada))
                self.l16.config(text=" ")
                self.l17.config(text=" ")

                #------ parte de la grafica -----------   
                self.c1.create_rectangle((self.c1.winfo_width()-(200*self.longitud) ) / 2, (self.c1.winfo_height()- (90*self.ancho) )/2,(self.c1.winfo_width()+(200*self.longitud) )/2 , (self.c1.winfo_height()-(90) )/2, outline='red', width="3")
                
                self.c1.create_rectangle(((self.c1.winfo_width()-(200*self.longitud) ) / 2 ), ((self.c1.winfo_height()- (90*self.ancho) )/2)+ (100*self.distancia),(self.c1.winfo_width()+(200*self.longitud) )/2 , (self.c1.winfo_height()-(90) )/2 + (100*self.distancia), outline='red', width="3")

                self.c1.create_rectangle((self.c1.winfo_width()-(200*self.longitud) ) / 2, (self.c1.winfo_height()-(90) )/2,(self.c1.winfo_width()+(200*self.longitud) )/2 , (self.c1.winfo_height()-(90*self.ancho) )/2 + (100*self.distancia), outline='purple', width="3")

                               

            else: 
                messagebox.showerror("Error", "Ingrese valores validos para la distancia y longitud")
        except Exception as msg: 
            messagebox.showerror("error", "asegurese de ingresar un número válido y todos los valores ")



    def Esferico(self):
        """
        Ecuaciones utiles: 
        C= 4pi*E0/((1/a)-(1/b))
        Q=C*Vab
        E= (1/2)*CV^2
        """
        try:

            self.EpsilonCero = 8.85*10**-12
            self.radioA= float(self.e1.get())
            self.radioB= float(self.e2.get())
            self.voltaje= float(self.e3.get())
            self.plexiglas= float(3.40)

            if (self.radioA > 0 and self.radioB > 0 and self.radioA!= self.radioB ):
                #-----limpiar canvas-----
                self.limpiar()
                #-----calculo de capacitancia------
                """
                C= 4pi*E0/((1/a)-(1/b))
                """
                self.Capacitancia= (self.EpsilonCero * 4 * pi)/((1/self.radioA)-(1/self.radioB))
                self.l7.config(text=str( self.Capacitancia))

                #------carga del capacitor ------
                """
                Q=C*Vab
                """
                
                self.carga= self.Capacitancia *  self.voltaje   
                self.l8.config(text="carga del capacitor (C):")
                self.l9.config(text=str(self.carga))

                #------energia------
                """
                E= (1/2)*CV^2
                """
                self.Energia = (1/2)*(self.Capacitancia*(self.voltaje**2) )
                self.l10.config(text="energia almacenada (J):")
                self.l11.config(text=str(self.Energia))

                self.l12.config(text=" ")
                self.l13.config(text=" ")
                self.l14.config(text=" ")
                self.l15.config(text=" ")
                self.l16.config(text=" ")
                self.l17.config(text=" ")
                self.l18.config(text=" ")
                self.l19.config(text=" ")
                self.l20.config(text=" ")
                self.l21.config(text=" ")
                self.l22.config(text=" ")
                self.l23.config(text=" ")



            else: 
                messagebox.showerror("Error", "Ingrese valores validos para la distancia y longitud")
        except Exception as msg: 
            messagebox.showerror("error", "asegurese de ingresar un número válido y todos los valores ")



    def EsfericoMitad(self):
        """
        Ecuaciones utiles: 
        C= 4pi*E0/((1/a)-(1/b))
        Q=C*Vab
        E= (1/2)*CV^2
        """
        try:

            self.EpsilonCero = 8.85*10**-12
            self.radioA= float(self.e1.get())
            self.radioB= float(self.e2.get())
            self.voltaje= float(self.e3.get())
            self.plexiglas= float(3.40)

            if (self.radioA > 0 and self.radioB > 0 and self.radioA!= self.radioB ):
                #-----limpiar canvas-----
                self.limpiar()
                #-----calculo de capacitancia------
                """
                C= k2pi*E0/((1/a)-(1/b))
                C= k2pi*E0* (rb*ra)/((rb)-(ra))
                """
                
                #-------capacidad total----
                self.Capacitancia1= (self.EpsilonCero  * self.plexiglas * 2 * pi)*(self.radioA * self.radioB)/((self.radioB)-(self.radioA))
                self.Capacitancia2= (self.EpsilonCero * 2 * pi)*(self.radioA * self.radioB)/((self.radioB)-(self.radioA))
                self.CapacitanciaTotal= self.Capacitancia1 + self.Capacitancia2
                
                self.l7.config(text=str( self.CapacitanciaTotal))

                #------carga del capacitor ------
                """
                Q=C*Vab
                """
                self.Capacitancia= (self.EpsilonCero * 4 * pi)/((1/self.radioA)-(1/self.radioB))
                self.carga= self.Capacitancia *  self.voltaje   
                self.l8.config(text="carga del capacitor (C):")
                self.l9.config(text=str(self.carga))

                #------energia------
                """
                E= (((1/2*C0*V^2)/2) + ((1/2*C*(V/K)^2)/2))
                """
                self.Energia = ((1/2)*(self.Capacitancia2*(self.voltaje**2))) # + ((1/2)*(self.Capacitancia1*(self.voltaje**2)))
                self.l10.config(text="energia almacenada (J):")
                self.l11.config(text=str(self.Energia))

                #------carga libre de aire Ra superior------
                """
                (1/(K+1))(Q/(2PI*(RA**2)))
                (1/(K+1))(Q/(2PI*(RB**2)))
                (1/(K+1))(QK/(2PI*(RA**2))
                (1/(K+1))(QK/(2PI*(RB**2)))
                """
                self.densidadLibreAireRaSuperior = (1/(self.plexiglas + 1)) * ((self.carga)/ (2 * pi * (self.radioA**2)))
                self.l12.config(text="carga Libre Aire Ra Superior")
                self.l13.config(text=str(self.densidadLibreAireRaSuperior))

                #------carga libre de aire Rb superior------
                self.densidadLibreAireRbSuperior = (1/(self.plexiglas + 1)) * ((self.carga)/ (2 * pi * (self.radioB**2)))
                self.l14.config(text="carga libre de aire Rb superior")
                self.l15.config(text=str(self.densidadLibreAireRbSuperior))
                                
                #------carga libre de aire Ra inferior------
                self.densidadLibreAireRaInferior = (1/(self.plexiglas + 1)) * ((self.carga * self.plexiglas)/ (2 * pi * (self.radioA**2)))
                self.l16.config(text="carga libre de aire Ra inferior")
                self.l17.config(text=str(self.densidadLibreAireRaInferior))

                #------carga libre de aire Rb inferior------
                self.densidadLibreAireRbInferior = (1/(self.plexiglas + 1)) * ((self.carga * self.plexiglas)/ (2 * pi * (self.radioB**2)))
                self.l22.config(text="carga libre de aire Rb inferior")
                self.l23.config(text=str(self.densidadLibreAireRbInferior))

                #------carga ligada de plexigas Ra inferior------
                """
                ((k-1)/(k+1))*(Q/(2*pi(Ra**2)))
                """
                self.cargaLigadaPlexiglasRaInferior= ((self.plexiglas-1)/(self.plexiglas+1))*(self.carga/(2*pi*(self.radioA)**2))
                self.l18.config(text="carga ligada de plexigas Ra inferior:")
                self.l19.config(text=str(self.cargaLigadaPlexiglasRaInferior))

                #------carga ligada de plexigas Rb inferior------
                """
                ((k-1)/(k+1))*(Q/(2*pi(Rb**2)))
                """
                self.cargaLigadaPlexiglasRbInferior= ((self.plexiglas-1)/(self.plexiglas+1))*(self.carga/(2*pi*(self.radioB)**2))
                self.l20.config(text="carga ligada de plexigas Rb inferior:")
                self.l21.config(text=str(self.cargaLigadaPlexiglasRbInferior))
                            


            else: 
                messagebox.showerror("Error", "Ingrese valores validos para la distancia y longitud")
        except Exception as msg: 
            messagebox.showerror("error", "asegurese de ingresar un número válido y todos los valores ")


    def EsfericoCompleto(self):
        
        
        self.EpsilonCero = 8.85*10**-12
        self.radioA= float(self.e1.get())
        self.radioB= float(self.e2.get())
        self.voltaje= float(self.e3.get())
        self.plexiglas= float(3.40)
        try:
            if (self.radioA > 0 and self.radioB > 0 and self.radioA!= self.radioB ):
                    #-----limpiar canvas-----
                    self.limpiar()
                    #-----calculo de capacitancia------
                    """
                    C = k(Ra*Rb)(4*pi*e)/(b-a)
                    C = (k*4*pi*e)*((Ra*Rb)/(Rb-Ra))
                    """
                    
                    #-------capacidad total----
                    self.Capacitancia = (self.plexiglas*4*pi*self.EpsilonCero)*((self.radioA*self.radioB)/(self.radioB-self.radioA))
                    self.l7.config(text=str( self.Capacitancia))

                    #------carga del capacitor ------
                    """
                    Q = Cog*V
                    """
                    self.cog = (4*pi*self.EpsilonCero)*((self.radioA*self.radioB)/(self.radioB-self.radioA))
                    self.carga= self.voltaje*self.cog 
                    self.l8.config(text="carga del capacitor (C):")
                    self.l9.config(text=str(self.carga))

                    #------energia acumulada------
                    """
                    E= (C*V^2)/2
                    """
                    self.Energia = (self.Capacitancia*(self.voltaje/self.plexiglas)**2)/2
                    self.l10.config(text="energia almacenada (J):")
                    self.l11.config(text=str(self.Energia))

                    #------carga libre de aire Ra superior------
                    """
                    Q/((4*pi*(Ra**2))) 
                    Q/((4*pi*(Rb**2)))
                    """
                    #------Carga libre de aire Ra -----------
                    self.densidadLibreAireRa=  self.carga/((4*pi*(self.radioA**2)))
                    self.l12.config(text="carga Libre Aire Ra ")
                    self.l13.config(text=str(self.densidadLibreAireRa))

                    #------carga libre de aire Rb ------
                    self.densidadLibreAireRb = self.carga/((4*pi*(self.radioB**2)))
                    self.l14.config(text="carga libre de aire Rb ")
                    self.l15.config(text=str(self.densidadLibreAireRb))
                                    
                    #------carga ligada de plexigas ------
                    """
                    CargaLibre1*(1-1/k)
                    CargaLibre2*(1-1/k)
                    """
                    #----- carga ligada plexigas Ra -----------
                    self.cargaLigadaPlexiglasRa= self.densidadLibreAireRa*(1-1/self.plexiglas)
                    self.l18.config(text="carga ligada de plexigas Ra :")
                    self.l19.config(text=str(self.cargaLigadaPlexiglasRa))

                    #------carga ligada de plexigas Rb ------
                
                    self.cargaLigadaPlexiglasRb = self.densidadLibreAireRb*(1-1/self.plexiglas)
                    self.l20.config(text="carga ligada de plexigas Rb :")
                    self.l21.config(text=str(self.cargaLigadaPlexiglasRb))
                                

            else: 
                messagebox.showerror("Error", "Ingrese valores validos para la distancia y longitud")
        

        except Exception as msg: 
            messagebox.showerror("error", "asegurese de ingresar un número válido y todos los valores ")



    def Cilindrico(self):
        """
        Ecuaciones utiles: 
        C= 2pi*E0*L/ln(b/a)
        Q=C*Vab
        E= (1/2)*CV^2
        """
        try:

            self.EpsilonCero = 8.85*10**-12
            self.radioA= float(self.e1.get())
            self.radioB= float(self.e2.get())
            self.largo= float(self.e3.get())
            self.voltaje= float(self.e4.get())
            self.plexiglas= float(3.40)

            if (self.radioA > 0 and self.radioB > 0 and  self.largo > 0):
                #-----limpiar canvas-----
                self.limpiar()
                #-----calculo de capacitancia------
                """
                C= 2pi*E0*L/ln(b/a)
                """
                self.Capacitancia= (self.EpsilonCero * self.largo * 2 * pi)/log(self.radioB/self.radioA)
                self.l7.config(text=str( self.Capacitancia))

                #------carga del capacitor ------
                """ 
                Q=C*Vab
                """
                
                self.carga= self.Capacitancia *  self.voltaje   
                self.l8.config(text="carga del capacitor (C):")
                self.l9.config(text=str(self.carga))

                #------energia------
                """
                E= (1/2)*CV^2
                """
                self.Energia = (1/2)*(self.Capacitancia*(self.voltaje**2) )
                self.l10.config(text="energia almacenada (J):")
                self.l11.config(text=str(self.Energia))

                self.l12.config(text=" ")
                self.l13.config(text=" ")
                self.l14.config(text=" ")
                self.l15.config(text=" ")
                self.l16.config(text=" ")
                self.l17.config(text=" ")
                



            else: 
                messagebox.showerror("Error", "Ingrese valores validos para la distancia y longitud")
        except Exception as msg: 
            messagebox.showerror("error", "asegurese de ingresar un número válido y todos los valores ")

    def CilindricoMitad(self):
        """
        Ecuaciones utiles: 
        C= 2pi*E0*L/ln(b/a)
        Q=C*Vab
        E= (1/2)*CV^2
        """
        self.EpsilonCero = 8.85*10**-12
        self.radioA= float(self.e1.get())
        self.radioB= float(self.e2.get())
        self.largo= float(self.e3.get())
        self.voltaje= float(self.e4.get())
        self.plexiglas= float(3.40)

        try:

            self.EpsilonCero = 8.85*10**-12
            self.radioA= float(self.e1.get())
            self.radioB= float(self.e2.get())
            self.largo= float(self.e3.get())
            self.voltaje= float(self.e4.get())
            self.plexiglas= float(3.40)

            if (self.radioA > 0 and self.radioB > 0 and  self.largo > 0):
                #-----limpiar canvas-----
                self.limpiar()
                #-----calculo de capacitancia------
                """
                C= (k)(pi*l*e)/(ln(Rb/Ra)) + (pi*l*e)/(ln(Rb/Ra))
                """
                self.Capacitancia = (self.plexiglas * pi * self.largo * self.EpsilonCero) / (log(self.radioB / self.radioA)) + (pi * self.largo * self.EpsilonCero) / (log(self.radioB / self.radioA))
                self.l7.config(text=str( self.Capacitancia))

                #------carga del capacitor ------
                """ 
                Q = Cog*V
                Cog = (2*pi*l*e)/(ln(Rb/Ra))
                """
                self.cog = (2*pi*self.largo*self.EpsilonCero)/(log(self.radioB/self.radioA))
                self.carga= self.cog * self.voltaje
                self.l8.config(text="carga del capacitor (C):")
                self.l9.config(text=str(self.carga))

                #------energia------
                """
                E = (C*V^2)/2
                """
                self.Energia = (self.cog*(self.voltaje**2))/4 + (self.Capacitancia*(self.voltaje/self.plexiglas)**2)/4
                self.l10.config(text="energia almacenada (J):")
                self.l11.config(text=str(self.Energia))

                # ---- cargas libres -----
                """
                
                Q/((2*pi*Ra*l*(k+1))/2)
                Q/((2*pi*Rb*l*(k+1))/2)
                (Q*k)/((2*pi*Ra*l*(k+1))/2)
                (Q*k)/((2*pi*Rb*l*(k+1))/2)

                """

                # ----- carga libre Radio a Superior --------
                self.cargaLibreSuperiorRa = self.carga/((2*pi*self.radioA*self.largo*(self.plexiglas+1))/2)
                self.l12.config(text="Carga libre Superior Ra")
                self.l13.config(text=str(self.cargaLibreSuperiorRa))

                # ----- carga libre Radio b Superior --------
                self.cargaLibreSuperiorRb = self.carga/((2*pi*self.radioB*self.largo*(self.plexiglas+1))/2)
                self.l14.config(text="Carga libre Superior Rb")
                self.l15.config(text=str(self.cargaLibreSuperiorRb))


                # ----- carga libre Radio a Inferior --------
                self.cargaLibreInferiorRa = (self.carga*self.plexiglas)/((2*pi*self.radioA*self.largo*(self.plexiglas+1))/2)
                self.l16.config(text="Carga libre Inferior Ra")
                self.l17.config(text=str(self.cargaLibreInferiorRa))


                # ----- carga libre Radio a Inferior --------
                self.cargaLibreInferiorRb = (self.carga*self.plexiglas)/((2*pi*self.radioB*self.largo*(self.plexiglas+1))/2)
                self.l18.config(text="Carga libre Inferior Rb")
                self.l19.config(text=str(self.cargaLibreInferiorRb))


                # ---- cargas ligadas
                """
                CargaLibreInferiorRa*(1-1/k)
                CargaLibreInferiorRb*(1-1/k)
                """
             
                #---- carga ligada Ra -----
                self.cargaLigadaRa = self.cargaLibreInferiorRa*(1-1/self.plexiglas)
                self.l20.config(text="Carga libre Inferior Ra")
                self.l21.config(text=str(self.cargaLigadaRa))
                
                #---- carga ligada Ra -----
                self.cargaLigadaRb = self.cargaLibreInferiorRb*(1-1/self.plexiglas)
                self.l22.config(text="Carga libre Inferior Rb")
                self.l23.config(text=str(self.cargaLigadaRb))





            else: 
                messagebox.showerror("Error", "Ingrese valores validos para la distancia y longitud")
        except Exception as msg: 
            messagebox.showerror("error", "asegurese de ingresar un número válido y todos los valores ")


    def CilindricoCompleto(self):
        """
        Ecuaciones utiles: 
        C= 2pi*E0*L/ln(b/a)
        Q=C*Vab
        E= (1/2)*CV^2
        """
        self.EpsilonCero = 8.85*10**-12
        self.radioA= float(self.e1.get())
        self.radioB= float(self.e2.get())
        self.largo= float(self.e3.get())
        self.voltaje= float(self.e4.get())
        self.plexiglas= float(3.40)

        try:

            self.EpsilonCero = 8.85*10**-12
            self.radioA= float(self.e1.get())
            self.radioB= float(self.e2.get())
            self.largo= float(self.e3.get())
            self.voltaje= float(self.e4.get())
            self.plexiglas= float(3.40)

            if (self.radioA > 0 and self.radioB > 0 and  self.largo > 0):
                #-----limpiar canvas-----
                self.limpiar()
                #-----calculo de capacitancia------
                """
                C= 
                C = (k*2*pi*l*e)/(ln(Rb/Ra))
                """
                self.Capacitancia = (self.plexiglas * 2 * pi * self.largo * self.EpsilonCero) / (log(self.radioB / self.radioA))
                self.l7.config(text=str( self.Capacitancia))

                #------carga del capacitor ------
                """ 
                Q = Cog*V
                Cog = (2*pi*l*e)/(ln(Rb/Ra))
                """
                self.cog = (2*pi*self.largo*self.EpsilonCero)/(log(self.radioB/self.radioA))
                self.carga= self.cog * self.voltaje
                self.l8.config(text="carga del capacitor (C):")
                self.l9.config(text=str(self.carga))

                #------energia------
                """
                E = (C*(Voltage/k)**2)/2
                """
                self.Energia = (self.Capacitancia*(self.voltaje/self.plexiglas)**2)/2
                self.l10.config(text="energia almacenada (J):")
                self.l11.config(text=str(self.Energia))

                # ---- cargas libres -----
                """
                
                Q/((2*pi*Ra*l))
                Q/((2*pi*Rb*l))

                """

                # ----- carga libre Radio a  --------
                self.cargaLibreRa = self.carga/((2*pi*self.radioA*self.largo))
                self.l12.config(text="Carga libre Ra")
                self.l13.config(text=str(self.cargaLibreRa))

                # ----- carga libre Radio b  --------
                self.cargaLibreRb = self.carga/((2*pi*self.radioB*self.largo))
                self.l14.config(text="Carga libre Rb")
                self.l15.config(text=str(self.cargaLibreRb))



                # ---- cargas ligadas
                """
                CargaLibreInferiorRa*(1-1/k)
                CargaLibreInferiorRb*(1-1/k)
                """
             
                #---- carga ligada Ra -----
                self.cargaLigadaRa = self.cargaLibreRa*(1-1/self.plexiglas)
                self.l16.config(text="Carga libre Ra")
                self.l17.config(text=str(self.cargaLigadaRa))
                
                #---- carga ligada Ra -----
                self.cargaLigadaRb = self.cargaLibreRb*(1-1/self.plexiglas)
                self.l18.config(text="Carga libre Rb")
                self.l19.config(text=str(self.cargaLigadaRb))

                self.l20.config(text="")
                self.l21.config(text="")
                self.l22.config(text="")
                self.l23.config(text="")
                



            else: 
                messagebox.showerror("Error", "Ingrese valores validos para la distancia y longitud")
        except Exception as msg: 
            messagebox.showerror("error", "asegurese de ingresar un número válido y todos los valores ")


                  


    def limpiar(self):
        self.c1.delete("all")


            

    


app().mainloop()