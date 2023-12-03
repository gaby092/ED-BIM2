"""
2- Faça um programa que leia uma matriz 3x3 e multiplique os elementos da diagonal principal da matriz por um
número k. Imprima a matriz na tela antes e depois da multiplicação.
ex:     
input
|  4     6    9 |
|  3     2    7 |
|  1     2    5 |

ouput, suponha k = 5
|  20     6     9 |
|  3       10    7 |
|  1     2      25 |
"""
def multiplica_diagonal_principal(matriz, k):
    # imprime a matriz original
    print("matriz original:")
    for linha in matriz:
        print("|", end=" ")
        for elemento in linha:
            print(f"{elemento:4}", end=" ")
        print("|")

    # multiplica os elementos da diagonal principal por k
    for i in range(len(matriz)):
        matriz[i][i] *= k

    # imprime a matriz após a multiplicação
    print("\nmatriz após a multiplicação:")
    for linha in matriz:
        print("|", end=" ")
        for elemento in linha:
            print(f"{elemento:4}", end=" ")
        print("|")

# solicita ao usuário que insira os elementos da matriz 3x3
matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        elemento = int(input(f"digite o elemento da posição ({i+1},{j+1}): "))
        linha.append(elemento)
    matriz.append(linha)

# solicita ao usuário que insira o valor de k
k = int(input("digite o valor de k: "))

# chama a função para multiplicar a diagonal principal por k e imprimir a matriz
multiplica_diagonal_principal(matriz, k)
