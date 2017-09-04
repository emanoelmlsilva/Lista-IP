num1 = float(input('Informe o primeiro numero: '))
num2 = float(input('Informe o segundo numero: '))
escolha = str.lower(input('Qual a operação que deseja calcaular: '))
if(escolha == 'soma'):
    resu = num1 + num2
elif(escolha == 'subtraçao'):
    resu = num1 - num2
elif(escolha == 'multiplicaçao'):
    resu = num1 * num2
elif(escolha == 'divisao'):
    resu = num1/num2
print('A {} entre {} e {} é iqual a {}'.format(escolha,num1,num2,resu))
