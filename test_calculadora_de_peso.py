import pytest


from calculadora_de_peso import obter_peso_ideal


def test_calcular_peso_homem_1_50m():
    # pytest.approx(valor_esperado, casa_decimal) -> é usado para aproximar o resultado float à uma casa decimal
    assert obter_peso_ideal(1.5, 'M') == pytest.approx(51.05, 0.01)


def test_calcular_peso_mulher_1_50m():
    assert obter_peso_ideal(1.5, 'F') == pytest.approx(48.45, 0.01)


def test_calcular_peso_homem_1_60m():
    assert obter_peso_ideal(1.60, 'M') == pytest.approx(58.32, 0.01)


def test_calcular_peso_mulher_1_60m():
    assert obter_peso_ideal(1.60, 'F') == pytest.approx(54.66, 0.01)


def test_calcular_peso_homem_1_70m():
    assert obter_peso_ideal(1.70, 'M') == pytest.approx(65.59, 0.01)


def test_calcular_peso_mulher_1_70m():
    assert obter_peso_ideal(1.70, 'F') == pytest.approx(60.86, 0.01)


def test_calcular_peso_homem_1_80m():
    assert obter_peso_ideal(1.80, 'M') == pytest.approx(72.86, 0.01)


def test_calcular_peso_mulher_1_80m():
    assert obter_peso_ideal(1.80, 'F') == pytest.approx(67.08, 0.01)


def test_calcular_peso_homem_1_90m():
    assert obter_peso_ideal(1.90, 'M') == pytest.approx(80.13, 0.01)


def test_calcular_peso_mulher_1_90m():
    assert obter_peso_ideal(1.90, 'F') == pytest.approx(73.28, 0.01)


def test_calcular_peso_homem_2m():
    assert obter_peso_ideal(2.00, 'M') == pytest.approx(87.4, 0.01)


def test_calcular_peso_mulher_2m():
    assert obter_peso_ideal(2.00, 'F') == pytest.approx(79.5, 0.01)
