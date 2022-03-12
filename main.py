import cola
class Index:
    
    
    def __init__ (self, opcion):
        self.opcion=opcion

def main():

        var=cola.colita()
       
        menu='''
        \n
        Menu Principal:
        1.- Ingresar Orden
        2.- Entregar Orden
        3.- Mostrar Ordenes
        4.- Mostrar Grafica
        5.- Mostrar Datos
        6.- Salir'''

        while True:
            print(menu)
            op=input("Ingrese una opcion: ")

            if op == '1':               
                #rt=input("Ingrese el ingrediente para la pizza: ")
                v1=input("Ingrese Nombre del cliente: ")
                v2=input("Ingrese el ingrediente para la pizza: ")
                v3=input("Ingrese cantidad de pizzas: ")
                v4=1
                if (v2 == "Pepperoni"):
                    v4=3
                elif (v2 == "Salchicha"):
                    v4=4
                elif (v2 == "Carne"):
                    v4=10
                elif (v2 == "Queso"):
                    v4=5
                elif (v2 == "Piña"):
                    v4=2
                else:
                    print("ingrediente no encontrado")
                
                
                v4=int(v3)*v4
                var.push(v1,v2,v3,v4)
                

            elif op == '2':  

                var.pop()
                
                
                
                          
            elif op == '3':
                print("Ordenes en cola: ")#mostrar
                var.mostrar()
                

            elif op == '4':
               var.grafica()
               
            elif op == '5':
                tx='''
                    Maria Luisa Fernanda Calderon Molina
                    201602458
                    INTRODUCCION A LA PROGRAMACION Y COMPUTACION 2 
                    Sección B
                '''
                print(tx)
               #var.grafica()

            
            elif op == '6':
                break
            else:
                print("Opcion Invalida")
                #break

    


if __name__ == "__main__":
    main()
