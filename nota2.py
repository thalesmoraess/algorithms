nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
nota3 = float(input("Terceira nota: "))

media = (nota1 + nota2 + nota3) / 3
print("Média: ", media)

if media < 5.0:
    print("Reprovado")
elif media < 10:
    print("Aprovado")
else:
    print("Aprovado com distinção!")