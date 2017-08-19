while(True):
        num1 = int(input('Informe o primeiro valor: '))
        num2 = int(input('Informe o segundo valor: '))
        if(num1 <= 0 or num2 <= 0):
                m = ( num1 + num2) / 2
                print(m)
        else:
                soma = num1 + num2
                mult = num1 * num2
                print('{} {}'.format(soma,mult))
        perg = str.lower(input('Deseja continuar (S/n): '))
        if      perg    ==      's'     :
                True
        else:
                break

