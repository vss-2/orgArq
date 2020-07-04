class Usuario:
	"""Usuário padrão que insere seus palpites"""

	def __init__(self, email, nome, senha):
		self.email = email
		self.nick  = nome
		self.senha = senha
		self.ponto = 0

	def __repr__(self):
		return "Olá usuário '{}', mais conhecido por '{}', você tem '{}' ponto(s)!".format(self.email, self.nome, self.ponto)
