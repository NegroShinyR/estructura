
class Pila:
    def __init__(self):
        self.items = []
    
    def apilar(self, item):
        self.items.append(item)
    
    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            print("La pila está vacia.")
    
    def esta_vacia(self):
        return len(self.items) == 0

    def mostrar(self):
        print("Contenido de la pila (de abajo hacia arriba):", self.items)

# Función con menú
def menu():
    mi_pila = Pila()

    while True:
        print("\n--- MENÚ ---")
        print("1. Apilar elemento")
        print("2. Desapilar elemento")
        print("3. Mostrar pila")
        print("4. Salir")

        opcion = input("Elige una opcion: ")

        if opcion == "1":
            elem = input("Ingresa el elemento a apilar: ")
            mi_pila.apilar(elem)
            print(f"{elem} apilado.")
        elif opcion == "2":
            desapilado = mi_pila.desapilar()
            if desapilado is not None:
                print(f"Elemento desapilado: {desapilado}")
        elif opcion == "3":
            mi_pila.mostrar()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opcion no valida. Intenta de nuevo.")

# Ejecutar el programa
menu()
