# Lendo 5 números inteiros e armazenando em uma lista
numeros = []
for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

# Mostrando na ordem lida
print("Ordem original:", numeros)

# Mostrando na ordem inversa
print("Ordem inversa:", numeros[::-1])
