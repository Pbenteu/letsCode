import os
from Loja import loja
from datetime import datetime, timedelta

# TODO criar classe do cliente
class cliente(object):
  pass

config = {
  "comandos": {
    1: {"Texto": "Digite 1 para ver as bicicletas disponiveis"},
    2: {"Texto": "Digite 2 para alugar bicicletas"},
    3: {"Texto": "Digite 3 para avançar o tempo"},
    4: {"Texto": "Digite 4 para listar bicicletas alugadas"},
    5: {"Texto": "Digite 5 para devolver bicicletas"},
  }
}

currentTime = datetime.now()

lojaDeBicicletas = loja(5)

bicicletasAlugadas = []

# Limpa o console
def clearConsole():
  os.system('cls' if os.name == 'nt' else 'clear')

# Pede um numero inteiro ao usuario
def getInt(text):
  while True:
    num = input(text)
    if not num.isnumeric():
      print("Input invalido")
      continue

    return int(num)

# Printa o menu
def printMenu():
  print('')
  for x in config['comandos']:
    print(config['comandos'][x]['Texto'])
  print('')

# Pega um comando valido do usuario
def getComando():
  while True:
    comando = input("Digite o numero do comando que deseja executar: ")
    if not comando.isnumeric() or not int(comando) in config['comandos']:
      print("ERRO - Codigo invalido")
      continue

    return int(comando)

def printBicicletasAlugadas(lista):
  for x in lista:
    print(f"Id: {x['id']}, Nome: {x['nome']}, Alugada em: {x['alugadaEm'].strftime('%d/%m/%Y %H:%M:%S')}, ")


while True:
  print(f"Data atual: {currentTime.strftime('%d/%m/%Y %H:%M:%S')}")
  printMenu()

  comando = getComando()

  clearConsole()

  if comando == 1:
    bicicletas = lojaDeBicicletas.getBicicletasDisponiveis()
    print(f"Existem {bicicletas} bicicletas disponiveis")
  
  if comando == 2:
    qntBicicletas = getInt("quantas bicicletas voce quer alugar? ")
    bicicletas = lojaDeBicicletas.alugarBicicletas(qntBicicletas, currentTime)
    if not bicicletas:
      print("Quantidade de bicletas em estoque insuficiente")
      continue

    bicicletasAlugadas = bicicletas
    printBicicletasAlugadas(bicicletasAlugadas)

  if comando == 3:
    horas = getInt("Quantas horas deseja avançar? ")
    currentTime = currentTime + timedelta(hours=horas)
  
  if comando == 4:
    printBicicletasAlugadas(bicicletasAlugadas)

  if comando == 5:
    bicicleta = getInt("Qual bicicleta deseja devolver? ")
    total = lojaDeBicicletas.devolverBicicleta(bicicleta, currentTime)
    print(f"Total a pagar: R$ {total}")