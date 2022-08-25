import mysql.connector # Tem que baixar e importar a biblioteca para conectar no banco

def criar_conexao (host, usuario, senha, nomeBanco):
    return mysql.connector.connect(host=host, user=usuario, password=senha, database=nomeBanco, autocommit=True )

def fechar_conexao(con):
    return con.close()