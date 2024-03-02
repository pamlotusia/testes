# calcula o volume de uma caixa retangular
def calcula_volume(comprimento, largura, altura):

    return comprimento * largura * altura


def converte_para_celsius(fahrenheit):
    celsius = (5.0/9.0) * (fahrenheit - 32)
    return celsius


def converte_para_fahrenheit(celsius):
    fahrenheit = 1.8 * celsius + 32
    return fahrenheit
