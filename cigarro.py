print("\nEstimativa da redução de vida de um fumante\n")

# Entrada de dados
qtdeCigarros = int(input("Quantidade de cigarros fumados por dia: "))
anosFumando = int(input("Quantidade de anos fumando: "))

# Cálculo de redução de tempo de vida
qtdeDias = anosFumando * 365
totalCigarros = qtdeDias * qtdeCigarros

minutosPerdidos = totalCigarros * 10
diasPerdidos = float(minutosPerdidos / 1440)

# Imprimindo resultado na tela
print("")
print(f"Dias de vida perdidos: {diasPerdidos:.0f}") 