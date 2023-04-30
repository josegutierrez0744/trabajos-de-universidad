import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client['w09']
collection = db['producto']

def registrar_articulo():
    nombre = input("Nombre del artículo: ")
    precio = float(input("Ingrese el precio del arituclo: "))
    cantidad = int(input("Cantidad disponible: "))
    producto = {'nombre': nombre, 'precio': precio, 'cantidad': cantidad}
    collection.insert_one(producto)
    print(f"El producto se agrego de manera exitosa")
    print()

def buscar_articulo():
    nombre = input("Nombre del producto a buscar: ")
    producto = collection.find_one({'nombre': nombre})
    if producto:
        print()
        print(f"ID: {producto['_id']}")
        print(f"Nombre: {producto['nombre']}")
        print(f"Precio: {producto['precio']}")
        print(f"Cantidad: {producto['cantidad']}")
        print()
    else:
        print("Producto no encontrado")
        print()

def editar_articulo():
    nombre = input("Nombre del producto que desea modificar: ")
    producto = collection.find_one({'nombre': nombre})
    if producto:
        nombre = input(f"Nuevo nombre ({producto['nombre']}): ") or producto['nombre']
        precio = float(input(f"Nuevo precio ({producto['precio']}): ")) or producto['precio']
        cantidad = int(input(f"Nueva cantidad ({producto['cantidad']}): ")) or producto['cnatidad']
        collection.update_one({'nombre': nombre}, {'$set': {'nombre': nombre, 'precio': precio, 'cantidad': cantidad}})
        print("Producto actualizado")
        print()        
    else:
        print("Producto no encontrado")
        print()

def eliminar_articulo():
    nombre = input("Ingresa el nombre del producto que quieres eliminar: ")
    producto = collection.find_one({'nombre': nombre})
    if producto:
        collection.delete_one({"nombre": nombre})
        print("Producto eliminado")
        print()
    else:
        print("No se eliminó ningún producto")
        print()

def menu():
    print("1. Registrar producto")
    print("2. Buscar producto")
    print("3. Editar producto")
    print("4. Eliminar prducto")
    print("5. Salir") 

while True:
    menu()
    opcion = input("Seleccione una opción: ")
    if opcion == '1':
        registrar_articulo()
    elif opcion == '2':
        buscar_articulo()
    elif opcion == '3':
        editar_articulo()
    elif opcion == '4':
        eliminar_articulo()
    elif opcion == '5':
        print("Usted ha salido del inventario")
        break
    else:
        print("Opcion invalida")
        print() 
