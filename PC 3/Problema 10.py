class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

    def __str__(self):
        return f"Titulo: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}"

class GestionBiblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        if isinstance(libro, Libro):
            self.libros.append(libro)
            print("Libro agregado exitosamente.")
        else:
            print("Error: El objeto no es de tipo Libro.")

    def listar_libros(self):
        if not self.libros:
            print("No hay libros en la biblioteca.")
        else:
            for libro in self.libros:
                print(libro)

    def buscar_por_titulo(self, titulo):
        encontrados = [libro for libro in self.libros if libro.titulo.lower() == titulo.lower()]
        if encontrados:
            for libro in encontrados:
                print(libro)
        else:
            print("No se encontró ningún libro con ese título.")

    def buscar_por_autor(self, autor):
        encontrados = [libro for libro in self.libros if libro.autor.lower() == autor.lower()]
        if encontrados:
            for libro in encontrados:
                print(libro)
        else:
            print("No se encontró ningún libro de ese autor.")

def menu():
    biblioteca = GestionBiblioteca()

    while True:
        print("\n--- Menú de Gestión de Biblioteca ---")
        print("1. Agregar un libro")
        print("2. Listar todos los libros")
        print("3. Buscar libro por título")
        print("4. Buscar libro por autor")
        print("5. Salir")
        
        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                titulo = input("Ingrese el título del libro: ")
                autor = input("Ingrese el autor del libro: ")
                isbn = input("Ingrese el ISBN del libro: ")
                libro = Libro(titulo, autor, isbn)
                biblioteca.agregar_libro(libro)

            elif opcion == 2:
                biblioteca.listar_libros()

            elif opcion == 3:
                titulo = input("Ingrese el título del libro a buscar: ")
                biblioteca.buscar_por_titulo(titulo)

            elif opcion == 4:
                autor = input("Ingrese el autor del libro a buscar: ")
                biblioteca.buscar_por_autor(autor)

            elif opcion == 5:
                print("Saliendo del programa...")
                break

            else:
                print("Opción no válida. Por favor, elija una opción entre 1 y 5.")

        except ValueError:
            print("Error: Por favor, ingrese un número válido.")

if __name__ == '__main__':
    menu()
