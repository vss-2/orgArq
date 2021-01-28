from tkinter import *
from tkinter.font import Font
from tkinter import messagebox

faixas_salarios = [1100.00, 2203.48, 3305.22, 6433.57]
faixas_aliquotas = [0.075, 0.09, 0.12, 0.14]

def percentual(salario, inss):
    percentil = inss/salario
    return percential

def main():
    base = Tk()
    base.wm_title('Cálculo de INSS')
    base_fonte = Font(family="Helvetica", size=18)
    descricao_lb = Label(base, text='Insira o salário: ', font=base_fonte)
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

        if(sal < faixas_salarios[0]):
            calculo = faixas_salarios[0]*faixas_aliquotas[0]
            messagebox.showinfo("INSS para R${:.2f}".format(sal), 'R$ {:.2f} \nAproximadamente {:.2f}%'.format(calculo, (calculo*100/faixas_salarios[0])))
        elif(sal > faixas_salarios[0] and sal < faixas_salarios[1]):
            calculo = (faixas_salarios[0]*faixas_aliquotas[0]) + ((sal-faixas_salarios[0])*faixas_aliquotas[1])
            messagebox.showinfo("INSS para R${:.2f}".format(sal), 'R$ {:.2f} \nAproximadamente {:.2f}%'.format(calculo, (calculo*100/faixas_salarios[1])))
        elif(sal > faixas_salarios[1] and sal < faixas_salarios[2]):
            calculo = (faixas_salarios[0]*faixas_aliquotas[0]) + ((faixas_salarios[1]-faixas_salarios[0])*faixas_aliquotas[1]) + ((faixas_salarios[2]-faixas_salarios[1])*faixas_aliquotas[2])
            messagebox.showinfo("INSS para R${:.2f}".format(sal), 'R$ {:.2f} \nAproximadamente {:.2f}%'.format(calculo, (calculo*100/faixas_salarios[2])))
        elif(sal > faixas_salarios[2] and sal < faixas_salarios[3]):
            calculo = (faixas_salarios[0]*faixas_aliquotas[0]) + ((faixas_salarios[1]-faixas_salarios[0])*faixas_aliquotas[1]) + ((faixas_salarios[2]-faixas_salarios[0])*faixas_aliquotas[2]) + ((sal-faixas_salarios[2])*faixas_aliquotas[3])
            messagebox.showinfo("INSS para R${:.2f}".format(sal), 'R$ {:.2f} \nAproximadamente {:.2f}%'.format(calculo, (calculo*100/faixas_salarios[3])))
        else:
	        messagebox.showinfo('Valor alto: R${:.2f}'.format(sal), 'Salário superior a R${:.2f}, provavelmente é só multiplicar por 14%! \nR${:.2f}'.format(faixas_salarios[3],sal*faixas_aliquotas[3]))

    sal_input = StringVar()
    sal_entry = Entry(base, textvariable = sal_input, font=base_fonte)
    sal_entry.grid(row=0, column=1)
    sal_entry.bind('<Return>', calcular)

    botao_calcular = Button(base,
        text='Calcular INSS',
        command=calcular,
	    font=base_fonte
    )
    botao_calcular.grid(row=1, column=1)

    botao_sair = Button(base,
        text='Sair',
	    font=base_fonte,
        command=quit
    )

    botao_sair.grid(row=1, column=0)
    base.bind('<Escape>', quit)
    base.mainloop()

main()
