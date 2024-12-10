# esse método possibilita adicionar a uma lista
# o conteúdo de outro objeto de sequência ou iterável
# (objeto cujos elementos podem ser recuperados um por vez).
# Caso o iterável seja uma string,cada caractere é adicionado individualmente.
# Neste exemplo, cada caractere da string 'pera' é adicionado individualmente:

x = ["maçã", "limão", "banana", "laranja"]
x.extend("pera")
print(x)