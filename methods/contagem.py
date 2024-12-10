# contar quantas vezes o elemento 7 aparece na lista:

lista = [1, 7, 2, 7, 3, 7, 4, 5, 6]
cont = 0
for i in range(len(lista)):
    if lista[i] == 7:
        cont += 1
print(cont)


# outra maneira com o método count():

lista = [1, 7, 2, 7, 3, 7, 4, 5, 6]
cont = lista.count(7)
print(cont)