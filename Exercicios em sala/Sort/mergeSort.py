from random import randint

def mergeSort(lista):
  if len(lista) == 1:
    return lista

  else:
    meio = len(lista)//2
    sort1 = mergeSort(lista[:meio])
    sort2 = mergeSort(lista[meio:])

    newLista = []
    end = False
    cursor1 = 0
    cursor2 = 0
    while not end:
      if sort1[cursor1] > sort2[cursor2]:
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

lista = []
for x in range(20):
  lista.append(randint(0, 100))

print(lista)
print(mergeSort(lista))

