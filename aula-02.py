import unittest


def soma(a, b):
    return a + b


class TesteSoma(unittest.TestCase):
    def test_funcao_soma(self):
        self.assertEqual(soma(10, 5), 15)


# exercicio 01
def avaliar_notas(n1, n2, n3, media_exercicios):
    if n1 < 0 or n1 > 10:
        raise ValueError('Valor inválido para n1')
    if n2 < 0 or n2 > 10:
        raise ValueError('Valor inválido para n2')
    if n3 < 0 or n3 > 10:
        raise ValueError('Valor inválido para n3')
    if media_exercicios < 0 or media_exercicios > 10:
        raise ValueError('Valor inválido para media_exercicios')

    media_aproveitamento = (n1 + 2*n2 + 3*n3 + media_exercicios)/7
    if media_aproveitamento >= 9.0:
        return 'A'
    elif media_aproveitamento >= 7.5 and media_aproveitamento < 9:
        return 'B'
    elif media_aproveitamento >= 6.0 and media_aproveitamento < 7.5:
        return 'C'
    elif media_aproveitamento < 6.0:
        return 'D'


class TesteMedia(unittest.TestCase):
    def test_valor_invalido(self):
        self.assertRaises(ValueError, avaliar_notas, -1, 0, 0, 0)

    def test_valor_invalido2(self):
        self.assertRaises(ValueError, avaliar_notas, 0, -1, 0, 0)

    def test_valor_invalido3(self):
        self.assertRaises(ValueError, avaliar_notas, 0, 0, -1, 0)

    def test_media1(self):
        self.assertEqual(avaliar_notas(10, 10, 10, 10), 'A')

    def test_media2(self):
        self.assertEqual(avaliar_notas(9, 9, 9, 9), 'A')

    def test_media3(self):
        self.assertEqual(avaliar_notas(8.9, 8.9, 8.9, 8.9), 'B')

    def test_media4(self):
        self.assertEqual(avaliar_notas(7.5, 7.5, 7.5, 7.5), 'B')

    def test_media5(self):
        self.assertEqual(avaliar_notas(7.4, 7.4, 7.4, 7.4), 'C')

    def test_media6(self):
        self.assertEqual(avaliar_notas(6.0, 6.0, 6.0, 6.0), 'C')

    def test_media7(self):
        self.assertEqual(avaliar_notas(5.9, 5.9, 5.9, 5.9), 'D')

    def test_media8(self):
        self.assertEqual(avaliar_notas(0.0, 0.0, 0.0, 0.0), 'D')


# exercicio 02
REQUERER = 'Requerer aposentadoria'
NAO_REQUERER = 'Não requerer'


def verificar_qualificacao_empregado(idade, tempo_de_servico):
    if idade <= 0 or tempo_de_servico <= 0:
        raise ValueError('Valor inválido')
    if isinstance(idade, str) or isinstance(tempo_de_servico, str):
        raise TypeError('Valor inválido')

    if idade >= 65:
        return REQUERER
    elif tempo_de_servico >= 30:
        return REQUERER
    elif idade >= 60 and tempo_de_servico >= 25:
        return REQUERER
    return NAO_REQUERER


class TesteAposentadoria(unittest.TestCase):
    def test_valor_invalido(self):
        self.assertRaises(ValueError, verificar_qualificacao_empregado, 0, 10)

    def test_valor_invalido2(self):
        self.assertRaises(ValueError, verificar_qualificacao_empregado, 20, 0)

    def test_valor_invalido_string(self):
        self.assertRaises(
            TypeError, verificar_qualificacao_empregado, '65', 30)

    def test_valor_invalido_string2(self):
        self.assertRaises(
            TypeError, verificar_qualificacao_empregado, 65, '30')

    def test_aposentadoria(self):
        self.assertEqual(verificar_qualificacao_empregado(
            65, 20), 'Requerer aposentadoria')
        
    def test_aposentadoria2(self):
        self.assertEqual(verificar_qualificacao_empregado(
            59, 30), 'Requerer aposentadoria')
        
    def test_aposentadoria3(self):
        self.assertEqual(verificar_qualificacao_empregado(
            60, 25), 'Requerer aposentadoria')
        
    def test_aposentadoria4(self):
        self.assertEqual(verificar_qualificacao_empregado(
            59, 24), 'Não requerer')


if __name__ == '__main__':
    unittest.main()
