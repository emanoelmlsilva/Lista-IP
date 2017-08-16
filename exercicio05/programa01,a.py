rendaAnual = float (input())
if (rendaAnual <= 12000):
    imposto = 0
elif (rendaAnual > 60000): #if nao tem laço com o primeiro if e fica exibindo todo vez com o primerio if sendo ou nao execultado
    imposto = rendaAnual*0.07
else:
    imposto = rendaAnual*0.03
print(imposto)
