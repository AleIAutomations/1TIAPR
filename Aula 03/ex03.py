#exemplo 3-------------------------------

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# adicionando um elemento (100) a segunda linha na primeira posição
matriz[1].insert(0, 100)

# imprimindo a matriz atualizada
for linha in matriz:
    print(linha)