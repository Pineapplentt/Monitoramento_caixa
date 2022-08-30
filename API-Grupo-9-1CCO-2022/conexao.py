import mysql.connector #Importando a biblioteca responsável por conectar o python ao mysql local

# Autocommit serve para garantir que os comandos serão executados dentro do SQL
def criar_conexao (host, usuario, senha, nomeDoBD):
    return mysql.connector.connect(host=host, user=usuario, password=senha, database=nomeDoBD, autocommit=True )

def fechar_conexao(con):
    return con.close()