import bibliotecacorreios

tipo = str.lower(input('informe o tipo do item (documento ou pacote): '))

peso = float(input('Digite o peso em quilo: '))

embalagem = str.lower(input('Informe  o tipo da embalagem (grande, pequena, media): '))

entrega = str.lower(input('Informe o tipo da entrega(normal,sedex,sedex10): '))

bibliotecacorreios.validaEntrega(entrega)
e = bibliotecacorreios.calcularCustoEntrega(entrega)

bibliotecacorreios.validaPeso(peso)
pesoConv = bibliotecacorreios.convertePeso(peso)

bibliotecacorreios.tipoItem(tipo)
i = bibliotecacorreios.calculaCustoItem(tipo, pesoConv)


bibliotecacorreios.validaEmbalagem(embalagem)
b = bibliotecacorreios.calculaCustoEmbalagem(embalagem)

print('Custo total {} R$'.format(e+i+b))
