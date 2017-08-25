""" Escreva um programa que leia dois números. Imprima a divisão inteira do primeiro pelo
segundo, assim como o resto da divisão. Utilize apenas os operadores de soma e subtração para
calcular o resultado. Lembre-se de que podemos enteder o quociente da divisão de dois números
como a quantidade de vezes que podemos retirar o divisor do dividendo. Logo, 20 + 4  = 5, uma vez
que podemos subtrair 4 cinco vezes de 20."""

num1 = int(input('Informe o primeiro numero: '))
num2 = int(input('Informe o segundo numero: '))
r = num1
q = 0
cont = num2
while(cont <= num1):
    q = q + 1
    cont += num2
    r -= num2

print(q)
print(r)

"""r = num1
q = 0
while(r >= num2):
    q += 1
    r -= num2
print(q)
print(r)"""