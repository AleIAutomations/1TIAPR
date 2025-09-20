#calcule a soma de numeros positivos forecidos pelo usuario, encerrando quando um nuemro negativo for inserido.

acumulador = 0
num = int(input("digite um numero:"))
while num >= 0:
    acumulador += num
    num = int(input("digite um numero:"))
print(f"A soma dos numeros é: {acumulador}")