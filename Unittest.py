# -*- coding: utf-8 -*-
import py_compile
import unittest
import Maior_e_Menor_Tested

class test_program (unittest.TestCase):

    def test_ct01(self):
        self.assertEqual(Maior_e_Menor_Tested.maior_e_menor('a', 'b', 'c'), "Entrada inválida, a entrada não é um número inteiro.")
    
    def test_ct02(self):
        self.assertEqual(Maior_e_Menor_Tested.maior_e_menor('a', 1, 2), "Entrada inválida, a entrada não é um número inteiro.")
    
    def test_ct03(self):
        self.assertEqual(Maior_e_Menor_Tested.maior_e_menor('a', 1, 'c'), "Entrada inválida, a entrada não é um número inteiro.")

    def test_ct04(self):
        self.assertEqual(Maior_e_Menor_Tested.maior_e_menor(999, 1000, 1001), "Entrada inválida, um ou mais números inseridos não estão entre 0 e 1000.")
    
    def test_ct05(self):
        self.assertEqual(Maior_e_Menor_Tested.maior_e_menor(-1, 0, 1), "Entrada inválida, um ou mais números inseridos não estão entre 0 e 1000.")
    
    def test_ct06(self):
        self.assertEqual(Maior_e_Menor_Tested.maior_e_menor(0, 1, 2), 'O maior número digitado foi 2, e o menor foi 0')
    
    def test_ct07(self):
        self.assertEqual(Maior_e_Menor_Tested.maior_e_menor(998, 999, 1000), 'O maior número digitado foi 1000, e o menor foi 998')
    
    def test_ct08(self):
        self.assertEqual(Maior_e_Menor_Tested.maior_e_menor(462, 943, 738), 'O maior número digitado foi 943, e o menor foi 462')
    
if __name__ == '__main__':
    unittest.main()