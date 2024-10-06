def procesar_calificaciones(cadena_calificaciones):
    try:
        # Dividir la cadena en calificaciones individuales
        lista_calificaciones = cadena_calificaciones.split(',')
        # Convertir cada calificación a un número entero
        lista_calificaciones_enteros = [int(calificacion) for calificacion in lista_calificaciones]
        return lista_calificaciones_enteros
    except ValueError as e:
        # Informar al usuario si ocurre un error al convertir a entero
        print(f"Error: Una o más calificaciones no son válidas. {e}")
        return None

if __name__ == '__main__':
    # Solicitar al usuario una lista de calificaciones
    calificaciones_usuario = input("Ingrese una lista de calificaciones separadas por comas: ")
    # Procesar las calificaciones
    resultado = procesar_calificaciones(calificaciones_usuario)
    if resultado:
        print(f"Las calificaciones en formato entero son: {resultado}")
