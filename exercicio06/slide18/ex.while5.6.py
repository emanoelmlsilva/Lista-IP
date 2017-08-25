#   Escreva um programa para exibir os resultados no mesmo formato de uma tabuada:

tab = int(input('Informe qua a tabuada desejada: '))
cont = 0
while(cont <= 10):
    res = cont * tab
    print('%d X %d = %d'%(cont,tab,res))
    cont += 1