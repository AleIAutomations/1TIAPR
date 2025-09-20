#crie um jogo de advinhação de um numero entre 1 e 10, com 3 tentativas

import random
tentativas = 3
# numero = random.randint(1, 10)
numero = 7

while tentativas > 0:
    palpite = int(input("Digite um numero entre 1 e 10"))
    if palpite == numero:
        print("PArabens! voce acertou")
        break
    else:
        tentativas -= 1
        print("voce errou ")
        
