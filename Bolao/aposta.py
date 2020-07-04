class Aposta:
	"""Aposta padrão que contém palpites dos usuários"""

	def __init__(self, partida, vencer, placar):
		self.partida   = partida
		self.vencedor  = vencer
		self.placar    = placar

	def __repr__(self):
		return "Usuario '{}': Na partida: '{}' você apostou em '{}', boa sorte!".format(self.id_usr, self.partida, self.vencedor)
