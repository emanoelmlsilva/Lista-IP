distancia = float(input('informe a distancia que deseja percorer: '))
if(distancia <= 200):
    pagamento = distancia*0.50
else:
    pagamento = distancia*0.45    
print('Preço da viagem é de {} R$'.format(pagamento))
