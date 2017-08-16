setor = str.lower(input('Infome o setor do ingresso (plateia vip, arquibancada e cadeira: '))
ingresso = str.lower(input('Informe o tipo do ingresso (inteira, meia): '))
if(setor == 'plateia vip'):
    if(ingresso == 'meia'):
        tipo = 'Tipo de ingresso inválido'
    else:
        tipo = (350 * 0.05) + 350
elif(setor == 'cadeira'):
    if(ingresso == 'inteira'):
        tipo = (200 * 0.05) + 200
    elif(ingresso == 'meia'):
        tipo = (200 * 0.05) + 100
    else:
        tipo = 'Tipo de ingresso inválido'
elif(setor == 'arquibancada'):
    if(ingresso == 'inteira'):
        tipo = (100 * 0.05) + 100
    elif(ingresso == 'meia'):
        tipo = (100 * 0.05) + 50
    else:
        tipo = 'Tipo de ingresso inválido'
else:
    tipo = 'Setor inválido'
print('R$ {}'.format(tipo))
    
