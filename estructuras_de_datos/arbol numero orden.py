class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)
    
    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.izquierda, valor)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.derecha, valor)

    def recorrido_inorden(self):
        print("Recorrido inorden (valores ordenados):")
        self._inorden(self.raiz)
        print()  # Salto de línea

    def _inorden(self, nodo):
        if nodo is not None:
            self._inorden(nodo.izquierda)
            print(nodo.valor, end=' ')
            self._inorden(nodo.derecha)

# Programa principal
if __name__ == "__main__":
    arbol = ArbolBinario()

    print("Árbol Binario de Búsqueda - Inserción de Números")
    while True:
        try:
            entrada = input("Ingresa un numero (o escribe 'salir' para terminar): ")
            if entrada.lower() == 'salir':
                break
            numero = int(entrada)
            arbol.insertar(numero)
        except ValueError:
            print("Por favor, ingresa un numero valido.")

    arbol.recorrido_inorden()
