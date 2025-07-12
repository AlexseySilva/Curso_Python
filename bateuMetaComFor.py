vendas = [1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 70,
          90, 80, 1100, 999, 900, 880, 870, 50, 1111, 120,
          300, 450, 800]
meta = 1000

qtdeBateuMeta = 0

for venda in vendas:
    if venda >= meta:
        qtdeBateuMeta += 1

qtdeFuncionarios = len(vendas)
print(qtdeBateuMeta)
print(qtdeFuncionarios)

print('O percentual de pessoas que bateram a meta foi de {:.0%}'.format(qtdeBateuMeta / qtdeFuncionarios)) 