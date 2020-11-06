from tkinter import *
from tkinter import messagebox

def percentual(salario, inss):
    percentil = inss/salario
    return percential

def main():
    base = Tk()
    base.wm_title('Cálculo de INSS')

    descricao_lb = Label(base, text='Insira o salário: ')
    descricao_lb.grid(row=0, column=0)

    def calcular(event=None):
        sal = sal_entry.get()

        try:
            sal = float(sal)
        except ValueError:
            if(sal[len(sal)-3:len(sal)-2] == ','):
                sal = float(sal[:len(sal)-3]+'.'+sal[len(sal)-2:])
            else:
                messagebox.showerror("Erro de digitação", "Salário inválido!")
                return

        if(sal < 1045.01):
            calculo = sal*0.075
            messagebox.showinfo("INSS para R${:.2f}".format(sal), 'R$ {:.2f} \nAproximadamente {:.2f}%'.format(calculo, (calculo*100/sal)))
        elif(sal > 1045.00 and sal < 2089.61):
            calculo = (1045.00*0.075) + ((sal-1045.00)*0.09)
            messagebox.showinfo("INSS para R${:.2f}".format(sal), 'R$ {:.2f} \nAproximadamente {:.2f}%'.format(calculo, (calculo*100/sal)))
        elif(sal > 2089.60 and sal < 3134.41):
            calculo = (1045.00*0.075) + ((2089.60-1045.00)*0.09) + ((sal-2089.60)*0.12)
            messagebox.showinfo("INSS para R${:.2f}".format(sal), 'R$ {:.2f} \nAproximadamente {:.2f}%'.format(calculo, (calculo*100/sal)))
        elif(sal > 3134.40 and sal < 6101.06):
            calculo = (1045.00*0.075) + ((2089.60-1045.00)*0.09) + ((3134.40-1045.00)*0.12) + ((sal-3134.40)*0.14)
            messagebox.showinfo("INSS para R${:.2f}".format(sal), 'R$ {:.2f} \nAproximadamente {:.2f}%'.format(calculo, (calculo*100/sal)))
        else:
	        messagebox.showinfo('Valor alto: R${:.2f}'.format(sal), 'Salário superior a R$ 6101.06, provavelmente é só multiplicar por 14%! \nR${:.2f}'.format(sal*0.14))

    sal_input = StringVar()
    sal_entry = Entry(base, textvariable = sal_input)
    sal_entry.grid(row=0, column=1)
    sal_entry.bind('<Return>', calcular)

    botao_calcular = Button(base,
        text='Calcular INSS',
        command=calcular
    )
    botao_calcular.grid(row=1, column=1)

    botao_sair = Button(base,
        text='Sair',
        command=quit
    )

    botao_sair.grid(row=1, column=0)
    base.bind('<Escape>', quit)
    base.mainloop()

main()
