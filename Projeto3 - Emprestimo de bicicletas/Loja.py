from datetime import date
from math import floor


class loja(object):

  def __init__(self, quantidadeBicicletas):
    # Config de preço do aluguel
    self.config = {
      "preco": {
        "hora": 5,
        "dia:": 25,
        "semana": 100
      }
    }

    # Cria todas as bicicletas e seta o status para disponivel
    self.bicicletas = []
    for x in range(quantidadeBicicletas):
      self.bicicletas.append({
        "id": x,
        "nome": f"bicicleta {x}",
        "disponivel": True,
        "alugadaEm": False,
        "pacoteFamilia": False
      })

  def getBicicletasDisponiveis(self):
    return len([x for x in self.bicicletas if x['disponivel']])
  
  def alugarBicicletas(self, qntBicicletas, time):
    if self.getBicicletasDisponiveis() < qntBicicletas:
      return False

    pacoteFamilia = True if qntBicicletas >= 3 else False 
    
    bicicletas = []
    for x in self.bicicletas:
      if x['disponivel']:
        x['disponivel'] = False
        x['alugadaEm'] = time
        x['pacoteFamilia'] = pacoteFamilia
        bicicletas.append(x)
      if len(bicicletas) == qntBicicletas:
        break

    return bicicletas

  def devolverBicicleta(self, id, time):
    diff = (time - self.bicicletas[id]['alugadaEm']).total_seconds()

    semanas = floor(diff / 604800)
    resto = diff % 604800
    dias = floor(resto / 86400)
    resto = resto % 86400
    horas = floor(resto / 3600)

    total = semanas * 100 + dias * 25 + horas * 5

    if self.bicicletas[id]['pacoteFamilia']: total = total * 0.7
    
    self.bicicletas[id]['disponivel'] = True
    self.bicicletas[id]['alugadaEm'] = False
    self.bicicletas[id]['pacoteFamilia'] = False

    return total