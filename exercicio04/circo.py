idade = float(input('Informe a idade da pessoa: '))
if(idade <= 5):
    ingresso = 10
elif(idade >= 60):
    ingresso = 15
else:
    ingresso= 25
print('O valor do ingresso sera de {}'.format(ingresso))
