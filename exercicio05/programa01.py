num = int(input('Informe um numero: '))

if(num > 0):
    entrada = 'Positivo'
elif(num < 0):
    entrada = 'Negativo'
else:
    entrada = 'Neutro'
print('{}'.format(entrada))
