import mysql.connector 

def criar_conexao (host, usuario, senha, bancoImc):
    return mysql.connector.connect(host=host, user=usuario, password=senha, database=bancoImc, autocommit=True )

def fechar_conexao(con):
    return con.close()