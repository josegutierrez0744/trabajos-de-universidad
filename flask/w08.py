from flask import Flask, render_template, request
import pymongo

app = Flask(__name__)
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['w08']
collection = db['diccionario']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/lista')
def lista_palabra():
    palabras = collection.find()
    return render_template('lista_palabra.html', palabras=palabras)

@app.route('/agregar', methods=['GET', 'POST'])
def agregar_palabra():
    error = None
    if request.method == 'POST':
        palabra = request.form['palabra']
        significado = request.form['significado']
        palabra_existente = collection.find_one({'palabra': palabra})
        if palabra_existente is None:
            collection.insert_one({'palabra': palabra, 'significado': significado})
            return render_template('index.html')
        else:
            error = 'La palabra "{}" ya existe en el diccionario.'.format(palabra)
    return render_template('agregar_palabra.html', error=error)

@app.route('/editar', methods=['GET', 'POST'])
def editar_palabra(palabra):
    palabra_existente = collection.find_one({'palabra': palabra})
    if palabra_existente is None:
        return render_template('index.html')
    else:
        significado = palabra['significado']
        if request.method == 'POST':
            nuevo_significado = request.form['significado']
            collection.update_one({'palabra': palabra}, {'$set': {'significado': nuevo_significado}})
            return render_template('index.html')
        return render_template('editar_palabra.html', palabra=palabra, significado=significado)

@app.route('/eliminar', methods=['GET', 'POST'])
def eliminar_palabra(palabra):
    palabra_existente = collection.find_one({'palabra': palabra})
    if palabra_existente is None:
        return render_template('index.html')
    else:
        if request.method == 'POST':
            collection.delete_one({'palabra': palabra})
            return render_template('index.html')
        return render_template('eliminar_palabra.html', palabra=palabra)

@app.route('/buscar', methods=['GET', 'POST'])
def buscar_palabra():
    if request.method == 'POST':
        palabra = request.form['palabra']
        palabra_existente = collection.find_one({'palabra': palabra})
        if palabra_existente is not None:
            return render_template('buscar_palabra.html', palabra=palabra, significado=palabra_existente['significado'])
    return render_template('buscar_palabra.html') 

if __name__ == '__main__':
    app.run(debug=True)
