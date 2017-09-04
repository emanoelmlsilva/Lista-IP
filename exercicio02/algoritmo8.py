idade_dias = 7149
anos = idade_dias/365
mes = (idade_dias%365)/30
dias = (idade_dias%365)%30

print('%d anos, %d meses, %d dias '%(anos,mes,dias))
