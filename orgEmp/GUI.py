from tkinter import *
from tkinter.font import Font
# from main import banco_completo
import sqlite3

def banco_completo():
        conector = sqlite3.connect('empresa.db')
        cursor  = conector.cursor()
        cursor.execute("SELECT * FROM empresa")
        todos = cursor.fetchall()
        conector.close()
        return todos

if __name__ == "__main__":
	# Setup inicial Tkinter
	base = Tk()
	# base.configure(background='grey')
	base.wm_title('SiGere')
	sigere_Fonte = Font(family="Helvetica", size=12)

	linhas = 3

	# Labels (descrições)
	def carregar_labels():
		data_mes_demissao_lb = Label(base, text = 'Dia e Mês da Demissão', font=sigere_Fonte)
		data_mes_demissao_lb.grid(row = linhas, column = 0)

		nome_lb = Label(base, text = 'Nome do Funcionário', font=sigere_Fonte)
		nome_lb.grid(row = linhas + 2, column = 0)

		salario_lb = Label(base, text = 'Salário', font=sigere_Fonte)
		salario_lb.grid(row = linhas + 1, column = 0)

	
	# Lacunas (campos de texto)
	def carregar_inputs():
		nome_input = StringVar()
		nome_entry = Entry(base, textvariable = nome_input, font=sigere_Fonte)
		nome_entry.grid(row = linhas, column = 1)

		salario_input = StringVar()
		salario_entry = Entry(base, textvariable = salario_input, font=sigere_Fonte)
		salario_entry.grid(row = linhas + 1, column = 1)

		data_input = StringVar()
		data_entry = Entry(base, textvariable = data_input, font=sigere_Fonte)
		data_entry.grid(row = linhas + 2, column = 1)

	# Lista de itens
	def carregar_listboxes():
		funcs_lbox = Listbox(base, height = 20, width = 25)
		funcs_lbox.grid(row = 14, column = 0, rowspan = 2, columnspan = 3)
		funcs = banco_completo()
		for i in funcs:
			funcs_lbox.insert(END, i[1])

	# Barra de rolagem

	# barra = Scrollbar(base)
	# barra.grid(row = 7, column = 5, rowspan = 8)
	# funcs_lbox.configure(yscrollcommand = barra.set)
	# barra.configure(command=funcs_lbox.yview)

	# Carregar do Banco de Dados

	# Botões
	def carregar_botoes():
		botao_Adcfunc = Button(base, 
			text='Adicionar Funcionário', 
			width = 15, 
			background='#62D178', 
			font=sigere_Fonte,
			foreground='black',
			bd = 0, 
			highlightthickness=1, 
			borderwidth=1,
		)
		botao_Adcfunc.grid(row = 6, column = 1)

		botao_Sair = Button(base, 
			text='Sair', 
			width = 5, 
			background='#5993D8', 
			font=sigere_Fonte,
			foreground='black',
			bd =  10, 
			highlightthickness=1, 
			borderwidth=1,
			command=quit
		)
		botao_Sair.grid(row = 50, column = 0)

		botao_Editar = Button(base, 
			text='Editar', 
			width = 5, 
			background='#F9C444', 
			font=sigere_Fonte,
			foreground='black',
			bd =  10, 
			highlightthickness=1, 
			borderwidth=1,
			command=quit
		)
		botao_Editar.grid(row = 14, column = 2)

		botao_Remover = Button(base, 
			text='Remover', 
			width = 5, 
			background='#EC6434', 
			font=sigere_Fonte,
			foreground='black',
			bd =  10, 
			highlightthickness=1, 
			borderwidth=1,
			command=quit
		)
		botao_Remover.grid(row = 15, column = 2)

	def carregar_GUI_completa():
		carregar_inputs()
		carregar_labels()
		carregar_listboxes()
		carregar_botoes()

	carregar_GUI_completa()

	def sair(event):
		base.quit()

	# Atalhos de teclado	
	base.bind('<Control-q>', sair)

	base.mainloop()