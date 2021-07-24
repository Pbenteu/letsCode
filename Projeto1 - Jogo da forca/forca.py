import os
import requests
from bs4 import BeautifulSoup
import math

config = {
  'vidas': 8,
  'minLenPalavra': 5
}

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
  |       😁
  |
  |
  |
  """,
  """
  |--------|
  |       😀
  |        | 
  |
  |
  """,
  """
  |--------|
  |       😐
  |        | \\
  |
  |
  """,
  """
  |--------|
  |       😢
  |      / | \\
  |       
  |
  """,
  """
  |--------|
  |       😭
  |      / | \\
  |       / 
  |
  """,
  """
  |--------|
  |       😵
  |      / | \\
  |       / \\
  |
  """
]

desenhoPessoaPerdeu = """
|--------|
|       😵
|      / | \\
|       / \\
|
"""

desenhoPessoaGanhou = """
|--------|
|  🎊       🎉  
|     \\ 🥳 /
|        | 
|       / \\
"""

# Faz um request para um gerador de palavras online e usa webscraping para retirar a palavra do HTML
def getPalavra():
  # Faz o request 
  html = requests.get("https://www.palabrasaleatorias.com/palavras-aleatorias.php?fs=1&fs2=1&Submit=Nova+palavra").content
  soup = BeautifulSoup(html, 'html.parser')
  
  # Encontra a palavra
  palavra = soup.select_one('div[style*="font-size:3em; color:#6200C5;"]')

  # Limpa a palavra e retornas
  palavra = palavra.string.strip().lower()

  # Se a palavra for menor que o minimo da config busca outra palavra
  return palavra if len(palavra) >= config['minLenPalavra'] else getPalavra()

# Função usada para pedir uma letra para o usuario
def getLetra(letrasUsadas):
  letra = input("Escolha uma letra: ")

  # Enquanto o usuario não selecionar uma letra valida continua no loop
  while len(letra) != 1 or not letra.isalpha() or letra.lower() in letrasUsadas:
    print("[error] Você deve escolher uma letra que ainda não tenha sido usada")
    letra = input("Escolha uma letra: ")
    
  return letra.lower()

def renderGame(vidas, letrasUsadas, palavraEscondida):
  # Mostra a forca
  forcaLength = len(forca) - 1
  forcaIndice = forcaLength - math.ceil((vidas / (config['vidas'] / forcaLength)))
  print(forca[forcaIndice])

  # Mostra as letras encontradas
  print(' '.join(palavraEscondida))

  # Mostras as vidas e as letras usadas
  print('\nVidas: {}'.format(' '.join(["\u2764\ufe0f" for x in range(vidas)])))
  print('\nletras usadas: {}\n'.format(', '.join(letrasUsadas)))

# Mostra o resultado do jogo
def renderResult(vidas, palavra):
  clearConsole()

  final = desenhoPessoaGanhou if vidas > 0 else desenhoPessoaPerdeu
  result  = 'ganhou' if vidas > 0 else 'perdeu'

  print(final)
  print("Você {}! A palavra era: {}".format(result, palavra))

# Limpa o terminal, só funciona no windows
def clearConsole():
    os.system('cls')

def initGame():
  print("Buscando uma palavra...")
  palavra = getPalavra()

  letrasUsadas = []
  vidas = config['vidas']

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
          
    # Verifica se o jogo acabou
    if len(letrasNaoEncontradas) == 0 or vidas == 0:
      fimDeJogo = True
      renderResult(vidas, palavra)
      
initGame()