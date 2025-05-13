class Cola:
    def __init__(self):
        self.cola = []
    
    def encolar(self, item):
        self.cola.append(item)
    
    def desencolar(self):
        if not self.esta_vacia():
            return self.cola.pop(0)
        else:
            print("La cola esta vacia.")
            return None
    
    def esta_vacia(self):
        return len(self.cola) == 0

    def mostrar(self):
        if self.esta_vacia():
            print("La cola esta vacia.")
        else:
            print("Contenido de la cola:", self.cola)

# Programa principal
if __name__ == "__main__":
    cola = Cola()
    
    while True:
        print("\n=== Menu de Cola ===")
        print("1. Encolar")
        print("2. Desencolar")
        print("3. Mostrar Cola")
        print("4. Salir")
        
        opcion = input("Selecciona una opcion: ")
        
        if opcion == '1':
            valor = input("Ingresa un valor para encolar: ")
            cola.encolar(valor)
            print(f"'{valor}' ha sido encolado.")
        
        elif opcion == '2':
            resultado = cola.desencolar()
            if resultado is not None:
                print(f"'{resultado}' ha sido desencolado.")
        
        elif opcion == '3':
            cola.mostrar()
        
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida. Intenta de nuevo.")
