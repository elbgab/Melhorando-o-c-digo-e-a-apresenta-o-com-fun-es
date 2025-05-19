# Funcao que calcula o valor com desconto
def calcular_desconto(preco, percentual):
    desconto = preco * (percentual / 100)
    return preco - desconto


# Chamando a funcao
preco_produto = 150.0
desconto = 10  # 10%
print("Preço com desconto:", calcular_desconto(preco_produto, desconto))
