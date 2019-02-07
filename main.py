import os 
import datetime
import Tkinter
## OS: Usado para acessar o diretório; 
## DateTime: Usado para saber "momento" (dia, mês, ano)
## Tkinter: Usado para interface gráfica

dia = datetime.datetime.now()
mes = datetime.datetime.now()
ano = datetime.datetime.now()
  
class Aplicacao:
  def __init__(self, master=None):
    self.widget1 = Frame(master)
    self.widget1.pack()
    self.msg = Label(self.widget1, text="Em qual diretório quer gerar a pasta?");
    self.msg.pack()                             ## Terminou de usar? Empacota
    self.criar = Button(self.widget1)
    self.criar["text"] = "Gerar pasta"
    self.criar["width"] = 10
    self.criar.pack()
    self.sair = Button(self.widget1)            ## Botão
    self.sair["text"] = "Sair"                  ## Texto botão
    self.sair["width"] = 5                      ## Comprimento botão
    self.sair["command"] = self.widget1.quit    ## Encerra
    self.sair.pack()
    
    def criarPasta(self, event, ano, mes):
      ## Se existe pasta com o ano, avance
        ## Se existe pasta com o mês ano, avance
          ## Crie pasta
        ## Senão, crie pasta com o mês
      ## Senão, crie pasta com o ano

    
base = Tk()
Aplicacao(base)
base.mainloop()
