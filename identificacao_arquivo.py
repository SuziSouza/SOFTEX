# arquivos.py

# Criando a tupla com os nomes dos arquivos
arquivos = ('documento.pdf', 'foto.jpg', 'relatorio.pdf', 'planilha.xlsx')

# Contando quantas vezes a extensão .pdf aparece
pdf_count = sum(1 for arquivo in arquivos if arquivo.endswith('.pdf'))

# Mostrando o resultado
print(f"A extensão .pdf aparece {pdf_count} vezes na tupla.")
