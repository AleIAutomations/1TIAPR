matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# usando "de1" para remover a segunda linha
del matriz[1]

# imprimindo a matriz após a remoção da segunda linda
print("matriz apos a remoção da segunda linha:")
for linha in matriz:
    print(linha)

# usando "pop" para remover e obter o elemento na terceira coluna da primeira linha
elemento = matriz[0].pop(2)
print("\nElemento removido", elemento)

# imprimindo a matriz após a remoção do elemento
print("\nMatriz após a remoção do elemento:")
for linha in matriz:
    print(linha)