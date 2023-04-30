from flask import Flask, render_template, request, redirect, url_for
import pymongo

app = Flask(__name__)
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['dictionary']
collection = db['words']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/words')
def list_words():
    words = collection.find()
    return render_template('list_words.html', words=words)

@app.route('/words/add', methods=['GET', 'POST'])
def add_word():
    error = None
    if request.method == 'POST':
        word = request.form['word']
        definition = request.form['definition']
        existing_word = collection.find_one({'word': word})
        if existing_word is None:
            collection.insert_one({'word': word, 'definition': definition})
            return redirect(url_for('list_words'))
        else:
            error = 'La palabra "{}" ya existe en el diccionario.'.format(word)
    return render_template('add_word.html', error=error)

@app.route('/edit/<word>', methods=['GET', 'POST'])
def edit_word(word):
    existing_word = collection.find_one({'word': word})
    if existing_word is None:
        return redirect(url_for('list_words'))
    else:
        definition = existing_word['definition']
        if request.method == 'POST':
            new_definition = request.form['definition']
            collection.update_one({'word': word}, {'$set': {'definition': new_definition}})
            return redirect(url_for('list_words'))
        return render_template('edit_word.html', word=word, definition=definition)

@app.route('/delete/<word>', methods=['GET', 'POST'])
def delete_word(word):
    existing_word = collection.find_one({'word': word})
    if existing_word is None:
        return redirect(url_for('list_words'))
    else:
        if request.method == 'POST':
            collection.delete_one({'word': word})
            return redirect(url_for('list_words'))
        return render_template('delete_word.html', word=word)

@app.route('/words/search', methods=['GET', 'POST'])
def search_word():
    if request.method == 'POST':
        word = request.form['word']
        existing_word = collection.find_one({'word': word})
        if existing_word is not None:
            return render_template('search_word.html', word=word, definition=existing_word['definition'])
    return render_template('search_word.html')

if __name__ == '__main__':
    app.run(debug=True)
