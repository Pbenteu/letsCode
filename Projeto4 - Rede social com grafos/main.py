from classes.usuario import Usuario
from classes.rede import RedeSocial

rede = RedeSocial()

def printTopInfluencers(influencers):
  print('\nTOP INFLUENCERS')
  for x in topInfluencers:
    userName = x['usuario'].userName
    seguidores = x['seguidores']
    print(f'{userName}: {seguidores} seguidores')

# Adiciona os usuarios a rede
with open('dados/usuarios.csv', 'r') as usuarios:
  for usuario in usuarios.readlines():
    usuario = usuario.rstrip('\n').split(',')
    usuario = Usuario(usuario[0], usuario[1])
    rede.adicionarUsuario(usuario)
  
# Adiciona os seguidores a rede
with open('dados/conexoes.csv', 'r') as conexoes:
  for conexao in conexoes.readlines():
    conexao = conexao.rstrip('\n').split(',')
    rede.seguirUsuario(conexao[0], conexao[1], int(conexao[2]))

# Pede ao usuario os usuarios que seram buscados
usuario1 = input('Escolha um usuario a pesquisar: ')
usuario2 = input('Escolha outro usuario: ')
  
# Printa a quantidade de seguidores de um usuario
seguidores = len(rede.getSeguidores(usuario1))
print('QUANTIDADE DE PESSOAS QUE SEGUEM O USUARIO')
print(seguidores)

# Printa a quantidade de pessoas que um usuario segue
seguindo = rede.getQuantidadeSeguindo(usuario1)
print('\nQUANTIDADE DE PESSOAS QUE O USUARIO SEGUE')
print(seguindo)


# Printa a lista de stories
listaStories = rede.listStories(usuario1)
lista = []
for x in listaStories:
  lista.append(x['usuario'].userName)
print("\nLISTA DE PRIORIDADE DOS STORIES")
print(', '.join(lista))

# Printa os top k influencers
topInfluencers = rede.getInfluencers(3)
printTopInfluencers(topInfluencers)

# Printa o menor caminho entre 2 usuarios
caminho = rede.getCaminhoUsuarios(usuario1, usuario2)
print('\nMENOR CAMINHO ENTRE 2 USUARIOS')
print(caminho)