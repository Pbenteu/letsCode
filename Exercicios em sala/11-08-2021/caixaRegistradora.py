class produto(object):

  def __init__(self, descricao, valor, quantidade):
    self.descricao = descricao
    self.valor = valor
    self.quantidade = quantidade
    
  def __repr__(self):
    return f'Producto {self.descricao} - valor: {self.valor} - quantidade: {self.quantidade}'

estoque = [
  produto('Pasta de dente', 3, 10),
  produto('Escova', 5, 2),
  produto('Sabonete', 2, 4),
]

diatemplate = {
  'muito baixo': 0,
  'baixo': 0,
  'normal': 0,
  'alto': 0,
  'muito alto': 0
}


class compra(object):

  produtos = {}
  total = 0

  def adicionarProduto(self, index, quantidade):
    index = int(index)
    if not index in self.produtos:
      self.produtos[index] = 0

    if (self.produtos[index] + quantidade) > estoque[int(index)].quantidade:
      print("Item fora de estoque")
      return False

    self.produtos[index] += quantidade
    self.total += estoque[int(index)].valor

  def finalizarCompra(self):
    for index in self.produtos:
      index = int(index)
      produto = estoque[index]
      total = int(produto.valor) * int(self.produtos[index])
      print(f'{produto.descricao}, {self.produtos[index]} unidades: R${int(total):.2f}')
    
    print(f'Total: R${self.total},00')

  def receberPagamento(self, valorPago):
    if valorPago < self.total:
      print("Valor insuficiente")
      return False

    troco = valorPago - self.total
    print(f'Troco: R${troco}')
    return True


carrinhoDeCompras = compra()

for index, produto in enumerate(estoque):
  print(f'{index}: {produto}')

fimDasCompras = False
while not fimDasCompras:
  produtoSelecionado = input('O que voce gostaria? Escolha pelo index: ')

  if produtoSelecionado == 'fim':
    fimDasCompras = True
    break
  
  carrinhoDeCompras.adicionarProduto(produtoSelecionado, 1)

carrinhoDeCompras.finalizarCompra()
valorPago = int(input("Insira o valor que voce dara: "))

pago = False
while not pago:
  pago = carrinhoDeCompras.receberPagamento(valorPago)