# palavras_unicas.py

# Frase de exemplo
frase = "o gato e o cachorro brincam no jardim o gato pula"

# Dividindo a frase em palavras
palavras = frase.split()

# Criando um conjunto para pegar apenas palavras únicas
palavras_unicas = set(palavras)

# Contando o número de palavras únicas
numero_unico = len(palavras_unicas)

# Mostrando o resultado
print(f"Número de palavras únicas na frase: {numero_unico}")
print(f"Palavras únicas: {palavras_unicas}")
