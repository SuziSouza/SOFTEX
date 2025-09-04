# Criando a lista inicial de alunos
alunos = ["Bruno", "Ana", "Carlos", "Denise", "Felipe"]

print("Lista original:", alunos)

# Ordenando a lista em ordem decrescente (Z → A)
alunos.sort(reverse=True)
print("Lista em ordem decrescente:", alunos)

# Acessando o aluno Felipe
indice_felipe = alunos.index("Felipe")   # descobre a posição
print(f"O aluno na posição {indice_felipe} é {alunos[indice_felipe]}")

# Acessando a aluna Ana
indice_ana = alunos.index("Ana")
print(f"A aluna na posição {indice_ana} é {alunos[indice_ana]}")
