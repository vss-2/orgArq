from datetime import datetime as dt

class Empregado:
        """ Características básicas de um empregado """

        def __init__(self, nome, salario, admissao, demissao):
                self.nome     = nome
                self.salario  = salario

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
                        return print("Dados do empregado\nNome: {},\nSalário: R${},\nAdmissão: {},\nDemissão: {}".format(self.nome, self.salario, self.admissao.strftime('%d/%m/%Y'), self.demissao.strftime('%d/%m/%Y')))
                except AttributeError:
                        return print("Dados do empregado\nNome: {},\nSalário: R${},\nAdmissão: {}".format(self.nome, self.salario, self.admissao.strftime('%d/%m/%Y')))