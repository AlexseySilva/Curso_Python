meta = 20000
vendas = int(input("Valor de vendas:"))
if vendas < meta:
    print("Não ganhou bônus")
elif vendas > (meta * 2):
    bonus = 0.07 * vendas
    print(f"Ganhou {bonus} de bônus")
else:
    bonus = 0.03 * vendas
    print(f"Ganhou {bonus} de bônus") 