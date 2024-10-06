def fuel_percentage():
    while True:
        try:
            # Solicitar al usuario una fracción en formato X/Y
            fraction = input("Ingrese la fracción de combustible en formato X/Y: ")
            
            # Dividir la fracción en X e Y
            x, y = fraction.split('/')
            
            # Convertir X e Y a enteros
            x = int(x)
            y = int(y)

            # Verificar que Y no sea cero para evitar división entre 0
            if y == 0:
                raise ZeroDivisionError

            # Verificar que X no sea mayor que Y
            if x > y:
                raise ValueError("X no puede ser mayor que Y.")
            
            # Calcular el porcentaje de combustible en el tanque
            percentage = round((x / y) * 100)

            # Determinar el resultado según los casos especiales
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")
            break

        except ValueError:
            print("Error: Ingrese valores enteros y asegúrese de que X <= Y.")
        except ZeroDivisionError:
            print("Error: No se puede dividir por 0.")
        except Exception as e:
            print(f"Error inesperado: {e}")

# Ejecutar el programa principal
if __name__ == "__main__":
    fuel_percentage()
