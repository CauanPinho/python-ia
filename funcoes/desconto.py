def calcular_desconto(valor, desconto):
    valor_desconto = valor * (desconto / 100)
    valor_final = valor - valor_desconto
    return valor_final


print(calcular_desconto(100,10))