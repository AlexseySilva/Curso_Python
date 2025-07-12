# Cadastro de notas com for range
quantidadeAlunos = int(input("Quantos alunos vamos adicionar?"))
disciplina = []
for i in range(quantidadeAlunos):
    nome = input('Qual o nome do aluno?')
    nota = input("Qual a nota do aluno?")
    resultado = [nome, 'nota:{}'.format(nota)]
    disciplina.append(resultado)
print(disciplina) 