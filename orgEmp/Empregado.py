class Empregado:
        """ Caracteristicas básicas de um empregado """

        def __init__(self, nome, salario, admissao, demissao):
                self.nome     = nome
                self.salario  = salario
                self.admissao = admissao
                self.demissao = demissao
        
        def __repr__(self):
                return "Dados do empregado ('{}', '{}', {})".format(self.nome, self. salario, self.admissao, self.demissao)