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
        
        txt = """|0000|016|0|01072022|31072022|TESTE LTDA|11111111000191||MG|111111111111|3125101|||B|0|
|0001|0|
|0002|09|
|0005|TESTE LTDA|37640000|ESTM XXX XXX XXX|1300||DOS XXXX|3531979985|||
|0015|RJ|111111111|
|0015|SP|111111111111|
|0100|XXXX XXX XXXX XXXX|11111111111|SPXXXXXXX||12914001|AVENIDA ANTONIO PIRES PIMENTEL|XXXX||CENTRO|111111111|111111111|xxxx@xxxx.com.br|3507605|
|0150|CLI000000503|CONSTRUTONI MATERIAIS PARA CON|1058|05923344000196||7012595100085|3170107||AVENIDA ORLANDO RODRIGUES DA CUNHA|35||VL SAO VICENTE|
|0150|FOR000028800|TRANSPORTADORA Y23 EIRELI|1058|39848198000101||0039007510061|3125101||RUA ANTONIO MOREIRA FILHO|50||DOS TENENTES|
|0150|FOR000026707|EFIZI AZU COMERCIO LTDA|1058|34229157000105||083582452|3205002||RUA 7 A|69|SETOR B SALA 1|CIVIT II|
|0200|DESP00191|BIODIGESTOR 700L - FORTLEV|||156|07|||00||18||
|C100|1|0|CLI000000503|55|00|001|38111|31220737008145000149550010000381111212144153|11072022|11072022|4155,75|1|0|0|3582,24|0|0|0|0|3582,24|429,87|5574,32|573,51|0|52,01|239,58|0|0|
|C190|010|5401|12|4155,75|3582,24|429,87|5574,32|573,51|0|0||
|C195|8|Debito para a sub-apuracao|
|C100|1|0|FOR000026707|55|00|001|37862|31220737008145000149550010000378621423637667|05072022|05072022|949,5|1|0|0|949,5|9|0|0|0|949,5|66,47|0|0|0|14,57|67,11|0|0|
|C190|000|6118|7|949,5|949,5|66,47|0|0|0|0||
|C195|8|Debito para a sub-apuracao|
|C197|MG23000999|Debito para a sub-apuracao do produto 500133|500133|949,5|7|66,47|0|
|C197|MG24000999|Debito para a sub-apuracao do produto 500180|500180|3582,24|12|429,87|0|
|D100|0|1|FOR000028800|57|00|001||870|31220739848198000101570010000008701000000007|05072022|13072022|0||1851,86|0|9|1851,86|0|0|1851,86||4214|3125101|3205101|
|D190|000|2352|0|1851,86|0|0|0||
"""
        with open('efd.txt', 'w') as f:
            f.write(txt)        
        
        efd = ArquivoDigital()
        efd.readfile("efd.txt")
        efd.prepare()
        self.assertEqual("TESTE LTDA", efd.abertura.NOME)
        self.assertEqual("11111111000191", efd.abertura.CNPJ)
        print(efd)

if __name__ == '__main__':
    unittest.main()