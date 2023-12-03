"""
Uma pista de Kart permite 10 voltas para cada um de 6 corredores. Faça um programa que leia os nomes e os tempos (em segundos) de cada volta de cada corredor e guarde as informações em uma matriz. Ao final, o programa deve informar:

a) De quem foi a melhor volta da prova, e em que volta
b) Classificação final em ordem (1º o campeão)
c) Qual foi a volta com a média mais rápida
"""
# Função para calcular a média de uma coluna específica da matriz
def calcular_media(matriz, coluna):
    soma = sum(matriz[i][coluna] for i in range(len(matriz)))
    return soma / len(matriz)

# Leitura dos tempos de cada volta para cada corredor
corredores = 6
voltas = 10
tempos = []

for i in range(corredores):
    tempos_corredor = []
    print(f"Corredor {i+1}:")
    for j in range(voltas):
        tempo = int(input(f"digite o tempo da volta {j+1} (em segundos): "))
        tempos_corredor.append(tempo)
    tempos.append(tempos_corredor)

# calculo da melhor volta da prova e em que volta
melhor_volta = min(min(tempos[i]) for i in range(corredores))
corredor_melhor_volta = [i + 1 for i in range(corredores) if melhor_volta in tempos[i]][0]
volta_melhor_volta = tempos[corredor_melhor_volta - 1].index(melhor_volta) + 1

# calculo da classificação final
classificacao_final = sorted(range(1, corredores + 1), key=lambda x: sum(tempos[x-1]))

# calculo da volta com a média mais rápida
media_volta_rapida = min((calcular_media(tempos, j), j) for j in range(voltas))
volta_media_rapida = media_volta_rapida[1] + 1

# Impressão dos resultados
print("\nresultado:")
print(f"a melhor volta da prova foi do Corredor {corredor_melhor_volta} na volta {volta_melhor_volta}.")
print(f"classificação final em ordem (1º o campeão): {classificacao_final}")
print(f"a volta com a média mais rápida foi a volta {volta_media_rapida}.")

