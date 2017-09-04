dias = int(input('Entre com o valor em dias: ')) # 1 dia tem 86400 segundos
horas = int(input('Entre com o valor em horas: ')) # 1 hora tem 3600 segundos
minutos = float(input('Entre com o valor em minutos; ')) # 1 minuto tem 60 segundos
segundos= float(input('Entre com o valor em segundos: '))
tot_segund = (dias*864000) + (horas*3600) + (minutos*60) + segundos
print('O total em segundos corresponde a %5.2f'%tot_segund)
