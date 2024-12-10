# esse método permite excluir a primeira ocorrência
# de cada item em uma lista. Caso o item não seja encontrado, é gerado
# um ValueError. Observe o exemplo abaixo com a string 'maçã':

x = ["maçã", "limão", "banana", "laranja", "limão"]
x.remove("limão")
print(x)