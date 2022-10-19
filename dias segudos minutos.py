dias = int(input("dias:"))
horas = int(input("horas:"))
minutos = int(input("minutos:"))
segundos = int(input("segundos:"))
sd=dias*86400
sh=horas*3600
sm=minutos*60
st=segundos+sd+sh+sm
print(st)
