i = 1
nota = []
print("digite as 5 notas do aluno:")
while i<= 5:
    n = int(input("digite a nota %d:" %i))
    nota.append(n)
    i += 1

x = 0
while x < len(nota):
    print("nota %d é:" % x, nota[x])
    x += 1

print("Fim")
