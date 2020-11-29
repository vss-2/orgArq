import os.path
import sqlite3
from Empregado import Empregado

conector = sqlite3.connect('empresa.db')
# Caso queira executar na memória (limpa sempre que fechado/aberto)
# conector = sqlite3.connect(':memory:')

####################################################################
############################# CRUD #################################
def inserir_emp(emp):
    # Fechando o arquivo com with
    with conector:
        cursor.execute("INSERT INTO empresa VALUES (:nome, :salario, :admissao, :demissao)", 
        {'nome': emp.nome, 'salario': emp.salario, 'admissao': emp.admissao, 'demissao': emp.demissao})
    return

def buscar_nome(nome):
    cursor.execute("SELECT * FROM empresa WHERE nome=:nome", {'nome': 'Joao Silva'})
    return c.fetchone()

def atualizar_salario(emp, novo_salario):
    with conector:
        conector.execute("UPDATE empresas SET salario=:salario WHERE nome=:nome AND admissao=:admissao",
                            {'nome': emp.nome, 'salario': novo_salario, 'admissao': emp.admissao})
    return

def remover_emp(emp):
    with conector:
        conector.execute("DELETE from empresas WHERE nome=:nome AND admissao=:admissao",
                            {'nome': emp.nome, 'admissao': emp.admissao})
    return
    
def banco_completo():
        conector = sqlite3.connect('empresa.db')
        cursor  = conector.cursor()
        cursor.execute("SELECT * FROM empresa")
        todos = cursor.fetchall()
        conector.close()
        return todos
####################################################################

cursor  = conector.cursor()

if(os.path.exists('empresa.db') == False):
    cursor.execute("""CREATE TABLE empregado (
		nome       TEXT,
		salario    REAL,
		admissao   TEXT,
		demissao   TEXT,
                cpf        TEXT,
                nascimento TEXT,
                empresa    INTEGER
		)""")
    cursor.execute("""CREATE TABLE empresa (
                numero     INTEGER PRIMARY KEY AUTOINCREMENT,
                nome       TEXT,
                cnpj       TEXT,
                telefone   TEXT,
                cep        TEXT,
                endereco   TEXT,
                insc_estadual TEXT
                )""")

# Jeito errado usando .format, suscetível a SQL Injection
# cursor.execute("INSERT INTO empresa VALUES ('{}', '{}', {}, '{}', '{}')".format(None, 'Joao Silva', 1030.0, '23/10/2019'))

# 2 Alternativas:
## Usando Tuplas:
# cursor.execute("INSERT INTO empregado VALUES (?, ?, ?, ?, ?)", (None, 'Joao Silva', 1030.0, '23/10/2019', ''))
## Usando Dicionários:
# cursor.execute("INSERT INTO empregado VALUES (:numero, :nome, :salario, :admissao, :demissao)", {'numero': None, 'nome': 'Joao Silva', 'salario': 1030.0, 'admissao': '23/10/2019', 'demissao': ''})

emp_1 = Empregado('Jose Silva', 1090.0, '10/05/2018', '', '13551489', '23/02/1998', 1)
emp_1 = Empregado('Maria Silva', 1200.0, '13/07/2019', '', '29974224', '15/05/1987', 2)
Marcos = Empregado('Marcos', 1045.0, '10/08/1999', '27/10/2020', '13898415', '03/11/2000', 3)
Marcos2 = Empregado('Marcos Segundo', 1045.0, '10/08/1999', '31/10/2020', '7876345', '10/10/1986', 4)

cursor.execute("SELECT * FROM empregado WHERE salario=?", (1030.0,))
cursor.execute("SELECT * FROM empregado WHERE nome=:nome", {'nome': 'Joao Silva'})

# cursor.fetchone(),   para pegar apenas o primeiro; caso não retorna NULL
# cursor.fetchmany(5), retorna a quantidade dada como parâmetro
# cursor.fetchall()    retorna todos

conector.commit()

conector.close()
