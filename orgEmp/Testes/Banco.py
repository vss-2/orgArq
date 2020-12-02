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

def remover_empregado(campo, fk_empregado):
        if(type(fk_empregado) == str):
                fk_empregado = '\'{}\''.format(fk_empregado)

        rm_marcos = csr.execute("DELETE FROM empregado WHERE cpf={}".format(fk_empregado))
        return

def remover_empresa(campo, fk_empresa):
        if(type(fk_empresa) == str):
                fk_empresa = '\'{}\''.format(fk_empresa)

        rm_bar = csr.execute("DELETE FROM empresa WHERE cnpj={}".format(fk_empresa))
        return

def atualizar_empregado(campo, novo_valor, fk_empregado, id_empregado):
        if(type(novo_valor) == str):
                novo_valor = '\'{}\''.format(novo_valor)
        if(type(id_empregado) == str):
                id_empregado = '\'{}\''.format(id_empregado)

        csr.execute("UPDATE empregado SET {} = {} WHERE {} = {}".format(campo, novo_valor, fk_empregado, id_empregado))
        return

def atualizar_empresa(campo, novo_valor, fk_empresa, id_empresa):
        if(type(novo_valor) == str):
                novo_valor = '\'{}\''.format(novo_valor)
        if(type(id_empresa) == str):
                id_empresa = '\'{}\''.format(id_empresa)

        csr.execute("UPDATE empresa SET {} = {} WHERE {} = {}".format(campo, novo_valor, fk_empresa, id_empresa))
        return

if __name__ == "__main__":
        cnc, csr = iniciar_banco()

        inserir_banco_empregado()
        inserir_banco_empresa()
        mostrar_empregado()
        mostrar_empresa()

        # Se for alguma String em novo_valor ou id_empregado,
        # tem que dar cast de aspas simples, ex: s = '\'{}\''.format(novo_valor)
        atualizar_empregado('nome', 'Marcos Primeiro', 'cpf', '13898415')
        mostrar_empregado()
        atualizar_empresa('nome', 'Roth-Bar Libertário LTDA', 'cnpj', '3031902457')
        mostrar_empresa()

        remover_empregado('cpf', '13898415')
        remover_empresa('cnpj', '3031902457')

        mostrar_empregado()
        mostrar_empresa()
