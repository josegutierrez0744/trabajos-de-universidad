import requests

respuesta = requests.get('https://swapi.dev/api/planets/?page=2')
if respuesta.ok:
    planeta_data = respuesta.json()
    numero_de_peliculas = sum([len(planeta['films']) for planeta in planeta_data['results']])
    print(f"En {numero_de_peliculas} películas aparecen planetas cuyo clima es árido.")
else:
    print("No se encuentra esa informacion en el api")

respuesta = requests.get('https://swapi.dev/api/films/3/')
if respuesta.ok:
    data_film = respuesta.json()
    numero_de_wookies = sum([1 for character in data_film['characters'] if 'wookie' in requests.get(character).json()['species']])
    print(f"En el episodio 3 aparecen {numero_de_wookies} Wookies.")
else:
    print("No se encuentra esa informacion en el api")


respuesta = requests.get('https://swapi.dev/api/vehicles/')
if respuesta.ok:
    vehiculo_grande = max(respuesta.json()['results'], key=lambda vehicle: vehicle['length'])
    print(f"El vehiculo más grande de toda la saga es : {vehiculo_grande['name']}.")
else:
    print("No se encuentra esa informacion en el api")
