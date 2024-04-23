from rancking_nadadores import obter_categoria


def test_atleta_sem_categoria():
    assert obter_categoria(2) == 'Atleta muito jovem, não possui categoria'


def test_atleta_de_5_a_7_anos():
    assert obter_categoria(5) == 'Infantil A'


def test_atleta_de_8_a_10_anos():
    assert obter_categoria(9) == 'Infantil B'


def test_atleta_de_11_a_13_anos():
    assert obter_categoria(12) == 'Juvenil A'


def test_atleta_de_14_a_17_anos():
    assert obter_categoria(15) == 'Juvenil B'


def test_atleta_acima_de_18_anos():
    assert obter_categoria(20) == 'Sênior'
