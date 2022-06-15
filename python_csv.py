import csv

with open('Measurement_info.csv', newline='', encoding="utf8") as file:
	micsv = csv.reader(file, delimiter=',')
	for lineaCSV in micsv:
		print(lineaCSV)

# Measurement date,Station code,Item code,Average value,Instrument status

#horario: 
#si es < 08h MADRUGADA
#si es < 15:00h COMIDA
#si es < 22:00h TARDE
#sino: NOCHE
#valor: >5 ALTO sino BAJO
#estado: ROTO OK

mes_dia = lineaCSV[0][5:10]
horario = lineaCSV[0][11:16]
if(horario < '08:00'):
  horario = 'MADRUGADA'
elif(horario < '15:00'):
  horario = 'COMIDA'
elif(horario < '22:00'):
  horario = 'TARDE'
else:
  horario = 'NOCHE'
valor = float(lineaCSV[-2])
if(valor >5):
  valor = 'ALTO'
else:
  valor = 'BAJO'
estado = int(lineaCSV[-1])
if(estado == 0):
  estado = 'OK'
else:
  estado = 'ROTO'



result = [mes_dia, horario, valor, estado]
print(result)