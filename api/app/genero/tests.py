import unittest
from . import hooks

class TestGeneroModule(unittest.TestCase):

    def test_normaliza_nome_genero(self):
        generoObj = {"nome":"   heAvy meTaL   "}
        result = hooks.normaliza_nome_genero(generoObj)
        self.assertEqual(result["nome"],"Heavy Metal")