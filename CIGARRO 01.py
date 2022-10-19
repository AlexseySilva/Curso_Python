cigarros = int(input("Informe a qtd de cigarros fumaddos por dia:"))
anos = int(input("Informe a qtde de anos que fumou:"))
perda_min = 10
total_min_dia = cigarros * perda_min
total_dias = anos * 365
total_min = total_min_dia * total_dias
total_horas = total_min / 60
total_dias = total_horas / 24
print("Você tem {:.2f} dias a menos de vida por ter fumado por esse tempo".format(total_horas/24))
print("ou{:.2f} anos".format(total_dias/365))
