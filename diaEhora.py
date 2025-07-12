# Solicita ao usuário a quantidade de dias
dias = int(input("Dias: "))
# Solicita ao usuário a quantidade de horas
horas = int(input("Horas: "))
# Solicita ao usuário a quantidade de minutos
minutos = int(input("Minutos: "))
# Solicita ao usuário a quantidade de segundos
segundos = int(input("Segundos: "))

# Calcula o total em segundos
# 1 dia = 24 * 3600 segundos
# 1 hora = 3600 segundos
# 1 minuto = 60 segundos
total_em_segundos = dias * 24 * 3600 + horas * 3600 + minutos * 60 + segundos

# Exibe o resultado formatado
print("Convertido em segundos é igual a %10d segundos." % total_em_segundos)