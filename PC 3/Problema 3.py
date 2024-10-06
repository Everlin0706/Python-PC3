import math

class Circulo:
    def __init__(self, radio):
        # Validar que el radio sea positivo y numérico
        if isinstance(radio, (int, float)) and radio > 0:
            self.radio = radio
        else:
            raise ValueError("El radio debe ser un número positivo.")
    
    def calcular_area(self):
        # Calcular el área del círculo: A = π * r^2
        return math.pi * self.radio ** 2

if __name__ == '__main__':
    try:
        # Crear el primer objeto Circulo con manejo de errores
        radio1 = float(input("Ingrese el radio del primer círculo: "))
        circulo1 = Circulo(radio1)
        print(f"El área del primer círculo es: {circulo1.calcular_area():.2f}")

        # Crear el segundo objeto Circulo con manejo de errores
        radio2 = float(input("Ingrese el radio del segundo círculo: "))
        circulo2 = Circulo(radio2)
        print(f"El área del segundo círculo es: {circulo2.calcular_area():.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")
