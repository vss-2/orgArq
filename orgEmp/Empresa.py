from datetime import datetime as dt

str_dt = '%d/%m/%Y'

class Empresa:
        """ Características básicas de uma empresa """

        def __init__(self, nome, cpnj, insc_estadual, telefone, cep, endereco):
                self.nome     = nome
                self.cpnj     = cpnj
                self.telefone = telefone
                self.cep      = cep
                self.endereco = endereco
                self.insc_estadual = insc_estadual
                return
        
        def __repr__(self):
                return print("Dados da empresa\nNome: {},\nCPNJ: R${},\nTelefone: {},\nEndereco: {},\nCEP: {},\nInscrição Estadual: {},".format(
                                self.nome, 
                                self.cpnj, 
                                self.telefone, 
                                self.cep, 
                                self.endereco, 
                                self.insc_estadual)
                        )
