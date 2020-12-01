import sqlite3
from os import path, remove

def iniciar_banco():
        if(path.exists('empresa.db') == True):
                remover_banco()
                return iniciar_banco()
        else:
                cnc = sqlite3.connect('empresa.db')
                csr = cnc.cursor()
                csr.execute("""CREATE TABLE empregado (
        		nome       TEXT,
        		salario    REAL,
        		admissao   TEXT,
        		demissao   TEXT,
                        cpf        TEXT,
                        nascimento TEXT,
                        empresa    INTEGER
        		)""")
                csr.execute("""CREATE TABLE empresa (
                        numero     INTEGER PRIMARY KEY,
                        nome       TEXT,
                        cnpj       TEXT,
                        telefone   TEXT,
                        cep        TEXT,
                        endereco   TEXT,
                        insc_estadual TEXT
                        )""")
                return cnc, csr

def remover_banco():
        try:
                try:
                        cnc.close()
                except NameError:
                        remove('empresa.db')
        except OSError:
                return
        return

def inserir_banco_empresa():
        csr.execute("INSERT INTO empresa(nome, cnpj, telefone, cep, endereco, insc_estadual) VALUES (?, ?, ?, ?, ?, ?) ",
        ('Roth-Bar Libertário', '3031902457', '(81) 9090-3042', '53039-600', 'Brasil', '9041239325-PE'))
        return

def inserir_banco_empregado():
        csr.execute("INSERT INTO empregado VALUES (?, ?, ?, ?, ?, ?, ?)", 
        ('Marcos', 1045.0, '10/08/1999', '27/10/2020', '13898415', '03/11/2000', 0))

        csr.execute("INSERT INTO empregado VALUES (?, ?, ?, ?, ?, ?, ?)", 
        ('Marcos Segundo', 1045.0, '10/08/1999', '31/10/2020', '7876345', '10/10/1986', 1))
        
        cnc.commit()

        return

def mostrar_empregado():
        csr.execute("SELECT * FROM empregado")
        print(csr.fetchall())
        return

def mostrar_empresa():
        csr.execute("SELECT * FROM empresa")
        print(csr.fetchall())
        return

if __name__ == "__main__":
        cnc, csr = iniciar_banco()
        csr.execute("SELECT * from empregado")
        inserir_banco_empregado()
        inserir_banco_empresa()
        mostrar_empregado()
        mostrar_empresa()