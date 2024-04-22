# import pytest foi usado a partir do tratamento de excecao, assim como o import da excecao
import pytest
from bhaskara import calcular_raizes, ExcecaoNaoEhEquacaoSegundoGrau


def test_bhaskara_uma_raiz():
    assert calcular_raizes(1, 0, 0) == (1, 0)


def test_bhaskara_duas_raizes():
    assert calcular_raizes(1, -5, 6) == (2, 3, 2)


def test_bhaskara_zero_raizes():
    assert calcular_raizes(10, 10, 10) == 0


def test_bhaskara_uma_raiz_negativa():
    assert calcular_raizes(10, 20, 10) == (1, -1)


def test_bhaskara_nao_eh_equacao_segundo_grau():
    # a linha seguinte impede que o erro ZeroDvisionError tome a frente e seja lançado, visto que esse não é o nosso alvo.
    # with pytest.raises(ZeroDivisionError):
    #     calcular_raizes(0, 0, 0)
    # outra maneira de ser feito:
    with pytest.raises(ExcecaoNaoEhEquacaoSegundoGrau):
        calcular_raizes(0, 0, 0)

