# Criando a lista inicial com os produtos
estoque = ["camiseta", "calça", "meia", "jaqueta"]

print("Estoque inicial:", estoque)

# Adicionando o novo produto "boné"
estoque.append("boné")
print("Após chegada do novo produto:", estoque)

# Removendo o produto "calça" (sem estoque)
estoque.remove("calça")
print("Após remover produto sem estoque:", estoque)
