import random

N = 20
M = 3

# criar uma matriz NxM preenchida com zeros
matriz = []
for linha in range(N):
    matriz.append([0]*M)

# adicionar elementos aleatórios à matriz e contar números pares
numeros_pares = 0
for linha in range(N):
    for coluna in range(M):
        elemento = random.randint(0, 100)  # gera números aleatórios de 0 a 100
        matriz[linha][coluna] = elemento
        if elemento % 2 == 0:
            numeros_pares += 1

# imprimir a matriz
print("Matriz:")
for linha in range(N):
    for coluna in range(M):
        print(matriz[linha][coluna], end='\t')
    print()

# imprimir a quantidade de números pares
print(f"\nQuantidade de números pares na matriz: {numeros_pares}")
