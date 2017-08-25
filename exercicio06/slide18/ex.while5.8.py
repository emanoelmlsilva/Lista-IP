""" Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro
pelo segundo. Utilize apenas os operados de soma e subtração para calcular o resultado.
lembre-se de que podemos enteder a multiplicação de dois números como somas sucessivas de um deles.
Assim: 4 x 5 = 5 + 5 + 5 + 5"""

num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
cont = 1
res = 0
while (cont <= num1):
    res += num2
    cont+=1
print('multiplicação entre %d x %d = %d '%(num1,num2,res))