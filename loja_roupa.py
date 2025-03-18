from flask import Flask, render_template # Chama o módulo flask e importa apenas as funções Flask e render_template.

import sqlite3

app = Flask(__name__) # Instânciamento principal do Flask para criação de uma aplicação

def pegar_tecidos():
    conn = sqlite3.connect('moda_normalizado.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Tecidos')
    tecidos = cursor.fetchall()
    conn.close()
    return tecidos

#@app.route('/')
#def home():
#    return render_template('index.html')

@app.route('/') # Define uma rota para a URL raiz '/'
def home(): # Define a função que será chamada quando a rota raiz for acessada.
    tecidos = pegar_tecidos()
    return render_template('index.html', tecidos=tecidos) # Retorna o conteúdo html

@app.route('/produtos') # Define uma rota para a URL raiz '/produtos
def produtos(): # Define a função que será chamada quando a rota raiz for acessada.
    return render_template('produtos.html') # Retorna o conteúdo html

@app.route('/contato') # Define uma rota para a URL raiz '/contato'
def contato(): # Define a função que será chamada quando a rota raiz for acessada.
    return render_template('contato.html') # Retorna o conteúdo html

if __name__ == 'main': # Verifica se o script está sendo executado diretamente.
    app.run(debug=True) # nicia o servidor de desenvolvimento Flask com o modo de depuração ativado.
