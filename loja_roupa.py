from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Função para obter a lista de categorias do banco de dados
def get_categorias():
    conn = sqlite3.connect('moda_normalizado.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, nome FROM Categoria')
    categorias = cursor.fetchall()
    conn.close()
    return [{"id": row[0], "nome": row[1]} for row in categorias]

# Função para obter produtos por categoria
def get_produtos_por_categoria(categoria_id):
    conn = sqlite3.connect('moda_normalizado.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Produto WHERE categoria_id = ?', (categoria_id,))
    produtos = cursor.fetchall()
    conn.close()
    return produtos

@app.route('/')
def index():
    categorias = get_categorias()
    return render_template('index.html', categorias=categorias)

@app.route('/produtos_por_categoria/<int:categoria_id>')
def produtos_por_categoria(categoria_id):
    produtos = get_produtos_por_categoria(categoria_id)
    return render_template('produtos.html', produtos=produtos)

if __name__ == '__main__': # Verifica se o script está sendo executado diretamente.
    app.run(debug=True) # nicia o servidor de desenvolvimento Flask com o modo de depuração ativado.

