import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["w10"]
collection = db["dictionario"]

def agregarpalabra():
    palabra = input("Ingresa la palabra: ")
    documento = collection.find_one({"palabra": palabra})
    if documento:
     print("la palabra\t"+palabra+"\tya existe")
     print()
    else:
     significado = input("Ingresa el significado: ")
     collection.insert_one({"palabra": palabra, "significado": significado})
     print("La palabra se ha agregado correctamente")
     print()
    
def editarpalabra():
    palabra = input("Ingresa la palabra que quieres editar: ")
    documento = collection.find_one({"palabra": palabra})
    if documento:
        nuevo_significado = input("Ingresa el nuevo significado: ")
        collection.update_one({"palabra": palabra}, {"$set": {"significado": nuevo_significado}})
        print("La palabra se ha actualizado correctamente")
        print()
    else:
        print("La palabra no existe en el diccionario")
        print()

def eliminarpalabra():
    palabra = input("Ingresa la palabra que quieres eliminar: ")
    documento = collection.find_one({"palabra": palabra})
    if documento:
        collection.delete_one({"palabra": palabra})
        print("La palabra se ha eliminado correctamente")
        print()
    else:
        print("La palabra no existe en el diccionario")
        print()
    
def listasdepalabra():
    cursor = collection.find()
    for documento in cursor:
        print(documento["palabra"])
        print()

def buscarsignificado():
    palabra = input("Ingresa la palabra que quieres buscar: ")
    documento = collection.find_one({"palabra": palabra})
    if documento:
        print(documento["significado"])
        print()
    else:
        print("La palabra no existe en el diccionario")
        print()


def menu():
    print("Bienvenido al diccionario.")
    print("Seleccione una opcion:")
    print("a) Agregar nueva palabra")
    print("b) Editar palabra existente")
    print("c) Eliminar palabra existente")
    print("d) Ver listado de palabras")
    print("e) Buscar significado de palabra")
    print("f) Salir")

while True:
    menu()
    opcion = input("Ingresa tu opción: ")
    if opcion == "a":
        agregarpalabra()
    elif opcion == "b":
        editarpalabra()
    elif opcion == "c":
        eliminarpalabra()
    elif opcion == "d":
        listasdepalabra()
    elif opcion == "e":
        buscarsignificado()
    elif opcion == "f":
        print("Vuelva pronto")
        break
    else:
        print("Opción inválida.")
        print()