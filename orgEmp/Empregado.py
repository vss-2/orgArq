from datetime import datetime as dt

str_dt = '%d/%m/%Y'

class Empregado:
        """ Características básicas de um empregado """

        def __init__(self, nome, salario, admissao, demissao, cpf, nascimento, empresa):
                self.nome     = nome
                self.salario  = salario
                self.cpf      = cpf
                self.empresa  = empresa
                
                dia_mes_ano   = nascimento.split('/')
                dia_mes_ano   = [int(x) for x in dia_mes_ano]

                self.nascimento = dt(
                                        day=dia_mes_ano[0], month=dia_mes_ano[1], year=dia_mes_ano[2]
                                )

                dia_mes_ano   = admissao.split('/')
                dia_mes_ano   = [int(x) for x in dia_mes_ano]

                self.admissao = dt(
                                        day=dia_mes_ano[0], month=dia_mes_ano[1], year=dia_mes_ano[2]
                                )

                if(demissao != ''):
                        dia_mes_ano   = demissao.split('/')
                        dia_mes_ano   = [int(x) for x in dia_mes_ano]

                        self.demissao = dt(
                                                day=dia_mes_ano[0], month=dia_mes_ano[1], year=dia_mes_ano[2]
                                        )
                return
        
        def __repr__(self):
                try:
                        return print("Dados do empregado\nNome: {},\nSalário: R${},\nAdmissão: {},\nDemissão: {},\nCPF: {},\nData de nascimento: {}".format(
                                        self.nome, 
                                        self.salario, 
                                        self.admissao.strftime(str_dt), 
                                        self.demissao.strftime(str_dt), 
                                        self.cpf, 
                                        self.nascimento.strftime(str_dt))
                                )
                except AttributeError:
                        return print("Dados do empregado\nNome: {},\nSalário: R${},\nAdmissão: {}".format(self.nome, self.salario, self.admissao.strftime(str_dt), self.cpf, self.nascimento.strftime(str_dt)))