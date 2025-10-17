Detalles Ejercicio
el ejercioio esta desarrollado para ejecutarse en la terminal o shell,
en el desarrollo hay una carpeta llamada proceso que tiene pantallazos del proceso y un texto con el paso a paso 

el ejercicio planteado era :


***************************

Objetivo

Configurar Django para conectarse a una base de datos MySQL y aplicar operaciones CRUD (Crear, Leer, Actualizar y Borrar) utilizando el ORM de Django.

Instrucciones

Instalación de dependencias
Instala el conector necesario para usar MySQL con Django (mysqlclient).

Creación de un proyecto Django
Crea un nuevo proyecto llamado mi_proyecto.

Configuración de la conexión a MySQL
Edita el archivo settings.py del proyecto para que la base de datos utilice MySQL. Asegúrate de tener creada previamente una base de datos en tu servidor MySQL.

Creación de una aplicación Django
Crea una nueva aplicación dentro del proyecto llamada productos. Agrega esta aplicación a la lista INSTALLED_APPS en el archivo settings.py.

Creación del modelo en Django (ORM)
Dentro del archivo models.py de la aplicación productos, define un modelo llamado Producto con los siguientes atributos:

nombre: Cadena de caracteres única.

descripcion: Texto largo.

precio: Número decimal con dos decimales.

stock: Número entero.

fecha_creacion: Fecha de creación automática al momento de guardar.

Aplicación de migraciones
Genera las migraciones correspondientes y aplícalas para que el modelo se cree en la base de datos.

Operaciones CRUD con el ORM de Django
Utiliza la consola interactiva de Django (Django Shell) para realizar las siguientes operaciones:

a) Crear un producto con valores definidos y guardarlo en la base de datos.
b) Consultar el producto creado y mostrar sus detalles.
c) Modificar el precio del producto y guardar los cambios.
d) Eliminar el producto de la base de datos.



****************************