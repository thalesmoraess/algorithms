# agora, vamos aprender como criar
# listas baseadas em outras listas
# e/ou objetos iteráveis, com a possibilidade de
# aplicar filtros de maneira mais eficiente.
# Em Python, isso é chamado de "list comprehension".

# o código abaixo utiliza a list comprehension para filtrar
# uma lista, gerando uma nova lista:

notas = [0, 0, 9.0, 8.0, 5.0, 10.0, 7.0, 7.5, 4.0, 10.0, 7.0, 7.0, 8.0, 8.0, 7.5]

notas_validas = [nota for nota in notas if nota > 0] # list comprehension
print(notas_validas)

notas_org = sorted(notas_validas)
print(notas_org)

# a função sorted() foi chamada com o intuito de que as
# notas válidas fossem organizadas em ordem crescente.
