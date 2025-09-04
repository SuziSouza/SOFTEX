# Lista de vendas da semana
vendas_semana = [1200, 1500, 1100, 2000, 2500, 1800, 1300]

# Valor total das vendas
total_vendas = sum(vendas_semana)

# Menor valor de venda
menor_venda = min(vendas_semana)

# Descobrir o dia correspondente
dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
indice_menor = vendas_semana.index(menor_venda)
dia_menor = dias[indice_menor]

print("Vendas da semana:", vendas_semana)
print("Total de vendas:", total_vendas)
print(f"O menor valor foi {menor_venda}, no dia {dia_menor}.")
