# operador "+"
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

# operador "*"
x = [0] * 4
print(x)
y = [1, 2, 3] * 3
print(y)

# operador ":"
lista = ["a", "b", "c", "d", "e", "f"]
print(lista[1:3])
print(lista[:4])
print(lista[3:])

# Em lista[1:3], estamos informando que a fatia (slice) deve iniciar
# no segundo elemento da lista (listas iniciam no índice 0) e deve
# terminar no quarto elemento, mas sem incluí-lo. De acordo com o
# resultado da execução, esse comando resulta em uma lista com dois
# elementos, correspondentes ao segundo e ao terceiro elementos da
# lista original.

# Em lista[:4], como não especificamos o primeiro valor, iniciamos
# no primeiro elemento da lista e terminamos no quinto elemento, sem
# incluí-lo, resultando em uma lista com os quatro primeiros elementos
# da lista original.

# Por último, em lista[3:], o slice é executado a partir do quarto
# elemento; como o segundo parâmetro não foi especificado, vamos até
# o final da lista original.