class MiDiccionario:
    def __init__(self):
        self.size = 10
        self.table = [None] * self.size
    
    def hash(self, clave):
        return hash(clave) % self.size
    
    def agregar(self, clave, valor):
        indice = self.hash(clave)
        self.table[indice] =  valor 
    
    def obtener(self, clave):
        indice = self.hash(clave)
        return self.table[indice]

    def mostrar(self):
        print("\nContenido del diccionario:")
        for i, valor in enumerate(self.table):
            print(f"Índice {i}: {valor}")

# Programa principal
if __name__ == "__main__":
    diccionario = MiDiccionario()
    
    while True:
        print("\n=== Menu del Diccionario ===")
        print("1. Agregar clave y valor")
        print("2. Obtener valor por clave")
        print("3. Mostrar tabla interna")
        print("4. Salir")
        
        opcion = input("Selecciona una opcion: ")
        
        if opcion == '1':
            clave = input("Ingresa la clave: ")
            valor = input("Ingresa el valor: ")
            diccionario.agregar(clave, valor)
            print(f"Se agregó ('{clave}': '{valor}') al diccionario.")
        
        elif opcion == '2':
            clave = input("Ingresa la clave para buscar su valor: ")
            valor = diccionario.obtener(clave)
            if valor is not None:
                print(f"Valor encontrado: {valor}")
            else:
                print("No se encontro un valor para esa clave.")
        
        elif opcion == '3':
            diccionario.mostrar()
        
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        
        else:
            print("Opcion no valida. Intenta de nuevo.")
