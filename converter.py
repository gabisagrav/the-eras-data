import csv
import sqlite3
import os

pasta = "Albuns"
db_file = "lyrics.db"

conn = sqlite3.connect(db_file)
cur = conn.cursor()

for arquivo in os.listdir(pasta):
    if arquivo.endswith(".csv"):
        caminho = os.path.join(pasta, arquivo)
        nome_tabela = os.path.splitext(arquivo)[0]

        with open(caminho, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            headers = next(reader)

            cur.execute(f'DROP TABLE IF EXISTS "{nome_tabela}"')

            colunas = ', '.join([f'"{h}" TEXT' for h in headers])
            cur.execute(f'CREATE TABLE "{nome_tabela}" ({colunas})')

            placeholders = ', '.join(['?'] * len(headers))
            sql = f'INSERT INTO "{nome_tabela}" VALUES ({placeholders})'
            cur.executemany(sql, reader)

conn.commit()
conn.close()

print("Todos os álbuns foram importados para albuns.db")