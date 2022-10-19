print("\ Estimativa da Redução de Vida de um Fumante \n")

#Entrada de dados
qtde_cigarros = int(input("Quantidade de Cigarros Fumados por Dia: "))
anos_fum = int(input("Quantidade de anos Fumando: "))

#Calculo de redução de tempos de vida
#1 ano = 365 dias
qtde_dias = anos_fum * 365
total_cigarros = qtde_dias * qtde_cigarros

#1 dia = 24 horas = 1440 min = 86400 seg
#1 hora = 60 min = 3600 seg  
#1 min = 60 seg

minutos_perdidos = total_cigarros * 10
dias_perdidos = float(minutos_perdidos / 1440)

#Imprimindo resultado na tela
print("")
print("Dias de Vida Perdidos: %d" %dias_perdidos)