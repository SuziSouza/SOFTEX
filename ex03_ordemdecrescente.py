a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

# Colocamos os valores em uma lista e usamos sort(reverse=True)
numeros = [a, b, c]
numeros.sort(reverse=True)

print("Ordem decrescente:", numeros)
