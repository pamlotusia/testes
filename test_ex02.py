import unittest


def soma(a, b):
    if type(a) == int and type(b) == int:
        return a + b
    else:
        raise TypeError('Tipos incompativeis')


class TesteSoma(unittest.TestCase):
    def test_funcao_soma(self):
        self.assertEqual(soma(10, 5), 15)

    def test_excecao_tipos_incompativeis(self):
        self.assertRaises(TypeError, soma, 10, '5')


if __name__ == '__main__':
    unittest.main()
