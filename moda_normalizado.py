import sqlite3

# Conectar ao banco de dados (ou criá-lo se não existir)
conn = sqlite3.connect('moda_normalizado.db')

# Criar um cursor
cursor = conn.cursor()

# Criar tabela para Categorias
cursor.execute('''
CREATE TABLE IF NOT EXISTS Categorias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE
)
''')

# Inserir dados na tabela Categorias
categorias = [
    'Reta', 'Camiseta', 'Cropped', 'Longo', 'Midi', 'Tops', 'Festa', 'Pantalona', 'Mini', 'Curto'
]
cursor.executemany('INSERT INTO Categorias (nome) VALUES (?)', [(categoria,) for categoria in categorias])

# Criar tabela para Cores
cursor.execute('''
CREATE TABLE IF NOT EXISTS Cores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE
)
''')
# Inserir dados na tabela Cores

cores = [
    'Cinza', 'Roxo', 'Animal Print', 'Multicolor', 'Branco', 'Marrom', 'Rosa', 'Vermelho', 'Azul', 'Amarelo',
    'Bege', 'Laranja', 'Preto', 'Verde'
]
cursor.executemany('INSERT INTO Cores (nome) VALUES (?)', [(cor,) for cor in cores])

# Criar tabela para Tamanhos
cursor.execute('''
CREATE TABLE IF NOT EXISTS Tamanhos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE
)
''')
# Inserir dados na tabela Tamanhos

tamanhos = ['M/40', 'G/42', 'GG/44', 'U']
cursor.executemany('INSERT INTO Tamanhos (nome) VALUES (?)', [(tamanho,) for tamanho in tamanhos])

# Criar tabela para Tecidos
cursor.execute('''
CREATE TABLE IF NOT EXISTS Tecidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE
)
''')
# Inserir dados na tabela Tecidos

tecidos = ['Lamê', 'Linho', 'Algodão', 'Bordado', 'Laise', 'Jeans']
cursor.executemany('INSERT INTO Tecidos (nome) VALUES (?)', [(tecido,) for tecido in tecidos])

# Criar tabela para Ocasioes
cursor.execute('''
CREATE TABLE IF NOT EXISTS Ocasioes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE
)
''')
# Inserir dados na tabela Ocasioes

ocasioes = ['Festa', 'Casual', 'Noivas', 'Casamentos', 'Formatura', 'Eventos Sociais']
cursor.executemany('INSERT INTO Ocasioes (nome) VALUES (?)', [(ocasiao,) for ocasiao in ocasioes])

# Criar tabela para Roupas
cursor.execute('''
CREATE TABLE IF NOT EXISTS Roupas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    categoria_id INTEGER,
    FOREIGN KEY (categoria_id) REFERENCES Categorias(id)
)
''')
# Inserir dados na tabela Roupas
roupas = [
    ('Vestidos', 1), ('Casacos', 2), ('Shorts', 3), ('Calças', 4), ('Saias', 5), ('Tricot', 6),
    ('Blusas', 7), ('Couro', 8)
]
cursor.executemany('INSERT INTO Roupas (nome, categoria_id) VALUES (?, ?)', roupas)

# Criar tabela para Roupas_Ocasioes
cursor.execute('''
CREATE TABLE IF NOT EXISTS Roupas_Ocasioes (
    roupa_id INTEGER,
    ocasiao_id INTEGER,
    FOREIGN KEY (roupa_id) REFERENCES Roupas(id),
    FOREIGN KEY (ocasiao_id) REFERENCES Ocasioes(id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Roupas_Ocasioes (
    roupa_id INTEGER,
    ocasiao_id INTEGER,
    FOREIGN KEY (roupa_id) REFERENCES Roupas(id),
    FOREIGN KEY (ocasiao_id) REFERENCES Ocasioes(id)
)
''')

# Inserir dados na tabela Roupas_Ocasioes
roupas_ocasioes = [
    (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
    (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6),
    (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6),
    (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6),
    (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6),
    (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6),
    (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6),
    (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6)
]
cursor.executemany('INSERT INTO Roupas_Ocasioes (roupa_id, ocasiao_id) VALUES (?, ?)', roupas_ocasioes)

# Comitar as mudanças
conn.commit()

# Fechar a conexão
conn.close()
