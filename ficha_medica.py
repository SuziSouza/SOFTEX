# ficha_medica.py

# Criando o dicionário do paciente
paciente = {
    'nome': 'João',
    'idade': 35,
    'peso': 80,
    'altura': 1.75
}

# Corrigindo o valor da altura
paciente['altura'] = 1.80

# Mostrando o dicionário atualizado
print("Dados atualizados do paciente:")
for chave, valor in paciente.items():
    print(f"{chave}: {valor}")
