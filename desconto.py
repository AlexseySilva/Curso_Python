# Solicita o preço do produto ao usuário
p = float(input('Qual o preço do produto? '))
# Solicita o percentual de desconto ao usuário
x = int(input('De quanto será o desconto? '))
# Calcula o valor do desconto
d = (p / 100) * x
# Calcula o valor final do produto com desconto
v = p - d
# Exibe o resultado formatado
print('O produto que custava R${:.2f}, com {}% de desconto vai custar R${:.2f}'.format(p, x, v))