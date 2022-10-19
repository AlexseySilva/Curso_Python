#Vamos fazer um cadastro de notas com for range. Pergunte a quantidade de notas a
#serem lidas. Crie uma lista chamada disciplina e dentro dela insira o nome do aluno e a
#nota. Dentro do for você deverá perguntar o nome do aluno e a nota e atribuir esses
#valores a uma lista chamada alunos, e depois adicionar esses dados na lista disciplina
#que inicialmente está vazia.
#No caso de lançar notas para três alunos, a impressão da lista disciplina deverá ser algo
#parecido com isso:
#Disciplina[[‘João’, ‘nota: 7’], [‘Ana’, ‘nota: 8’], [‘André’, ‘nota: 10’]]



QuantidadeDeAlunos= int(input("Quantos alunos vamos adicionar?"))
disciplina = []
for i in range(QuantidadeDeAlunos):
        nome = input('Qual o nome do aluno?')
        nota = input("qual a nota do aluno?")
        resultado = [nome,'nota:{}'.format(nota)]
        disciplina.append(resultado)
print(disciplina)        