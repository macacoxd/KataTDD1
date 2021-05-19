import unittest
from src.conjunto import Conjunto


class TestConjunto(unittest.TestCase):
    def test_conjunto_vacio_retornaNone ( self ) :
        conjunto = Conjunto ([ ])
        self.assertIsNone(conjunto.promedio( ))

    def test_conjunto_unElemento_RetornaValorUnicoElemento ( self ) :
        conjunto = Conjunto ([ 5 ])
        self.assertEqual(5,conjunto.promedio( ))

    def test_conjunto_dosElemento_RetornaValorPromedioElementos ( self ) :
        conjunto = Conjunto ([ 5,7 ])
        self.assertEqual(6,conjunto.promedio( ))

    def test_conjunto_NElemento_RetornaValorPromedioElementos ( self ) :
        conjunto = Conjunto([2,4,8,9,10,15])
        self.assertEqual((2+4+8+9+10+15)/6,conjunto.promedio())