def main():
    nota = int(input("Digite uma nota: "))

    if nota < 30:
        print("Reprovado")
    elif nota < 60:
        print("Recuperação")
    else:
        print("Aprovado")