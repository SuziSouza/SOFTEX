# frutas.py

# Criando o conjunto de frutas
frutas = {'maçã', 'banana', 'manga', 'laranja'}

# Adicionando uma nova fruta
frutas.add('uva')

# Removendo elementos existentes
frutas.discard('banana')  # discard evita erro se o elemento não existir
frutas.discard('manga')

# Mostrando o conjunto atualizado
print("Frutas disponíveis:")
print(frutas)
