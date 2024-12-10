# Pense na seguinte situação: um professor faz cinco
# trabalhos durante o semestre, cada um valendo 10 pontos.
# Para obter a nota final dos alunos, ele pode digitar as notas obtidas
# ao término dos cinco trabalhos e dividir por 5.
# Observe o exemplo no código a seguir:

notas = []
for item in range(1,6):
    nota = float(input("Digite a nota %s: " % item))
    notas.append(nota)

    media = 0
for item in notas:
    media = media + item

print(media/5)