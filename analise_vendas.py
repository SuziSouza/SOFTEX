# Criando a tupla com produto e quantidade
venda = ("Caderno", 15)

# Preço unitário
preco_unitario = 25.00

# Calculando o valor total
produto, quantidade = venda
valor_total = quantidade * preco_unitario

print("Produto:", produto)
print("Quantidade:", quantidade)
print(f"Valor total da venda: R$ {valor_total:.2f}")
