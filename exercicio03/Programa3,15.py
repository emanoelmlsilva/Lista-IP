cigarro_dia = int(input('Informe a quantidade de cigarros fumados por dias: '))
anos = float(input('Informe a quantidade de anos que ja fumou: '))
minutos = 10*cigarro_dia
res = (minutos/1440) + (anos * 365)
print('O valor de dias perdidos é de %5.2f'%res)

