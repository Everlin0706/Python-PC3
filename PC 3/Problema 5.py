class Alumno:
    def __init__(self, nombre, numero_registro):
        # Inicialización de los atributos nombre y número de registro
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.nota = None

    def display(self):
        """
        Método para mostrar toda la información del alumno.
        """
        print(f"Nombre: {self.nombre}")
        print(f"Número de Registro: {self.numero_registro}")
        print(f"Edad: {self.edad if self.edad else 'No asignada'}")
        print(f"Nota: {self.nota if self.nota else 'No asignada'}")

    def set_age(self, edad):
        """
        Método para asignar la edad al alumno, validando que sea un número positivo.
        """
        if isinstance(edad, int) and edad > 0:
            self.edad = edad
        else:
            raise ValueError("La edad debe ser un número entero positivo.")

    def set_nota(self, nota):
        """
        Método para asignar la nota al alumno, validando que sea un número entre 0 y 100.
        """
        if isinstance(nota, (int, float)) and 0 <= nota <= 100:
            self.nota = nota
        else:
            raise ValueError("La nota debe ser un número entre 0 y 100.")

def crear_alumno():
    """
    Función para crear un objeto Alumno con manejo de errores.
    """
    try:
        nombre = input("Ingrese el nombre del alumno: ")
        numero_registro = input("Ingrese el número de registro: ")
        alumno = Alumno(nombre, numero_registro)
        return alumno
    except Exception as e:
        print(f"Error al crear el alumno: {e}")
        return None

def asignar_edad(alumno):
    """
    Función para asignar la edad a un alumno con manejo de errores.
    """
    try:
        edad = int(input("Ingrese la edad del alumno: "))
        alumno.set_age(edad)
    except ValueError as e:
        print(f"Error al asignar la edad: {e}")

def asignar_nota(alumno):
    """
    Función para asignar la nota a un alumno con manejo de errores.
    """
    try:
        nota = float(input("Ingrese la nota del alumno: "))
        alumno.set_nota(nota)
    except ValueError as e:
        print(f"Error al asignar la nota: {e}")

if __name__ == '__main__':
    # Crear el objeto Alumno
    alumno = crear_alumno()
    
    if alumno:
        # Mostrar la información del alumno
        alumno.display()
        
        # Asignar la edad con manejo de errores
        asignar_edad(alumno)
        
        # Asignar la nota con manejo de errores
        asignar_nota(alumno)
        
        # Mostrar la información actualizada del alumno
        print("\nInformación actualizada del alumno:")
        alumno.display()
