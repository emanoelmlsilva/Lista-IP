listaMes = list(range(12))
listaReceita = []
listaDespesa =[]
nome = ["janeiro","fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
totReceita = 0
totDespesa = 0
nomeMes = []
for i in listaMes:
	print("mes {}".format(i+1))
	receita = float(input("Digite o valor da receita :"))
	listaReceita.append(receita)
	despesa = float(input("Digite o valor da despesa: "))
	listaDespesa.append(despesa)
	totReceita += receita
	totDespesa += despesa
saldo = totReceita - totDespesa
if saldo > 0:
	info = "positivo"
else:
	info = "negativo"
print("="*30)
print("Total da receita no ano {}".format(totReceita))
print("="*30)
print("Total da despesa no ano {}".format(totDespesa))
print("="*30)
print("Saldo financeiro {}".format(info))
print("="*30)
for x in listaMes:
	if listaReceita[x] > listaDespesa[x]:
		nomeMes.append(nome[x])
print("Nome dois meses em que a receita superou a despesa {}".format(nomeMes))
