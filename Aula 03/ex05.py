#exemplo 5-----------------------------------

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# iterar sobre cada linha da matriz
for linha in matriz:
    #interar sobre cada elemento da linha
    for elemento in linha:
        print(elemento, end=' ')
        print()
# imprimir uma nova linha após cada linha da matriz
