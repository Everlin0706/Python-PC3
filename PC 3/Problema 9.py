import math

# Definición de la clase CIRCULO
class CIRCULO:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)


# Definición de la clase RECTANGULO
class RECTANGULO:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def area(self):
        return self.largo * self.ancho


# Definición de la clase CUADRADO, que hereda de RECTANGULO
class CUADRADO(RECTANGULO):
    def __init__(self, lado):
        super().__init__(lado, lado)


# Función para validar si un número es válido y positivo
def validar_numero(valor):
    try:
        numero = float(valor)
        if numero > 0:
            return numero
        else:
            print("Error: Debe ingresar un número positivo.")
            return None
    except ValueError:
        print("Error: Tipo de dato no válido. Debe ser un número.")
        return None


# Menú interactivo
def menu():
    while True:
        print("\nMenú:")
        print("1. Calcular el área de un círculo")
        print("2. Calcular el área de un rectángulo")
        print("3. Calcular el área de un cuadrado")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == '1':
            radio = input("Ingrese el radio del círculo: ")
            radio = validar_numero(radio)
            if radio is not None:
                circulo = CIRCULO(radio)
                print(f"El área del círculo es: {circulo.area():.2f}")

        elif opcion == '2':
            largo = input("Ingrese el largo del rectángulo: ")
            ancho = input("Ingrese el ancho del rectángulo: ")
            largo = validar_numero(largo)
            ancho = validar_numero(ancho)
            if largo is not None and ancho is not None:
                rectangulo = RECTANGULO(largo, ancho)
                print(f"El área del rectángulo es: {rectangulo.area():.2f}")

        elif opcion == '3':
            lado = input("Ingrese el lado del cuadrado: ")
            lado = validar_numero(lado)
            if lado is not None:
                cuadrado = CUADRADO(lado)
                print(f"El área del cuadrado es: {cuadrado.area():.2f}")

        elif opcion == '4':
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")


# Ejecutar el menú
if __name__ == '__main__':
    menu()
