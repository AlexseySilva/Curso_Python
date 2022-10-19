nome = input("digite seu nome:")
distancia = int(input("digite a distancia a percorrer:"))
velocidade = int(input("digite a velocidade media:"))

tempo_medio = distancia/velocidade
print(tempo_medio)

hora = str(tempo_medio)

if tempo_medio > 10:
     hora = hora[0] + hora [1] # ou hora = hora [:2]
else:
    hora = hora[0]
print(hora)

resto = tempo_medio - int(hora)
print(resto)

minutos = int(60 * resto)
print("{},sua viagem gastou {}h e {}min".format(nome,hora,str(minutos)))
