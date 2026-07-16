#Aqui é onde vamos gerenciar o banco de dados
#from flask import sqlalchemy

import pymysql as bd

conexao = bd.connect(host='localhost',
                     user='root',
                     password='admin',
                     database='Lumina',
                     charset='utf8mb4')

while True:
    nome = input("Informe o nome da equipe: ")
    titulos = int(input("Quantos titulos mundiais? "))
    cursor = conexao.cursor()
    cursor.execute(f"insert into Equipe values('{nome}', {titulos});")
    conexao.commit()

    resposta = input("Cadastrar mais? (s/n) ")
    if resposta == "n":
        conexao.close()