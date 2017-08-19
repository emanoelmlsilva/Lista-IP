cont = 0 # cont tem que ser um numero maior que 0
qtdePositivos = 0
numero = int (input()) #variavel numero fora do laçao de repetiçao 
while (cont > 0): #nao á condiçao de parada
        if (numero >= 0):
                qtdePositivos = numero + 1
        cont = cont + 1 #conte esta recebendo mais um ao inves de subtrair 
print(cont)

