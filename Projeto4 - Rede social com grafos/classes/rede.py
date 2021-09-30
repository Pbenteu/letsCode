from classes.usuario import Usuario

class RedeSocial(object):

  def __init__(self):
    self.matrizAdjacencia = {}
    self.config = {
      # Peso 1 é amigo, peso 2 é melhor amigo
      "pesos": [1, 2]
    }

  # Busca um usuario na matriz com base no userName
  def findUser(self, userName):
    for usuario in self.matrizAdjacencia:
      if usuario.userName == userName:
        return usuario
    
    return False

  def adicionarUsuario(self, vertice):
    if not isinstance(vertice, Usuario):
      return 'Vertice deve ser um objeto do tipo Usuario'

    self.matrizAdjacencia[vertice] = {}
  
  # Função usada para seguir um usuario, pode ser amigo ou melhor amigo
  def seguirUsuario(self, usuario, usuarioSeguido, peso = 1):
    if peso != 1 and peso != 2:
      return 'Peso invalido'

    usuario = self.findUser(usuario)
    usuarioSeguido = self.findUser(usuarioSeguido)

    if usuario and usuarioSeguido:
      if not usuarioSeguido in self.matrizAdjacencia[usuarioSeguido]:
        self.matrizAdjacencia[usuario][usuarioSeguido] = peso
        return True

      print('Cadastro duplicado')
      return False     

    print('Erro ao seguir')
    return False
  
  # Printa a matriz de usuarios
  def __str__(self) -> str:
      usuarios = ''
      for usuario in self.matrizAdjacencia:
        usuarios += f'{repr(usuario)}\n'
      return usuarios  
  
  # Busca os seguidores de uma pessoa
  def getSeguidores(self, userName):
    usuario = self.findUser(userName)

    seguidores = []
    for key, value in self.matrizAdjacencia.items():
      if usuario in value:
        seguidores.append({
          "usuario": key,
          "tipo": value[usuario]
        })

    return seguidores

  # Retorna a quantidade de pessoa que um usuario segue
  def getQuantidadeSeguindo(self, userName):
    usuario = self.findUser(userName)
    return len(self.matrizAdjacencia[usuario])

  # Retorna a ordem que os stories devem ser mostrados (igual a como funciona no instagram)
  def listStories(self, userName):
    # Pessoas que tem o usuario sendo buscado como melhor amigo
    pessoaQueTemUsuarioComoMelhorAmigo = []
    for x in self.getSeguidores(userName):
      if x['tipo'] == 2:
        pessoaQueTemUsuarioComoMelhorAmigo.append(x['usuario'])
    
    # Busca o usuario na rede
    usuario = self.findUser(userName)

    # Cria as lista de amigos e melhores amigos com base nas pessoas que consideram o usuario melhor amigo
    amigos = []
    melhoresAmigos = []
    for x in self.matrizAdjacencia[usuario]:
      if x in pessoaQueTemUsuarioComoMelhorAmigo:
        melhoresAmigos.append({'usuario': x, 'name': x.name})
      else:
        amigos.append({'usuario': x, 'name': x.name})
    
    return self.mergeSortUsuarios(melhoresAmigos, 'name') + self.mergeSortUsuarios(amigos, 'name')
    
    # Cria uma lista de melhores amigos 

  # Busca os top "qnt" pessoas com mais seguidores
  def getInfluencers(self, qnt):
    pessoas = {}
    for x in self.matrizAdjacencia.values():
      for y in x:
        if not y in pessoas:
          pessoas[y] = {'usuario': y, 'seguidores': 0}
        pessoas[y]['seguidores'] += 1
    
    return self.mergeSortUsuarios(list(pessoas.values()), 'seguidores')[0-qnt:]

  # TODO: Encontrar o caminho entre uma pessoa e outra na rede
  def getCaminhoUsuarios(self, userNameInicio, userNameFim):
    inicio = self.findUser(userNameInicio)
    fim = self.findUser(userNameFim)

    jaVisitados = []
    filaAVisitar = [inicio]
    verticeAnterior = {inicio: None}

    while len(filaAVisitar) > 0:
      for x in self.matrizAdjacencia[filaAVisitar[0]]:
        if not x in jaVisitados:
          # Adiciona o novo usuario a lista de predescesores
          verticeAnterior[x] = filaAVisitar[0]

          # Se o item X for o usuario que estamos buscando para o while
          if x == fim:
            break

          # Adiciona o usuario na fila
          filaAVisitar.append(x)

      # Se o loop não for interrompido o else é invocado dando continue e impedindo o break do while
      else:
        jaVisitados.append(filaAVisitar[0])
        filaAVisitar.pop(0)
        continue
      
      break

    string = fim.userName
    item = verticeAnterior[fim]
    while item != None:
      string = f'{item.userName} -> ' + string
      item = verticeAnterior[item]
    
    return string

  def mergeSortUsuarios(self, lista, key):
    if len(lista) == 1:
      return lista

    else:
      meio = len(lista)//2
      sort1 = self.mergeSortUsuarios(lista[:meio], key)
      sort2 = self.mergeSortUsuarios(lista[meio:], key)

      newLista = []
      end = False
      cursor1 = 0
      cursor2 = 0
      while not end:
        if sort1[cursor1][key] > sort2[cursor2][key]:
          newLista.append(sort2[cursor2])
          cursor2+=1
        else:
          newLista.append(sort1[cursor1])
          cursor1+=1
          
        if cursor1 == len(sort1):
          while cursor2 < len(sort2):
            newLista.append(sort2[cursor2])
            cursor2+=1
          end = True
        elif cursor2 == len(sort2):
          while cursor1 < len(sort1):
            newLista.append(sort1[cursor1])
            cursor1+=1
          end = True
      
      return newLista