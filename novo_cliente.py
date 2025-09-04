# clientes.py

# Criando o conjunto de clientes ativos
clientes_ativos = {'Ana', 'Pedro', 'Maria'}

# Criando a lista de novos clientes
novos_clientes = ['João', 'Maria', 'Lucas']

# Adicionando novos clientes ao conjunto, sem duplicatas
clientes_ativos.update(novos_clientes)

# Mostrando o conjunto atualizado
print("Clientes ativos atualizados:")
print(clientes_ativos)
