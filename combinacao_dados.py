# combinacao_clientes_saldos.py

# Lista de clientes
clientes = ['João', 'Maria', 'José']

# Lista de saldos correspondentes
saldos = [1500, 2500, 800]

# Imprimindo clientes e seus saldos usando enumerate e zip
for i, (cliente, saldo) in enumerate(zip(clientes, saldos), start=1):
    print(f"{i}. {cliente} - Saldo: R${saldo}")
