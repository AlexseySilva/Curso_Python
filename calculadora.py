num_1 =int(input("Digite o primeiro numero :"))
num_2 =int(input("Digite o segundo numero :"))
operacao = input("Qual operação você gostaria de fazer?""\nadicao = +\ndivisao = /\nsubtracao = -\nmultiplicacao = *\ndigite a operação:")
if operacao == "+":
     print(num_1 + num_2)
elif operacao =="-":
     print(num_1 - num_2)
elif operacao =="*":
     print(num_1 * num_2)
elif operacao =="/":
     print(num_1 / num_2)
else:
     print('operação invalida.')
