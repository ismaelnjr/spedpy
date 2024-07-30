# -*- coding: utf-8 -*-

import unittest
import os
import sys

# Necessário para que o arquivo de testes encontre
test_root = os.path.dirname(os.path.abspath(__file__))
os.chdir(test_root)
sys.path.insert(0, os.path.dirname(test_root))
sys.path.insert(0, test_root)

from sped.efd.icms_ipi.arquivos import ArquivoDigital

class TestICMSIPI(unittest.TestCase):

    def test_read_registro(self):
        
        efd = ArquivoDigital()
        efd.readfile("..\\etc\\efd.txt")
        self.assertEqual("TESTE LTDA", efd._registro_abertura.NOME)

if __name__ == '__main__':
    unittest.main()
