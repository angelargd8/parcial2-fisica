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
from tkinter.ttk import Combobox 
from sympy import *  #libreria para las derivadas e integrales



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

        #self.b = Button(self, text = "Crear",command= self.PlacasGUI, width=20, bg="#ff8fab"); self.b.place(x=20, y =130)
        self.b = Button(self, text = "Crear",command= self.llamar, width=20, bg="#ff8fab"); self.b.place(x=10, y =190)





    def llamar(self): # para llamar a las diferentes pantallas
        if(self.caja.get()=="Placas paralelas"):
            self.PlacasGUI()
        #else if 



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

                #------ parte de la grafica -----------   
                self.c1.create_rectangle((self.c1.winfo_width()-(200*self.longitud) ) / 2, (self.c1.winfo_height()- (90*self.ancho) )/2,(self.c1.winfo_width()+(200*self.longitud) )/2 , (self.c1.winfo_height()-(90) )/2, outline='red', width="3")
                
                self.c1.create_rectangle(((self.c1.winfo_width()-(200*self.longitud) ) / 2 ), ((self.c1.winfo_height()- (90*self.ancho) )/2)+ (100*self.distancia),(self.c1.winfo_width()+(200*self.longitud) )/2 , (self.c1.winfo_height()-(90) )/2 + (100*self.distancia), outline='red', width="3")



            else: 
                messagebox.showerror("Error", "Ingrese valores validos para la distancia y longitud")
        except Exception as msg: 
            messagebox.showerror("error", "asegurese de ingresar un número válido y todos los valores ")
                

        

    def PlacasParalelasDielectricoMitad(self):
        """
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

                #------ densidad carga libre de aire ------
                """
                Qaire= C2*V
                densidadAire= Qaire/ Area
                """
                #Qaire= ((self.CapacitanciaMitadSin) * self.voltaje)
                self.densidadAire= (self.carga/  self.area)/2
#------ 
                #self.densidadAire= self.Qaire/ self.area
                self.l12.config(text="DENSIDAD carga libre de Aire:")
                self.l13.config(text=str(self.densidadAire))

                #------ densidad carga libre de plexiglas------
                """
                Qdielectrico= C1*V
                densidadPlexiglas= Qaire/ Area
                """
                #self.Qdielectrico= self.CapacitanciaMitadCon * self.voltaje
                self.densidadPlexiglas= (self.carga/  (self.plexiglas * self.area))/2
#------ 
                #self.densidadPlexiglas= self.Qdielectrico/ self.area
                self.l14.config(text="DENSIDAD carga libre de plexigas:")
                self.l15.config(text=str(self.densidadPlexiglas))

                #------ densidad carga ligada de plexigas------
                """
                Qligada=Q-Qdielectrico
                densidadLigada= densidadLibre-densidadPlexigas
                """
                self.densidadligada= self.densidadAire- self.densidadPlexiglas
                self.l16.config(text="DENSIDAD de carga ligada de plexiglas:")
                self.l17.config(text=str(self.densidadligada))

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
                self.l12.config(text=" DENSIDAD carga libre :")
                self.l13.config(text=str(self.densidadLibre))


                #--------- densidad carga ligada ----------
                """
                densidadPlexiglas= Q/KA
                densidadLigada= densidadLibre-densidadPlexiglas
                """
                #self.Qligada= self.carga - self.CargaLibre
                self.densidadPlexiglas= self.carga/ (self.plexiglas * self.area)
                self.densidadLigada= self.densidadLibre-self.densidadPlexiglas 
                self.l14.config(text="DENSIDAD carga ligada de plexigas:")
                self.l15.config(text=str(self.densidadLigada))

                #------ parte de la grafica -----------   
                self.c1.create_rectangle((self.c1.winfo_width()-(200*self.longitud) ) / 2, (self.c1.winfo_height()- (90*self.ancho) )/2,(self.c1.winfo_width()+(200*self.longitud) )/2 , (self.c1.winfo_height()-(90) )/2, outline='red', width="3")
                
                self.c1.create_rectangle(((self.c1.winfo_width()-(200*self.longitud) ) / 2 ), ((self.c1.winfo_height()- (90*self.ancho) )/2)+ (100*self.distancia),(self.c1.winfo_width()+(200*self.longitud) )/2 , (self.c1.winfo_height()-(90) )/2 + (100*self.distancia), outline='red', width="3")

                self.c1.create_rectangle((self.c1.winfo_width()-(200*self.longitud) ) / 2, (self.c1.winfo_height()-(90) )/2,(self.c1.winfo_width()+(200*self.longitud) )/2 , (self.c1.winfo_height()-(90*self.ancho) )/2 + (100*self.distancia), outline='purple', width="3")

                               

            else: 
                messagebox.showerror("Error", "Ingrese valores validos para la distancia y longitud")
        except Exception as msg: 
            messagebox.showerror("error", "asegurese de ingresar un número válido y todos los valores ")




    def Esferico(self):
        pass

    def Cilindrico(self):
        pass
                  


    def limpiar(self):
        self.c1.delete("all")


            

    


app().mainloop()