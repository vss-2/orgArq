import os
import datetime
import platform
from tkinter import *
from tkinter import Menu
# OS: Usado para acessar o diretório;
# DateTime: Usado para saber "momento" (dia, mês, ano);
# Tkinter: Usado para interface gráfica;
# São usados nas linhas 28-31;
# Platform: Usado para saber o sistema operacional,
# o formato de endereço do Windows difere de Linux

class Aplicacao:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(
        self.widget1, text="Em qual diretório quer gerar a pasta?")
        self.msg["font"] = ("Trebuchet MS", 10)
        self.msg.pack()  # Terminou de usar? Empacota
        self.criar = Button(self.widget1)
        self.criar["text"] = "Gerar pasta"
        self.criar["width"] = 10
        self.criar["font"] = ("Trebuchet MS", 8)
        self.criar.bind("<Button-1>", self.criarPasta)
        self.criar.pack()
        self.sair = Button(self.widget1)          # Botão
        self.sair["text"] = "Sair"                # Texto botão
        self.sair["width"] = 5                    # Comprimento botão
        self.sair["command"] = self.widget1.quit  # Encerra
        self.sair["font"] = ("Trebuchet MS", 8)   # Estilo
        self.sair.pack()

    def criarPasta(self, event):
        dia = datetime.datetime.now().day # Nem usei, mas botei aqui kkkkk
        mes = str(datetime.datetime.now().month)
        ano = str(datetime.datetime.now().year)
        diretorioAtual = os.getcwd()


        # Endereços no Windows usam antebarras duplas

        if not (os.path.exists(diretorioAtual+'\\'+ano)):
            os.mkdir(diretorioAtual+'\\'+ano)
            print('Criei a pasta do ano:'+ano+'!')
            # Se existe pasta com o ano, avance

            if os.path.exists(diretorioAtual+'\\'+ano+'\\'+mes):
                # Se existe pasta com o mês ano, avance
                print('Já existe pasta de ano '+ano+' e mês '+mes+'!')
            else:
                # Crie pasta
                os.mkdir(diretorioAtual+'\\'+ano+'\\'+mes)
                print('Criei a pasta do mês:'+mes+'!')

        else:
            # Crie pasta
            if os.path.exists(diretorioAtual+'\\'+ano+'\\'+mes):
                # Se existe pasta com o mês ano, GG
                print('Já existe pasta de ano '+ano+' e mês '+mes+'!')
            else:
                # Crie pasta
                os.mkdir(diretorioAtual+'\\'+ano+'\\'+mes)
                print('Criei a pasta do mês:'+mes+'!')
        
base = Tk()
base.title("OrgArq")

menu = Menu(base)
itemMenu = Menu(menu, tearoff = 0)
# Tearoff é a linha pontilhada

itemMenu.add_command(label="Sair", command = quit)
#itemMenu.add_separator() Para separar comandos

menu.add_cascade(label="Opções", menu = itemMenu)
base.config(menu = menu)
Aplicacao(base)
base.mainloop()
