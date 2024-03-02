
from modulos01 import *


# caso 01
def soma(a, b):
    return a + b


# Programa principal
try:
    resultado = soma(10, 20)
    assert resultado == 30
    print('Soma correta!')
except AssertionError:
    print('Soma errada!')


# caso 02
try:
    resultado = soma(3, 5)
    assert resultado == 8
    print('soma correta')
except AssertionError:
    print('soma errada!')


# caso 03
try:
    resultado = soma('olá ', 'mundo')
    assert resultado == 'olá mundo'
    print('concatenação correta!')
except AssertionError:
    print('concatenação errada')


# caso 04
try:
    resultado = soma(1.4, 3.2)
    assert resultado == 4.6
    print('soma correta')
except AssertionError:
    print('soma errada!')


# exercicio 01
try:
    resultado = calcula_volume(1, 1, 1)
    assert resultado == 1
    print('calculo correto')
except AssertionError:
    print('calculo incorreto')

try:
    resultado = calcula_volume(2, 4, 3)
    assert resultado == 24
    print('calculo correto')
except AssertionError:
    print('calculo incorreto')

try:
    resultado = calcula_volume(5, 5, 2)
    assert resultado == 50
    print('calculo correto')
except AssertionError:
    print('calculo incorreto')


# exercicio 02
try:
    resultado = converte_para_fahrenheit(0)
    assert resultado == 32.0
    print('convertido para fahrenheit corretamente')
except AssertionError:
    print('conversão feita incorretamente')

try:
    resultado = converte_para_fahrenheit(27)
    assert resultado == 80.6
    print('convertido para fahrenheit corretamente')
except AssertionError:
    print('conversão feita incorretamente')

try:
    resultado = converte_para_celsius(32)
    assert resultado == 0
    print('convertido para celsius corretamente')
except AssertionError:
    print('conversão feita incorretamente')

try:
    resultado = converte_para_celsius(41)
    assert resultado == 5.0
    print('convertido para celsius corretamente')
except AssertionError:
    print('conversão feita incorretamente')
