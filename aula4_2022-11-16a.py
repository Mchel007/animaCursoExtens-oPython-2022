#importar biblioteca sqlite3 ( )
import sqlite3

#vamos estabelecer uma conexao com o banco de dados
conexao = sqlite3.connect("dc_universe (1).db")

#criar um objeto do tipo cursor()
cursor = conexao.cursor()

#comando SQL do banco
sql = "SELECT pessoa_id, nome, nome_civil, tipo FROM pessoas"

#executar o comando sqp no sqlite (no cursor) ()
cursor.execute(sql)

#exibir a consuta com todos os nomes de herois e viloes()
pessoas = cursor.fetchall()
for pessoa in pessoas:
  print(pessoa)

for pessoa in pessoas:
  print(f"\nNome: {pessoa[1]} ({pessoa[3]})")
                




