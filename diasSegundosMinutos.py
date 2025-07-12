# Solicita ao usuário a quantidade de dias
dias = int(input("Dias: "))
# Solicita ao usuário a quantidade de horas
horas = int(input("Horas: "))
# Solicita ao usuário a quantidade de minutos
minutos = int(input("Minutos: "))
# Solicita ao usuário a quantidade de segundos
segundos = int(input("Segundos: "))

# Converte dias, horas e minutos para segundos
sd = dias * 86400  # 1 dia = 86400 segundos
sh = horas * 3600  # 1 hora = 3600 segundos
sm = minutos * 60  # 1 minuto = 60 segundos

# Soma todos os segundos
st = segundos + sd + sh + sm
# Exibe o total de segundos
print(st)
