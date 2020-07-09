import os
from tkinter import *
from tkinter.font import Font
from main import banco_completo

base = Tk()
base.configure(background='white')
base.wm_title('SiGere')
neutra_Font = Font(family="Helvetica", size=12)

# Labels
linhas = 3
label0 = Label(base, text = '')
#label0.grid(row = linhas - 1, column = 0)

label1 = Label(base, text = 'Nome do Funcionário', background='white', font=neutra_Font)
label1.grid(row = linhas + 2, column = 0)

label2 = Label(base, text = 'Salário', background='white', font=neutra_Font)
label2.grid(row = linhas + 1, column = 0)

label3 = Label(base, text = 'Dia e Mês da Demissão', background='white', font=neutra_Font)
label3.grid(row = linhas, column = 0)

# Lacunas

lac1 = StringVar()
lac_NDF = Entry(base, textvariable = lac1, font=neutra_Font)
lac_NDF.grid(row = linhas, column = 1)

lac2 = StringVar()
lac_S = Entry(base, textvariable = lac2, font=neutra_Font)
lac_S.grid(row = linhas + 1, column = 1)

lac3 = StringVar()
lac_DM = Entry(base, textvariable = lac3, font=neutra_Font)
lac_DM.grid(row = linhas + 2, column = 1)

nome = lac1
salario = lac2
data = lac3

# Lista de itens

lis1 = Listbox(base, height = 10, width = 30)
lis1.grid(row = 10, column = 0, rowspan = 8, columnspan = 6)

# Barra de rolagem

barra = Scrollbar(base)
barra.grid(row = 7, column = 5, rowspan = 8)

lis1.configure(yscrollcommand = barra.set)
barra.configure(command=lis1.yview)

# Carregar do Banco de Dados
funcs = banco_completo()
for i in funcs:
    lis1.insert(END, i[1])

# Botões

botao_Add = Button(base, 
    text='Adicionar Funcionário', 
    width = 15, background='white', 
    font=neutra_Font,
    foreground='black',
    bd =  10, 
    highlightthickness=4, 
    highlightcolor="#37d3ff", 
    highlightbackground="#37d3ff", 
    borderwidth=4,
)
botao_Add.grid(row = 0, column = 0)

botao_Sair = Button(base, 
    text='Sair', 
    width = 5, background='white', 
    font=neutra_Font,
    foreground='black',
    bd =  10, 
    highlightthickness=4, 
    highlightcolor="#37d3ff", 
    highlightbackground="#37d3ff", 
    borderwidth=4,
    command=quit
)
botao_Sair.grid(row = 0, column = 1)

base.mainloop()