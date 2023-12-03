lista = ['a','b','c','d']
print=lista(2)

notas = [[10,20],[30,40],[50,60],[70,80]]
print(notas[1])
print(notas[0])
print(notas[2][1])

print(notas)
for i in range(4):
    print(notas[0])

print(f"total de linhas: {len(notas)}")
for i in range (len(notas)):
    for coluna in range (len(notas[0])):
        print(notas[0][coluna], end = '/t')
    print()