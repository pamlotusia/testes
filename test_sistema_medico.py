from sistema_medico import calcular_dosagem
import pytest


def test_idade_negativa():
    # sintaxe de testar. Se a exceção não estiver acontecendo, o teste irá falhar. Neste caso, se nenhuma idade negativa for passada, o teste irá falhar.
    with pytest.raises(ValueError):
        calcular_dosagem(-1, 5)


def test_idade_excessiva():
    with pytest.raises(ValueError):
        calcular_dosagem(250, 5)


def test_peso_negativo():
    with pytest.raises(ValueError):
        calcular_dosagem(1, -1)


def test_peso_excessivo():
    with pytest.raises(ValueError):
        calcular_dosagem(1, 250)


def test_paciente_20_anos():
    assert calcular_dosagem(20, 60) == 1000


def test_paciente_12_anos():
    assert calcular_dosagem(12, 60) == 1000


def test_paciente_20_anos_59_kilos():
    assert calcular_dosagem(20, 59) == 875


def test_paciente_12_anos_59_kilos():
    assert calcular_dosagem(12, 59) == 875


def test_paciente_1_ano():
    assert calcular_dosagem(1, 5) == 125


def test_paciente_1_ano_pesado():
    assert calcular_dosagem(1, 9) == 125


def test_paciente_2_ano_9_kilos():
    assert calcular_dosagem(2, 9.1) == 250


def test_paciente_2_ano_16_kilos():
    assert calcular_dosagem(2, 16) == 250


def test_paciente_3_ano_16_kilos():
    assert calcular_dosagem(3, 16.1) == 375


def test_paciente_3_ano_24_kilos():
    assert calcular_dosagem(3, 24) == 375


def test_paciente_4_ano_24_kilos():
    assert calcular_dosagem(4, 24.1) == 500


def test_paciente_5_ano_30_kilos():
    assert calcular_dosagem(5, 30) == 500


def test_paciente_6_ano_30_kilos():
    assert calcular_dosagem(6, 30.1) == 750
