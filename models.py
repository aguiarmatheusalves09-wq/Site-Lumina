#Aqui é onde vamos gerenciar o banco de dados

import pymysql as bd

conexao = bd.connect(host='localhost',
                     user='root',
                     password='admin',
                     database='Lumina',
                     charset='utf8mb4')

banco = conexao.cursor()
banco.execute("select * from usuario;")

banco.fetchall() #traz um vetor

for linha in banco.fetchall():
    print(linha[0], linha[1])

banco.execute("insert into usuario values(...);")
banco.execute("commit;") #faz com que o banco de dados confie no programa externo(esse no caso) 

#conexao.commit()
conexao.close()