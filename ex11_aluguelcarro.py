km = float(input("Digite a quantidade de Km percorridos: "))
dias = int(input("Digite a quantidade de dias de aluguel: "))

preco = (dias * 60) + (km * 0.15)
print(f"O preço a pagar é R$ {preco}")
