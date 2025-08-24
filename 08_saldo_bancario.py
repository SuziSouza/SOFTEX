saldo_bancario = 1000.0

deposito = float(input("Digite o valor do depósito: "))
saque = float(input("Digite o valor do saque: "))
juros = float(input("Digite o fator de juros: "))

saldo_bancario += deposito
saldo_bancario -= saque
saldo_bancario *= juros

print(f"Saldo final: {saldo_bancario}")
