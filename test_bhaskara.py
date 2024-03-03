
from bhaskara import calcular_raizes


def test_bhaskara_uma_raiz():
    assert calcular_raizes(1, 0, 0) == (1, 0)


def test_bhaskara_duas_raizes():
    assert calcular_raizes(1, -5, 6) == (2, 3, 2)


def test_bhaskara_zero_raizes():
    assert calcular_raizes(10, 10, 10) == 0


def test_bhaskara_uma_raiz_negativa():
    assert calcular_raizes(10, 20, 10) == (1, -1)
