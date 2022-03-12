import os


class nodo:

    def __init__(self, nombre, ingrediente, cantidad, tiempo):
        self.nombre=nombre
        self.ingrediente=ingrediente
        self.cantidad=cantidad
        self.tiempo=tiempo
        self.siguiente=None
        self.principio=None
        self.fin=None

class colita:
    def __init__(self):
        self.inicio=None
        
    def push(self, nombre, ingrediente, cantidad, tiempo):
       	
        if self.inicio==None:
            #tm=int(self.tiempoUltimo)+int(tiempo)
            nuevo=nodo(nombre, ingrediente, cantidad, tiempo)
            self.inicio=nuevo
            self.inicio.principio=nuevo
            nuevo.fin=nuevo
            

        else:
            tm=int(self.tiempoUltimo())+int(tiempo)
            nuevo=nodo(nombre, ingrediente, cantidad, tm)
            aux=self.posicion()
            aux.siguiente=nuevo
            nuevo.fin=nuevo

    def pop(self):
        try:
            aux=self.inicio
            print("La orden de pizza con "+aux.nombre+" fue despachada")
            
            self.inicio=self.inicio.siguiente
        except:
            print("No hay ordenes")

       
        
    def posicion(self):
        ultimo=self.inicio

        while ultimo.siguiente != None:
            ultimo=ultimo.siguiente

        return ultimo

    def mostrar(self):
        aux=self.inicio
        while aux != None:
            print("\n Cliente: "+aux.nombre+" - Tiempo de orden: "+str(aux.tiempo)+" minutos")
            aux=aux.siguiente


    def grafica(self):
        txt = '''
        digraph G { \n
        node[shape=square]; \n
        rankdir = LR \n
        
        '''
        aux=self.inicio
        
        while aux.siguiente != None:
            #print("Cliente: "+aux.nombre+" - Tiempo de orden: "+str(aux.tiempo)+" minutos")
            txt = txt + '"'+"Cliente: "+aux.nombre+"\n Tiempo: "+str(aux.tiempo)+" minutos"+ '"' + "->" +'"'+"Cliente: "+aux.siguiente.nombre+"\n Tiempo: "+str(aux.siguiente.tiempo)+" minutos" + '"'+ "; \n"
            aux=aux.siguiente
        

        txt = txt + "}"

        #print("Se a generado Imagen")
        file = open("cola.dot", "w")
        file.write(txt)
        file.close()
        
        #import os
        os.system("dot cola.dot -Tpng -o cola.png")
        #os.system("eog, grafsnake.png")
        print("Se a generado Imagen")
	

    def tiempoUltimo(self):
        tiempo=0
        aux=self.inicio
        while aux != None:
            tiempo=int(aux.tiempo)
            aux=aux.siguiente

        return tiempo
        









       