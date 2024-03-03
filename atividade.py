# Exercício 01
def salario_liquido(valor_hora, numero_aulas, percentual_INSS):
    salario_bruto = valor_hora * numero_aulas
    desconto_inss = (percentual_INSS / 100) * salario_bruto
    return round(salario_bruto - desconto_inss, 2)


print(salario_liquido(6.25, 160, 1.3))
print(salario_liquido(20.5, 240, 1.7))
print(salario_liquido(13.9, 200, 6.48))


# Exercício 02
def desconto(valor_produto):
    desconto = valor_produto * 0.09
    novo_valor = valor_produto - desconto
    return novo_valor, desconto


print(desconto(100))
print(desconto(1500))


# Exercício 03
def promocao(valor_original, desconto):
    return valor_original - desconto


print(promocao(90.00, 0.80))


# Exercício 04
def gorjeta(valor_conta):
    gorjeta = round(valor_conta * 0.10, 2)
    total = round(valor_conta + gorjeta, 2)
    return total, gorjeta


print(gorjeta(75.00))
print(gorjeta(125))
print(gorjeta(350.87))
