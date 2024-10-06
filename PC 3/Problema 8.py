# Definición de las funciones para las operaciones

def suma(a, b):
    try:
        return a + b
    except TypeError:
        return "Error: Tipo de dato no válido."

def resta(a, b):
    try:
        return a - b
    except TypeError:
        return "Error: Tipo de dato no válido."

def producto(a, b):
    try:
        return a * b
    except TypeError:
        return "Error: Tipo de dato no válido."

def division(a, b):
    try:
        if b == 0:
            return "Error: No es posible dividir entre cero."
        return a / b
    except TypeError:
        return "Error: Tipo de dato no válido."

# Ejecución del código
if __name__ == '__main__':
    # Probar las funciones de suma, resta, producto y división
    
    # Suma
    print(f"Suma de 10 y 5: {suma(10, 5)}")
    print(f"Suma de 'a' y 5: {suma('a', 5)}")  # Error esperado
    
    # Resta
    print(f"Resta de 10 y 5: {resta(10, 5)}")
    print(f"Resta de 10 y 'b': {resta(10, 'b')}")  # Error esperado
    
    # Producto
    print(f"Producto de 10 y 5: {producto(10, 5)}")
    print(f"Producto de 10 y 'c': {producto(10, 'c')}")  # Error esperado
    
    # División
    print(f"División de 10 entre 5: {division(10, 5)}")
    print(f"División de 10 entre 0: {division(10, 0)}")  # Error esperado
    print(f"División de 10 entre 'd': {division(10, 'd')}")  # Error esperado
