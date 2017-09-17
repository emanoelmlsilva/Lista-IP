def calculaEstacionamento(veic,horas,min):
		if horas > 1 and horas <= 5 and min == 0:
			taxa = 3
		else:
			taxa = ((horas%5) * 2) + ((horas//5) * 3) + 2
		if veic ==  'moto':
			taxa = taxa / 2
		return taxa

v = str.lower(input('Informe o tipo do veiculo: '))
h = int(input('Digite o tempo de horas: '))
m = int(input('Digite o tempo de minutos: '))

t = calculaEstacionamento(v,h,m)

print(t)
