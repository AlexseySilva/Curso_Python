i = 1
notas = []
print("Digite as 5 notas do aluno:")
while i <= 5:
    nota = int(input(f"Digite a nota {i}:"))
    notas.append(nota)
    i += 1

x = 0
while x < len(notas):
    print(f"Nota {x} é: {notas[x]}")
    x += 1

print("Fim") 