
val = float(input('Insira o salario no seguinte formato \'1045.00\': '))

if(val < 1045.01):
	print('R$',val*0.075)
elif(val > 1045.00 and val < 2089.61):
	print('R$',1045.00*0.075 + (val-1045.00)*0.09)
elif(val > 2089.60 and val < 3134.41):
	print('R$',1045.00*0.075 + (2089.60-1045.00)*0.09 + (val-2089.60)*0.12)
elif(val > 3134.40 and val < 6101.06):
	print('R$',1045.00*0.075 + (2089.60-1045.00)*0.09 + (3134.40-1045.00)*0.12 + (val-3134.40)*0.14)
else:
	print('Valor superior a R$ 6101.06, provavelmente é só multiplicar por 14%')
