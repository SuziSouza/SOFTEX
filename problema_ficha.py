# meus_dados.py

# Criando o dicionário com dados pessoais
meus_dados = {
    'nome': 'Alice',
    'idade': 35,
    'cidade': 'Nova York'
}

# Adicionando uma nova chave-valor
meus_dados['profissao'] = 'Médica'

# Modificando o valor da chave 'idade'
meus_dados['idade'] = 40

# Acessando e imprimindo o valor da chave 'cidade'
print(f"Cidade: {meus_dados['cidade']}")

# Exibindo o dicionário completo
print("Dicionário atualizado:")
for chave, valor in meus_dados.items():
    print(f"{chave}: {valor}")
