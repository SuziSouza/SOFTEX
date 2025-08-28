idade_motorista = int(input("Qual a sua idade? "))
tem_carteira = input("Você tem carteira de motorista? (True/False): ")

# Converter a entrada para booleano
tem_carteira = tem_carteira.lower() == "true"

# Corrigindo: precisa ser >= 18 e carteira True
pode_dirigir = (idade_motorista >= 18) and tem_carteira

print(f"Pode dirigir? {pode_dirigir}")
