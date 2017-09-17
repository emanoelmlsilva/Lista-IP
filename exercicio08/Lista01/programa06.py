import calculaMaior
maior = 0
for i in range(1,5):
	num = int(input('Digite um numero: '))
	m = calculaMaior.calculaMaior(num,maior)		
	maior = m
print(maior) 
