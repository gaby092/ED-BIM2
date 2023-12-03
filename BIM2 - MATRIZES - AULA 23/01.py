"""
1 - Programa que armazena os nomes e idades de 10 pessoas em uma matriz, e imprime o nome da pessoa mais nova
"""
# Iinicializa uma matriz vazia para armazenar os nomes e idades
pessoas = []

# pede ao usuário para inserir os nomes e idades de 10 pessoas
for i in range(10):
    nome = input(f"digite o nome da pessoa {i+1}: ")
    idade = int(input(f"digite a idade de {nome}: "))
    pessoas.append([nome, idade])

# encontra a pessoa mais nova na matriz
pessoa_mais_nova = min(pessoas, key=lambda x: x[1])

# imprime o nome da pessoa mais nova
print(f"a pessoa mais nova é {pessoa_mais_nova[0]} com {pessoa_mais_nova[1]} anos.")
