import unittest
from Loja import loja
from datetime import datetime, timedelta

class TestLoja(unittest.TestCase):

    # Testa alugar uma bicicleta
    def testAlugaBicicleta(self):
        lojaDeBicicletas = loja(5)
        currentTime = datetime.now()

        bicicletas = lojaDeBicicletas.alugarBicicletas(1, currentTime)
        
        self.assertEqual(bicicletas[0]['alugadaEm'], currentTime, "Should be current time")
        self.assertEqual(bicicletas[0]['disponivel'], False, "Should be current time")
        self.assertEqual(bicicletas[0]['pacoteFamilia'], False, "Should be current time")
    
    # Testa devolver uma bicicleta
    def testDevolverBicicleta(self):
      lojaDeBicicletas = loja(5)
      currentTime = datetime.now()

      bicicletas = lojaDeBicicletas.alugarBicicletas(1, currentTime)

      currentTime = currentTime + timedelta(hours=244)

      total = lojaDeBicicletas.devolverBicicleta(0, currentTime)

      self.assertEqual(total, 195, "Should be 195")

    # Testa se um erro é retornado ao tentar alugar mais bicicletas do que se tem no estoque
    def testAluguelMaiorQueEstoque(self):
      lojaDeBicicletas = loja(5)
      currentTime = datetime.now()

      bicicletas = lojaDeBicicletas.alugarBicicletas(6, currentTime)

      self.assertEqual(bicicletas, False, "Should be False")
    
    # Testa o desconto da promoção familia
    def testPromocaoFamilia(self):
        lojaDeBicicletas = loja(5)
        currentTime = datetime.now()
        
        bicicletas = lojaDeBicicletas.alugarBicicletas(3, currentTime)

        currentTime = currentTime + timedelta(hours=245)

        total = lojaDeBicicletas.devolverBicicleta(0, currentTime)

        self.assertEqual(total, 140, "Should be 140")

if __name__ == '__main__':
    unittest.main()