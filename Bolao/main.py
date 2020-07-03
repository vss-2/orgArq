import sqlite3
from usuario import Usuario
from aposta import Aposta

conector = sqlite3.connect(':memory:')
cursor   = conector.cursor()

def novo_usuario(usuario):
	with conector:
		cursor.execute("INSERT INTO usuario VALUES (:id_usr, :email, :nome, :senha, :ponto)",
		{'id_usr': None, 'email': usuario.email, 'nome': usuario.nome, 'senha': usuario.senha, 'ponto': 0})
	return


cursor.execute("""CREATE TABLE usuario (
		id_usr	INTEGER PRIMARY KEY AUTOINCREMENT,
		email	TEXT,
		nick	TEXT,
		senha	TEXT,
		ponto	INTEGER
		)""")

# Usuario contém id(key), email, senha, nick
# e pontuação para tabela

cursor.execute("""CREATE TABLE aposta (
		partida		TEXT,
		placar  	TEXT,
		vencedor	TEXT,
		id_usr		INTEGER,
		FOREIGN KEY (id_usr)
			REFERENCES usuario (id_usr)
		)""")

# Aposta contém id(key do usuário)
# partida: (TIME1xTIME2 DIA/MES HR:MIN)
# venceu: (TIME1/2)
# placar: (#x#)

# Exemplo:
# partida "PNGxSAN 05/06 15:00"
# vencedor  "PNG"
# placar  "1x0"

# partida "PNGxSAN 05/06 15:00"
# vencedor  "SAN"
# placar  "1x0"


usuario1 = Usuario('vss2', 'vitao', '1234')
# cursor.execute("INSERT INTO usuario VALUES (:id_usr, :email, :nick, :senha, :ponto)", 
# {'id_usr': None, 'email': usuario1.email, 'nick': usuario1.nick, 'senha': usuario1.senha, 'ponto': usuario1.ponto})

aposta1 = Aposta(1, "PNGxSAN 05/06 15:00", "SAN", "1x0")