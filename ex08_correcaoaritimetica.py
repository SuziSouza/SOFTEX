total_itens = 25  
total_cestas = 4  

# Correções:
# divisão inteira para itens por cesta
itens_por_cesta = total_itens // total_cestas  

# resto da divisão para itens que sobraram
itens_restantes = total_itens % total_cestas  

print(f"Itens por cesta: {itens_por_cesta}") 
print(f"Itens restantes: {itens_restantes}")
