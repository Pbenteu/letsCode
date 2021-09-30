from random import randint

def bubleSort(lista):
  for x in range(len(lista) - 1):
    for j in range(len(lista) - x - 1):
      if lista[j] > lista[j+1]:
        lista[j], lista[j+1] = lista[j+1], lista[j]

  return lista

lista = []
for x in range(20):
  lista.append(randint(0, 100))
  
print(lista)
print(bubleSort(lista))