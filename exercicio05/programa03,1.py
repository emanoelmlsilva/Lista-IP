quant = int(input('Infome a quantidade de pessoas: '))
tot = quant
nvan = 20
nbus = 42
vlt = 350
vld = 200
vlo = quant//nbus
quant = quant%nbus
vlv = quant//nvan
quant = quant%nvan
if(quant > 0):
    vlv += 1
if(vlv > 1 or vlo > 1):
    vld *= vlv
    vlt *= vlo  
if((vlv > 0) and (vlo > 0)):
    pagar = (vlt+vld)/tot
    print('{} Onibus e {} van'.format(vlo,vlv),'\nR$ {:.2f} por pessoa'.format(pagar))
elif(vlv > 0):
    preçoV = vld/tot
    print('{} van '.format(vlv),'\nR$ {:.2f} por pessoa'.format(preçoV))
elif(vlo > 0):
    preçoO = vlt/tot
    print('{} Onibus '.format(vlo),'\nR$ {:.2f} por pessoa'.format(preçoO))

