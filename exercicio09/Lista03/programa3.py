orçamento = [["janeiro",2343,4563],["fevereiro",2364,6755],["Março",1233,4564],["Abril",2346,3723,],["Maio",2343,1231],["Junho",1244,2342],["Julho",5645,6554],["Agosto",1232,2332],["Setembro",2342,3453],["Outubro",1233,2331],["Novembro",2321,4323],["Dezembro",4323,5324]]
maior = 0
soma = 0
print("Mes com receita superior a 2500")
for i in orçamento:
	if i[1] > 2500:
		print(i[0],end=' ')
	if i[2] > maior:
		maior = i[2]
		nome = i[0]
	soma += i[1]
print()
media = soma/12
print("Mes com a maior despesa foi {}".format(nome))
print("Receita media anual {:.2f}".format(media))
