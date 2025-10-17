from decimal import Decimal
from productos.models import Producto

# a) CREAR por shell
producto = Producto(
    nombre = "Desodorante",
    descripcion = "Olor chocolate",
    precio = 1000,
    stock = 10
)
producto.save()


Producto.objects.create(
    nombre = "Shampoo de Mascota",
    descripcion = "Shampoo para perritos y gatitos",
    precio = 500.00,
    stock = 5
)

producto = Producto(
    nombre = "laca",
    descripcion = "para fijar tu peinado",
    precio = 8000,
    stock = 35
)
producto.save()

Producto.objects.create(
    nombre = "crema de cuerpo",
    descripcion = "propiedades nutritivas",
    precio = 6000,
    stock = 6
)

#listar por shell
#Obtener TODOS -> Producto.objects.all()


#Obtener una lista de productos WHERE -> Producto.objects.filter()
producto1 = Producto.objects.get(id=1) #nombre = "Desodorante"
print(producto1, producto1.descripcion, producto.precio, producto1.stock)

#actualizar por shell
producto1.precio = 989

#guardar el nuevo precio 
producto1.save()
#borrar producto
producto1.delete()