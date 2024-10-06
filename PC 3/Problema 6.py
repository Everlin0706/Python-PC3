# Clase Producto
class Producto:
    def __init__(self, nombre, precio, año):
        self.nombre = nombre
        self.precio = self.validar_precio(precio)
        self.año = self.validar_año(año)

    def validar_precio(self, precio):
        """
        Función para validar que el precio sea positivo.
        """
        if isinstance(precio, (int, float)) and precio > 0:
            return precio
        else:
            raise ValueError("El precio debe ser un número positivo.")

    def validar_año(self, año):
        """
        Función para validar que el año sea un número válido.
        """
        if isinstance(año, int) and año > 0:
            return año
        else:
            raise ValueError("El año debe ser un número entero positivo.")

    def mostrar_informacion(self):
        """
        Método para mostrar la información del producto.
        """
        return f"Producto: {self.nombre}, Precio: ${self.precio}, Año: {self.año}"

# Clase Catálogo
class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        """
        Método para agregar un producto al catálogo.
        """
        self.productos.append(producto)

    def mostrar_productos(self):
        """
        Método para mostrar todos los productos del catálogo.
        """
        if self.productos:
            for producto in self.productos:
                print(producto.mostrar_informacion())
        else:
            print("El catálogo está vacío.")

    def filtrar_por_año(self, año):
        """
        Funcionalidad extra: Filtrar productos por año.
        """
        productos_filtrados = [p for p in self.productos if p.año == año]
        if productos_filtrados:
            for producto in productos_filtrados:
                print(producto.mostrar_informacion())
        else:
            print(f"No se encontraron productos del año {año}.")

    def buscar_por_precio_maximo(self, precio_max):
        """
        Funcionalidad extra: Buscar productos cuyo precio sea menor o igual al precio máximo dado.
        """
        productos_filtrados = [p for p in self.productos if p.precio <= precio_max]
        if productos_filtrados:
            for producto in productos_filtrados:
                print(producto.mostrar_informacion())
        else:
            print(f"No se encontraron productos con un precio menor o igual a ${precio_max}.")

if __name__ == '__main__':
    # Crear el catálogo
    catalogo = Catalogo()

    try:
        # Crear 3 productos
        producto1 = Producto("Filtro de Aceite", 150.0, 2022)
        producto2 = Producto("Batería 12V", 1200.0, 2020)
        producto3 = Producto("Neumático 15 pulgadas", 800.0, 2021)

        # Agregar productos al catálogo
        catalogo.agregar_producto(producto1)
        catalogo.agregar_producto(producto2)
        catalogo.agregar_producto(producto3)

        # Mostrar todos los productos
        print("\nTodos los productos en el catálogo:")
        catalogo.mostrar_productos()

        # Filtrar productos por año
        print("\nProductos del año 2021:")
        catalogo.filtrar_por_año(2021)

        # Buscar productos por precio máximo
        print("\nProductos con precio menor o igual a $900:")
        catalogo.buscar_por_precio_maximo(900)

    except ValueError as e:
        print(f"Error: {e}")
