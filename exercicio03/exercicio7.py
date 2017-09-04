idade = int(input('Informe a idade: '))
mes = int(input('Informe o mes: '))
dias = int(input('Infome os dias: '))
idade = idade * 365
mes = mes * 30
tot = idade + mes + dias
print('Anos expressado em dias %d'%tot)
