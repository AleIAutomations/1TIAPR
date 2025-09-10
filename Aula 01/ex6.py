# Solicita a idade da pessoa
idade = int(input("Digite sua idade: "))

# Verifica se a idade é suficiente para votar
if idade >= 16:
    print("Você pode votar!")
else:
    print("Você ainda não pode votar.")
