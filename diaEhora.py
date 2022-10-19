#recebe dia
dias = int(input("Dias:"))
#recebe hora
horas = int(input("Horas:"))
#recebe minutos
minutos = int(input("Minutos:"))
#recebe segundos
segundos = int(input("Segundos:"))
# Um dia tem 24 horas, logo 24 * 3600 segundos
# Uma hora tem 3600 (60 * 60) segundos50
# Um minuto tem 60 segundos


total_em_segundos = dias * 24 * 3600 + horas * 3600 + minutos * 60 + segundos
print("Convertido em segundos é igual a %10d segundos." % total_em_segundos)