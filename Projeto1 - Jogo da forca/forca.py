import os

forca = [
  """
  |--------|
  |
  |
  |
  |
  """,
  """
  |--------|
  |        o
  |
  |
  |
  """,
  """
  |--------|
  |        o
  |        | 
  |
  |
  """,
  """
  |--------|
  |        o
  |        | \\
  |
  |
  """,
  """
  |--------|
  |        o
  |      / | \\
  |       
  |
  """,
  """
  |--------|
  |        o
  |      / | \\
  |       / 
  |
  """,
  """
  |--------|
  |        o
  |      / | \\
  |       / \\
  |
  """
]

# Função usada para pedir uma letra para o usuario
def getLetra(letrasUsadas):
  letra = input("Escolha uma letra: ")

  # Enquanto o usuario não enviar uma letra valida continua no loop
  while len(letra) != 1 or not letra.isalpha() or letra.lower() in letrasUsadas:
    print("[error] Você deve escolher uma letra que ainda não tenha sido usada")
    letra = input("Escolha uma letra: ")
    
  return letra.lower()

# Verifica se a letra escolhida esta na palavra
def checaLetra(letra, palavra):
  pass

def renderGame(vidas, letrasUsadas, palavraEscondida):
  # Mostra a forca
  print(forca[len(forca) - 1 - vidas])

  # Mostra as letras encontradas
  print(' '.join(palavraEscondida))

  # Mostras as vidas e as letras usadas
  print('\nVidas: {}'.format(' '.join(["\u2764\ufe0f" for x in range(vidas)])))
  print('\nletras usadas: {}\n'.format(', '.join(letrasUsadas)))

# Limpa o terminal
def clearConsole():
    os.system('cls')
    os.system('clear')

def initGame():
  palavra = 'paralelepipedo'
  letrasUsadas = []
  vidas = len(forca) - 1

  # Cria a palavra escondida e um array com todas as letras da palavra
  palavraEscondida = []
  letrasNaoEncontradas = []
  for x in palavra:
    if not x in letrasNaoEncontradas: letrasNaoEncontradas.append(x)
    palavraEscondida.append('_')

  fimDeJogo = False
  while not fimDeJogo:
    # Limpa o terminal
    clearConsole()

    # Verifica se o jogo acabou
    if len(letrasNaoEncontradas) == 0 or vidas == 0:
      result  = 'ganhou' if vidas > 0 else 'perdeu'
      print("Você {}! A palavra era: {}".format(result, palavra))
      fimDeJogo = True
      break

    # Rendezira o game
    renderGame(vidas, letrasUsadas, palavraEscondida)

    # Pede uma letra ao usuario
    letra = getLetra(letrasUsadas)

    # Adiciona essa letra na lista de letras ja escolhidas
    letrasUsadas.append(letra)

    # checa se a letra existe na palavra
    if not letra in letrasNaoEncontradas:
      vidas -= 1
    else:
      letrasNaoEncontradas.remove(letra)
      for index, value in enumerate(palavra):
        if value == letra:
          palavraEscondida[index] = letra

initGame()