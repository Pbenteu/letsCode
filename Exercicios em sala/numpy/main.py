import numpy as np

lista = [1,2,3,4,5]
newLista = np.array(lista)
print(newLista)

# Numero de dimenções do array
newLista.ndim

# Numero de elementos no array
newLista.size

# Formato da lista, quantos elemtos tem em cada dimenção
newLista.shape

# Retorna um array com 10 zeros
my_array = np.zeros(10)
print(my_array)

# Crie uma função que receba um numpy array e retorne um array de 20 elementos contendo apenas o maior elemento do array recebido
def func(array):
  max_ = array.max()
  return np.full(20, max_)
print(func(newLista))
