import math

# Clase Punto
class Punto:
    def __init__(self, x=0, y=0):
        """
        Inicializa un punto con coordenadas X e Y.
        Si no se proporcionan, por defecto será el origen (0,0).
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        Sobrescribe el método __str__ para imprimir el punto en formato (X, Y).
        """
        return f"({self.x}, {self.y})"

    def cuadrante(self):
        """
        Método que indica a qué cuadrante pertenece el punto.
        """
        if self.x > 0 and self.y > 0:
            return "El punto está en el primer cuadrante."
        elif self.x < 0 and self.y > 0:
            return "El punto está en el segundo cuadrante."
        elif self.x < 0 and self.y < 0:
            return "El punto está en el tercer cuadrante."
        elif self.x > 0 and self.y < 0:
            return "El punto está en el cuarto cuadrante."
        elif self.x == 0 and self.y != 0:
            return "El punto está sobre el eje Y."
        elif self.x != 0 and self.y == 0:
            return "El punto está sobre el eje X."
        else:
            return "El punto está en el origen."

    def vector(self, otro_punto):
        """
        Método que calcula el vector entre este punto y otro punto.
        """
        return f"Vector: ({otro_punto.x - self.x}, {otro_punto.y - self.y})"

    def distancia(self, otro_punto):
        """
        Método que calcula la distancia entre este punto y otro punto.
        """
        return math.sqrt((otro_punto.x - self.x) ** 2 + (otro_punto.y - self.y) ** 2)

# Clase Rectangulo
class Rectangulo:
    def __init__(self, punto_inicial=Punto(), punto_final=Punto()):
        """
        Inicializa el rectángulo con dos puntos (punto inicial y punto final).
        Si no se proporcionan, se inicializa en el origen.
        """
        self.punto_inicial = punto_inicial
        self.punto_final = punto_final

    def base(self):
        """
        Método que calcula la base del rectángulo (diferencia en las coordenadas X).
        """
        return abs(self.punto_final.x - self.punto_inicial.x)

    def altura(self):
        """
        Método que calcula la altura del rectángulo (diferencia en las coordenadas Y).
        """
        return abs(self.punto_final.y - self.punto_inicial.y)

    def area(self):
        """
        Método que calcula el área del rectángulo (base * altura).
        """
        return self.base() * self.altura()

if __name__ == '__main__':
    # Crear algunos puntos
    punto1 = Punto(2, 3)
    punto2 = Punto(5, 5)
    punto3 = Punto(-3, -4)
    
    # Mostrar puntos
    print("Punto 1:", punto1)
    print("Punto 2:", punto2)
    print("Punto 3:", punto3)

    # Mostrar cuadrante de los puntos
    print(punto1.cuadrante())
    print(punto2.cuadrante())
    print(punto3.cuadrante())

    # Calcular y mostrar el vector entre punto1 y punto2
    print(punto1.vector(punto2))

    # Calcular y mostrar la distancia entre punto1 y punto2
    print(f"Distancia entre Punto 1 y Punto 2: {punto1.distancia(punto2):.2f}")

    # Crear un rectángulo
    rectangulo = Rectangulo(punto1, punto2)

    # Mostrar la base, altura y área del rectángulo
    print(f"Base del rectángulo: {rectangulo.base()}")
    print(f"Altura del rectángulo: {rectangulo.altura()}")
    print(f"Área del rectángulo: {rectangulo.area()}")
