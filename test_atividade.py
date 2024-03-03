from atividade import *


# Exercício 01
def test_salario_liquido():
    assert salario_liquido(6.25, 160, 1.3) == (987.0)


def test_salario_liquido2():
    assert salario_liquido(20.5, 240, 1.7) == (4836.36)


def test_salario_liquido3():
    assert salario_liquido(13.9, 200, 6.48) == (2599.86)


# Exercício 02
def test_desconto():
    assert desconto(100) == (91.00, 9.00)


def test_desconto2():
    assert desconto(1500) == (1365.00, 135.00)


def test_desconto3():
    assert desconto(60000) == (54600.00, 5400.00)


# Exercício 03
def test_promocao():
    assert promocao(500.00, 50.00) == (450.00)


def test_promocao2():
    assert promocao(10500.00, 500.00) == (10000.00)


def test_promocao3():
    assert promocao(90.00, 0.80) == (89.20)


# Exercício 04
def test_gorjeta():
    assert gorjeta(75.00) == (82.5, 7.5)


def test_gorjeta2():
    assert gorjeta(125) == (137.5, 12.5)


def test_gorjeta3():
    assert gorjeta(350.87) == (385.96, 35.09)
