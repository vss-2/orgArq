import sqlite3
from usuario import Usuario
from aposta import Aposta

conector = None
cursor   = None


def init_banco():
        conector = sqlite3.connect(':memory')
        cursor   = conector.cursor()

        cursor.execute("""CREATE TABLE usuario (
		id_usr  INTEGER PRIMARY KEY AUTOINCREMENT,
		email   TEXT,
		nick    TEXT,
		senha   TEXT,
		ponto   INTEGER
		)""")
        
        cursor.execute("""CREATE TABLE aposta (
		partida    TEXT,
		placar     TEXT,
		vencedor   TEXT,
		id_usr     INTEGER,
		FOREIGN KEY (id_usr)
			REFERENCES usuario (id_usr)
		)""")

        return

def print_tudo(cursor_select):
        cursor.fetchall()
        return

def pegar_tudo(banco):
        c = cursor.execute("SELECT * from {}".format(str(banco)))
        return c

def validar_palpite_resultado(partida, vencedor, resultado, pontuacao):
        cursor.execute("UPDATE usuario SET ponto = ponto + {} WHERE aposta = 'PNGxSAN 05/06 15:00' AND vencedor = 'PNG' AND palpite = {}".format(int(pontuacao), str(palpite)))

def validar_palpite(partida, vencedor, pontuacao):
        print('Pontuação antes da alteração: ')
        print_tudo(pegar_tudo('usuario'))
        cursor.execute("UPDATE usuario SET ponto = ponto + {} WHERE aposta = 'PNGxSAN 05/06 15:00' AND vencedor = 'PNG'".format(int(pontuacao)))
        print('Pontuação após alteraçã: ')
        return print_tudo(pegar_tudo('usuario'))
        

# Uso:
# print_tudo(pegar_tudo(banco))