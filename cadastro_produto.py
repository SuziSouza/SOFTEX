# cadastro_produtos.py

# Listas de nomes, preços e estoques
nomes = ['Teclado', 'Mouse']
precos = [250, 120]
estoques = [10, 25]

# Mesclando os elementos das listas usando zip e mostrando os valores
produtos = list(zip(nomes, precos, estoques))

print("Cadastro de produtos:")
for nome, preco, estoque in produtos:
    print(f"Produto: {nome}, Preço: R${preco}, Estoque: {estoque}")
