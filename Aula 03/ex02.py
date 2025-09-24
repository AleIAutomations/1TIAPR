#exemplo 2---------------------------------

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

#adicionando uma nova linha a matriz

nova_linha = [10, 11, 12]
matriz.append(nova_linha)

# imprimindo a matriz atualizada
for linha in matriz:
    print(linha)