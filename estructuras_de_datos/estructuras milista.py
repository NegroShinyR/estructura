class MiLista:
    def __init__(self):
        self.lista = []
    
    def agregar(self, elemento):
        self.lista.append(elemento)
    
    def eliminar(self, elemento):
        if elemento in self.lista:
            self.lista.remove(elemento)
        else:
            print(f"{elemento} no encontrado en la lista.")
    
    def mostrar(self):
        print("Contenido de la lista:", self.lista)

def menu():
    mi_lista = MiLista()
    
    while True:
        print("\n--- MENU ---")
        print("1. Agregar elemento")
        print("2. Eliminar elemento")
        print("3. Mostrar lista")
        print("4. Salir")

        opcion = input("Elige una opcion: ")

        if opcion == "1":
            elem = input("Ingresa el elemento a agregar: ")
            mi_lista.agregar(elem)
            print(f"{elem} agregado.")
        elif opcion == "2":
            elem = input("Ingresa el elemento a eliminar: ")
            mi_lista.eliminar(elem)
        elif opcion == "3":
            mi_lista.mostrar()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no valida. Intenta de nuevo.")

menu()
