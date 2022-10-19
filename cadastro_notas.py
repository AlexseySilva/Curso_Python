# Cadastro do nome do aluno e sua nota em uma lista

qtde_alunos = int(input('Quantos alunos para lançar nota?'))
disciplina= []
for i in range(qtde_alunos):
    nome = input('Qual o nome do aluno?')
    nota = input('Qual o a nota?')
    resultado = [nome, 'nota:{}'.format(nota)]
    disciplina.append(resultado)

print(disciplina)
