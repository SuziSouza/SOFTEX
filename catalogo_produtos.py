# catalogo.py

# Criando o dicionário com o primeiro produto
catalogo = {
    'Mouse Gamer': {'preço': 150.00, 'estoque': 50}
}

# Adicionando um novo produto
catalogo['Teclado Mecânico'] = {'preço': 450.00, 'estoque': 30}

# Mostrando todas as chaves e valores do dicionário
for produto, detalhes in catalogo.items():
    print(f"Produto: {produto}")
    for chave, valor in detalhes.items():
        print(f"  {chave}: {valor}")
