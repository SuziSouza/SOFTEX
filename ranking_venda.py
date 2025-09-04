# ranking_vendas.py

# Lista de vendedores
vendedores = ['João', 'Maria', 'Pedro', 'Ana']

# Imprimindo posição e valor usando enumerate, começando do número 1
for posicao, vendedor in enumerate(vendedores, start=1):
    print(f"{posicao}º lugar: {vendedor}")
