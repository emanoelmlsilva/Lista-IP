temp_second = 47500
horas = temp_second/3600
minutos = (temp_second%3600)/60
segundos = (temp_second%3600)%60
print('A duraçao é %d horas, %d minutos, %d segundos'%(horas,minutos,segundos))
