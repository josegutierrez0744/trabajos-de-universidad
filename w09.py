import redis

r= redis.StrictRedis(host='localhost', port=6379, db=0)

def agregarpalabra():
    palabra = input("Introdusca una palabra: ")
    if r.exists(palabra):
      print("La palabra\t"+palabra+"\tya existe")
      print()
    else:
     significado = input("Introdusca un significado: ")
     r.set(palabra,significado)
     print("La palabra se agrego exisitosamente")
     print()

def editarpalabra():
  palabra = input("Introdusca una palabra:")
  if r.exists(palabra):
     nuevosignificado = input("Introdusca nuevo significado: ")
     r.set(palabra,nuevosignificado)
     print("Se actualizo de forma exsitosa la palabra")
     print()
  else:
    print("La palabra no se encuentra en el diccionario")
    print()

def eliminarpalabra():
  palabra=input("Introdusca una palabra: ")
  if r.exists(palabra):
     r.delete(palabra)
     print("Se elimino la palabra del diccionario")
     print()
  else:
    print("La palabra no se encuentra en el diccionario")
    print()

def listasdepalabra():
  palabras = r.keys("*")
  if palabras:
     print("Lista de palabras:")
     for palabra in palabras:
       print(palabra.decode())
       print()
  else:
    print("El diccionario esta vacio")
    print()

def buscarsignificado():
  palabra = input("Ingresa la palabra que deseas saber el significado: ")
  significado = r.get(palabra)
  if significado:
     print("El significado de la palabra es: {}".format(significado.decode()))
     print()
  else:
        print("La palabra no se encuentra en el diccionario")
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