meta_1 = 20000
meta_2 = 40000
vendas = float(input("digite total de vendas:"))
if vendas >= meta_1 and not vendas >= meta_2:
  print("voce recebera bonus 3%")
elif vendas>= meta_2 :
  print("voce recebera bonus 7%")
else:
  print("voce nao atingiu a meta nao recebera bonus")

