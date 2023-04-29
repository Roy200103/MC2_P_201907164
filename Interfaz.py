from tkinter import *
from tkinter import *
from tkinter import messagebox
from algoritmo import prim
import networkx as nx
import matplotlib.pyplot as plt
class VentPrin:
    def __init__(self):
        self.vent = Tk()
        self.vent.resizable(False,False)
        self.vent.title('Proyecto 2 Laboratorio IPC2 C')
        self.Centrar(self.vent, 430, 500)
        self.vent.geometry('600x600')
        self.vent.configure(bg='AntiqueWhite3')
        self.vertices=[]
        self.edges=[]
        self.Ventana()
        
        
    def Centrar(self, r, ancho, alto):
        altura_pantalla = r.winfo_screenheight()
        ancho_pantalla = r.winfo_screenwidth()

        x = (ancho_pantalla // 2) - (ancho // 2)
        y = (altura_pantalla // 2) - (alto // 2)
        r.geometry(f'+{x}+{y}')
    
    def Ventana(self):
        self.frame = Frame(height=500, width=400)
        self.frame.config(bg='DarkSeaGreen2')
        self.frame.pack(padx=25, pady=25)

        self.extension = StringVar()
        self.extension1 = StringVar()
        self.extension2 = StringVar()
        self.extension3 = StringVar()
        self.extension4 = StringVar()
        Label(self.frame, text="Ingrese Vertices", font=('Arial Black',10), fg='#000000', bg= 'AntiqueWhite3',    width=20 ).place(x=110, y=15)
        self.ext1= Entry(self.frame , textvariable= self.extension ,font=('Times New Roman',12), width='20'  ).place(x='120', y='60')
        Button(self.frame, text="Agregar", command=self.AgV ,font=('Times New Roman',10), fg='#000000', bg= 'NavajoWhite2', width=15).place(x=140, y=90)
        Label(self.frame, text="Conecte Vertices", font=('Arial Black',10), fg='#000000', bg= 'AntiqueWhite3',    width=20 ).place(x=110, y=140)
        Label(self.frame, text="Peso", font=('Arial Black',10), fg='#000000', bg= 'AntiqueWhite3',    width=10 ).place(x=80, y=170)
        self.ext2= Entry(self.frame , textvariable= self.extension1 ,font=('Times New Roman',12), width='10'  ).place(x='190', y='170')
        Label(self.frame, text="Origen", font=('Arial Black',10), fg='#000000', bg= 'AntiqueWhite3',    width=10 ).place(x=80, y=195)
        self.ext3= Entry(self.frame , textvariable= self.extension2 ,font=('Times New Roman',12), width='10'  ).place(x='190', y='195')
        Label(self.frame, text="Destino", font=('Arial Black',10), fg='#000000', bg= 'AntiqueWhite3',    width=10 ).place(x=80, y=220)
        self.ext4= Entry(self.frame , textvariable= self.extension3 ,font=('Times New Roman',12), width='10'  ).place(x='190', y='220')
        Button(self.frame, text="Agregar", command=self.AgA ,font=('Times New Roman',10), fg='#000000', bg= 'NavajoWhite2', width=15).place(x=140, y=250)
        Button(self.frame, text="Ver Grafo", command=self.VerGrafo  ,font=('Times New Roman',10), fg='#000000', bg= 'NavajoWhite2', width=20).place(x=125, y=300)
        Label(self.frame, text="Aplicar Algoritmo de Prim", font=('Arial Black',10), fg='#000000', bg= 'AntiqueWhite3',    width=30 ).place(x=70, y=360)
        Label(self.frame, text="Origen", font=('Arial Black',10), fg='#000000', bg= 'AntiqueWhite3',    width=10 ).place(x=80, y=400)
        self.ext4= Entry(self.frame , textvariable= self.extension4 ,font=('Times New Roman',12), width='10'  ).place(x='190', y='400')
        Button(self.frame, text="Aplicar", command=self.ApAP, font=('Times New Roman',10), fg='#000000', bg= 'NavajoWhite2', width=15).place(x=140, y=430)
        self.frame.mainloop()

    def AgV(self):
        
        v=self.extension.get()
        ex=False
        for i in range(len(self.vertices)):
            if v == self.vertices[i]:
                messagebox.showinfo(message="El Vartice ya existe", title="AVISO")
                self.extension.set('')
                ex=True
                break
        if ex==False and v != '':
            self.vertices.append(v)
            self.extension.set('')
        #print(self.vertices)
    def AgA(self):
        pe=int(self.extension1.get())
        Vo=self.extension2.get()
        Vd=self.extension3.get()
        exv=False
        for i in range(len(self.vertices)):
            if Vo == self.vertices[i]:
                exv=True
        for i in range(len(self.vertices)):
            if Vd == self.vertices[i]:
                exv=True
        if exv==True and pe != '' and Vo != '' and Vd != '':
            self.edges.append((pe,Vo,Vd))
            self.extension1.set('')
            self.extension2.set('')
            self.extension3.set('')
        else:
            messagebox.showinfo(message="Uno de los Vertices no existe", title="AVISO")
            self.extension1.set('')
            self.extension2.set('')
            self.extension3.set('')
        #print(self.edges)

    def VerGrafo(self):
        
        print(self.edges)
        H = nx.DiGraph()

    # Agregar nodo
        for i in range(len(self.edges)):
          self.agregar_arista(H, self.edges[i][1], self.edges[i][2], self.edges[i][0])    
    # Crear Grafo
        pos = nx.layout.planar_layout(H)
        nx.draw_networkx(H, pos)
        labels = nx.get_edge_attributes(H, 'weight')
        nx.draw_networkx_edge_labels(H, pos, edge_labels=labels)
        plt.title("Grafo Ingresado")
        plt.show()
    
    def ApAP(self):
        ori=self.extension4.get()
        Ag=prim(self.vertices,self.edges,ori)
        G = nx.DiGraph()

    # Agregar nodo
        for i in range(len(Ag)):
          self.agregar_arista(G, Ag[i][1], Ag[i][2], Ag[i][0])    
    # Crear Grafo
        pos = nx.layout.planar_layout(G)
        nx.draw_networkx(G, pos)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.title("ALGORITMO DE PRIM")
        plt.show()
    
    def agregar_arista(self,G, o, d, w ):
        G.add_edge(o, d, weight=w)