import keyboard
from tabulate import tabulate
import os
import copy

class jogo(object):

  # Configuração basica de variaveis utilizadas no jogo
  def __init__(self):
    self.player1 = '❌'
    self.player2 = '⭕️'
    self.tie = 'empate'
    self.square = '⬜️'
    self.squareX = '❎'
    self.squareO = '🅾️'

    self.tabuleiro = [
      [self.player1, '', ''],
      ['', '', ''],
      ['', '', ''],
    ]

    self.currentSquareCords = [1, 1]

  # Printa o tabuleiro
  def printTabuleiro(self):
    # Cria uma copia do tabuleiro
    novoTabuleiro = copy.deepcopy(self.tabuleiro)

    # Altera o icone caso o quadrado seja um quadrado que ja foi selecionado
    squareDisplay = self.square
    if self.tabuleiro[self.currentSquareCords[0]][self.currentSquareCords[1]] == self.player1:
      squareDisplay = self.squareX
    elif self.tabuleiro[self.currentSquareCords[0]][self.currentSquareCords[1]] == self.player2:
      squareDisplay = self.squareO

    # Adiciona o quadrado de jogada ao tabuleiro
    novoTabuleiro[self.currentSquareCords[0]][self.currentSquareCords[1]] = squareDisplay
    
    # Printa o jogo
    print("Use as setas direcionais para controlar")
    print("Aperte ENTER para definir a jogada")
    print("Precione ESC para sair")
    print(f"Você: {self.player2}")
    print(f"Computador: {self.player1}")
    print(tabulate(novoTabuleiro, tablefmt="fancy_grid"))

  # Lida com os comandos vindos do teclado
  def handleKeyPress(self, key):
    # Anda com o quadrado pelo tabuleiro
    if key == 'up':
      newCord = self.currentSquareCords[0]-1
      if newCord < 0:
        return
      self.currentSquareCords[0] = newCord

    elif key == 'down':
      newCord = self.currentSquareCords[0]+1
      if newCord > 2:
        return
      self.currentSquareCords[0] = newCord

    elif key == 'left':
      newCord = self.currentSquareCords[1]-1
      if newCord < 0:
        return
      self.currentSquareCords[1] = newCord

    elif key == 'right':
      newCord = self.currentSquareCords[1]+1
      if newCord > 2:
        return
      self.currentSquareCords[1] = newCord
    
    # Ao pressionar enter faz a jogada
    elif key == 'enter':
      # 
      self.tabuleiro[self.currentSquareCords[0]][self.currentSquareCords[1]] = self.player2

      # Jogada do usuario
      self.clearConsole()
      ganhador = self.checaFimDeJogo(self.tabuleiro)
      if ganhador:
        self.finalizaJogo(ganhador)
      self.printTabuleiro()

      # Jogada do computador
      self.getJogadaComputador()
      ganhador = self.checaFimDeJogo(self.tabuleiro)
      if ganhador:
        self.finalizaJogo(ganhador)
      self.printTabuleiro()
      return
      
    self.clearConsole()
    self.printTabuleiro()

  def clearConsole(self):
    os.system('cls' if os.name == 'nt' else 'clear')

  def getTextPrevisao(self, jogada):
    if jogada[self.player1] == 1:
      return f"Jogador {self.player1} ganhara"
    elif jogada[self.player2] == 1:
      return f"Jogador {self.player2} ganhara"
    else:
      return "Sera empate"

  def getJogadaComputador(self):
    jogada = self.simulaJogada(self.tabuleiro, self.player1)
    self.clearConsole()

    print(self.getTextPrevisao(jogada))
    self.tabuleiro[jogada['jogada'][0]][jogada['jogada'][1]] = self.player1
  
  def getJogadasPossiveis(self, t):
    jogadasPossiveis = []
    for index1, linha in enumerate(t):
      for index2, coluna in enumerate(linha):
        if coluna == '':
          jogadasPossiveis.append([index1, index2])
    return  jogadasPossiveis

  def simulaJogada(self, t, player):
    jogadasPossiveis = self.getJogadasPossiveis(t)

    melhorJogada = {}

    for jogada in jogadasPossiveis:
      newT = copy.deepcopy(t)
      newT[jogada[0]][jogada[1]] = player
      fim = self.checaFimDeJogo(newT)
      
      if not fim:
        # Alterna entre os players
        newPlayer = self.player1
        if player == self.player1:
          newPlayer = self.player2

        # Calcula o proximo nivel
        result = self.simulaJogada(newT, newPlayer)
        if result[player] == 1:
          result['jogada'] = jogada
          return result
        elif result[self.tie] == 1 or melhorJogada == {}:
          result['jogada'] = jogada
          melhorJogada = result  

      else:
        # Se o jogador puder ganhar em uma jogada
        if fim == player:
          result = {'jogada': jogada, self.player1: 0, self.tie: 0, self.player2: 0}
          result[player] = 1

          return result

        # Se não existir melhor jogada ainda seta essa como a melhor jogada
        if melhorJogada == {}:
          melhorJogada = {'jogada': jogadasPossiveis[0], self.player1: 0, self.tie: 0, self.player2: 0}
          melhorJogada[fim] = 1

    return melhorJogada
    
  def checaFimDeJogo(self, t):
    # Checa verticais
    if t[0][0] == t[1][0] == t[2][0] and t[0][0] != '':
      return t[0][0]
    elif t[0][1] == t[1][1] == t[2][1] and t[0][1] != '':
      return t[0][1]
    elif t[0][2] == t[1][2] == t[2][2] and t[0][2] != '':
      return t[0][2]
    # Checa horizontais
    elif t[0][0] == t[0][1] == t[0][2] and t[0][0] != '':
      return t[0][0]
    elif t[1][0] == t[1][1] == t[1][2] and t[1][0] != '':
      return t[1][0]
    elif t[2][0] == t[2][1] == t[2][2] and t[2][0] != '':
      return t[2][0]
    # Checa diagonais
    elif t[0][0] == t[1][1] == t[2][2] and t[0][0] != '':
      return t[0][0]
    elif t[0][2] == t[1][1] == t[2][0] and t[0][2] != '':
      return t[0][2]
    else:
      # Checa se foi empate
      for linha in t:
        for coluna in linha:
          if coluna == '':
            return False

      return self.tie
  
  def finalizaJogo(self, ganhador):
    keyboard.unhook_all_hotkeys()
    self.printTabuleiro()
    if ganhador == self.tie:
      print("Empate!")
    else:
      print(f"{ganhador} ganhou!")
    
    print("Pressione ESC para sair")
    keyboard.wait('esc')

  def start(self):
    keys = ["up", "down", "left", "right", "enter"]
    for x in keys:
      keyboard.add_hotkey(x, lambda x=x: self.handleKeyPress(x))

    self.printTabuleiro()

    keyboard.wait('esc')


jogo = jogo()
jogo.start()