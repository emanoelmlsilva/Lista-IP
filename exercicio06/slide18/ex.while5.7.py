# Modifique o programa anterior de forma que o usuário também digite o inicio e o fim da tabuada, em vez de começar com 1 e 10.

tab = int(input('Informe qua a tabuada: '))
inic = int(input('Informe o começo da tabuada: '))
fim = int(input('Informe o fim da tabuada: '))
cont = inic

while(cont <= fim):
    res = tab*cont
    print('%d X %d = %d'%(tab,cont,res))
    cont+=1