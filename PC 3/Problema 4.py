# Definir la clase Rectangulo
class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = self.validar_valor(largo, 'largo')
        self.ancho = self.validar_valor(ancho, 'ancho')

    def validar_valor(self, valor, nombre_atributo):
        """
        Función para validar que un valor sea un número positivo.
        """
        if isinstance(valor, (int, float)) and valor > 0:
            return valor
        else:
            raise ValueError(f"El {nombre_atributo} debe ser un número positivo.")

    def calcular_area(self):
        """
        Función que calcula el área del rectángulo.
        """
        return self.largo * self.ancho

# Clase Cuadrado que hereda de Rectangulo
class Cuadrado(Rectangulo):
    def __init__(self, lado):
        # Se reutiliza la validación y el cálculo de área de la clase Rectangulo
        super().__init__(lado, lado)

def crear_rectangulo():
    """
    Función para crear un rectángulo a partir de la entrada del usuario con manejo de errores.
    """
    try:
        largo = float(input("Ingrese el largo del rectángulo: "))
        ancho = float(input("Ingrese el ancho del rectángulo: "))
        rectangulo = Rectangulo(largo, ancho)
        return rectangulo
    except ValueError as e:
        print(f"Error: {e}")
        return None

def crear_cuadrado():
    """
    Función para crear un cuadrado a partir de la entrada del usuario con manejo de errores.
    """
    try:
        lado = float(input("Ingrese el lado del cuadrado: "))
        cuadrado = Cuadrado(lado)
        return cuadrado
    except ValueError as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    # Crear un objeto Rectángulo
    rectangulo = crear_rectangulo()
    if rectangulo:
        print(f"El área del rectángulo es: {rectangulo.calcular_area():.2f}")
    
    # Crear un objeto Cuadrado
    cuadrado = crear_cuadrado()
    if cuadrado:
        print(f"El área del cuadrado es: {cuadrado.calcular_area():.2f}")
