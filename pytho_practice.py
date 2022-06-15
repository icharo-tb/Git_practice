# Python W4

# Coding Order:
    # Zona Librerias
    # Zona Funciones
    # Variables
#a = float(input('Numero 1:'))
#b = float(input('Numero 2:'))
#c = 0 #Resultado
    # Algoritmo
#a **= 2
#b **= 2
#c = (a + b) ** 0.5
    # Resultado
#print('Este es tu numerico:', round(c, 2))
    # round(x, numeroDecimales)

#text_1 = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean at pulvinar lacus. Fusce in purus eu tortor dignissim sodales ut sed sapien. Curabitur vitae turpis urna.'
#print(text_1 * 2)


# Ejercicio 1:

animal = 'Pantera'

print(animal * 3)

# Ejercicio 2:
edad = 23
sexo = 'masc.'
nombre = 'Daniel'

print('La edad es', (edad), ',el género es', (sexo), 'y el nombre es', (nombre))

# Ejercicio 3
pa1 = 3 #int(input('Numero atomico 1:'))
pm1 = 3 #int(input('Numero molecular 1:'))
pa2 = 2 #int(input('Numero atomico 2:'))
pm2 = 1 #int(input('Numero molecular 2:')) # or float if needed (f2 to change all variables with the same name)
pm = 0

pm = (pa1 * pm1) + (pa2 * pm2)

print('El resultado es:', (pm))

#Ejercicio 4:
'''b = 2
a = b
c = 3
d = 4

if(b == 2):
    print('b vale 2')
elif(b == 3 and c == 3):
    print('b no vale 2, pero si vale 3. C también')
else:
    print('b no vale 2ni 3')
print('sigue el programa')'''

tar1 = '100%'
tar2 = '85%'
tar3 = '75%'
tar4 = '50%'

edad = int(input('Edad:'))
trabajo = str(input('¿Trabaja usted?:(Si, No)')) # omitir str, altera el resultado

if(edad >= 18 and trabajo == 'Si'):
    print(tar1)
elif(edad >= 18 and trabajo == 'No'):
    print(tar2)
elif((edad <= 18 and edad > 14) and trabajo == 'Si' ):
    print(tar3)
elif((edad <= 18 and edad > 14) and trabajo == 'No'):
    print(tar4)
else:
    print('Es usted un niño, no paga nada, vieve usted de la renta del estado')

# Ejercicio 5:
'''class Warrior:
    Health = 3000
    Defense = 250
    Attack1 = 300
    Attack2 = 500

class Mage:
    Health = 1500
    Defense = 50
    Attack1 = 1000
    Attack2 = 20000

class Zombie:
    Health = 1000
    Defense = 100
    Attack1 = 35
    
if(Mage.Health >0 and Zombie.Health <0 or Warrior.Health >0 and Zombie.Health <0):
    print('You won this fight')
elif(Mage.Health <0 and Zombie.Health >0 or Warrior.Health >0 and Zombie.Health >0):
    print('Fatality!')'''

'''warrior_hp = 3000
warrior_def = 250
warrior_attack_1 = 300
warrior_attack_2 = 500

mage_hp = 1500
mage_def = 50
mage_attack_1 = 1000
mage_attack_2 = 20000

enemy_hp = 1000
enemy_def = 100
enemy_attack_1 = 35

if(warrior_attack_1 - (enemy_hp + enemy_def)):
    print('You dealed 300 Dmg: Enemy has 750 HP left')
elif(enemy_attack_1 - mage_hp):
    print('You have been attacked: You have 1465 HP left')'''

'''character_choice = input('Choose between Mage or Warrior:')

attack_dmg = {'Mage': 20000, 'Warrior': 300}

for character in attack_dmg:
    if character == character_choice:
        print(attack_dmg[character])
    elif character == character_choice:
        print(attack_dmg[character])'''

'''turno = 1
personaje = 1
vidaPersonaje = 200
vidaAtacante = 1000

if(turno == 1):
    if(personaje == 1):
        vidaAtacante = vidaAtacante - 300
    else:
        vidaAtacante = vidaAtacante 
        - 150
else:
    vidaPersonaje = vidaPersonaje - 20

if(vidaPersonaje <= 0):
    print('Muere tu personaje')
elif(vidaAtacante <= 0):
    print('Muere el enemigo')
else:
    print('No muere nadie')'''
    
pj_choice = input('Elige tu luchador: Kane or Scorpion')
turn_choice = input('Elige quien ataca: Kane or Scorpion')

kane_hp = 1500
scorpion_hp = 1500

patada_dmg = 500
putiaso_dmg = 20000
agarre_dmg = 1000

print('La vida de ambos es de 1500')
print('Round 1... FIGHT!')

if(pj_choice == 'Kane' and turn_choice == 'Kane'):
    attack_choice = input('Elige tu ataque: patada, putiaso o agarre')
    if(attack_choice == 'patada'):
        print('¡Le has hecho algo de pupa a tu oponente!', 'Tu vida restante:', scorpion_hp - patada_dmg)
    elif(attack_choice == 'putiaso'):
        print('FATALITY!!', scorpion_hp - putiaso_dmg)
    elif(attack_choice == 'agarre'):
        print('¡Agarras a tu oponente y lo empujas contra una picadora de carne!', 'Tu vida restante:', scorpion_hp - agarre_dmg)
elif(pj_choice == 'Kane' and turn_choice == 'Scorpion'):
    print('Scorpion te mete una patada-peñetazo y te mata!')
elif(pj_choice == 'Scorpion' and turn_choice == 'Scorpion'):
    attack_choice = input('Elige tu ataque: patada, putiaso o agarre')
    if(attack_choice == 'patada'):
        print('¡Le has hecho algo de pupa a tu oponente!', 'Tu vida restante:', kane_hp - patada_dmg)
    elif(attack_choice == 'putiaso'):
        print('FATALITY!!', kane_hp - putiaso_dmg)
    elif(attack_choice == 'agarre'):
        print('¡Agarras a tu oponente y lo empujas contra una picadora de carne!', 'Tu vida restante:', kane_hp - agarre_dmg)
elif(pj_choice == 'Scorpion' and turn_choice == 'Kane'):
    print('Kane te mete su cuchillo hasta el higadillo y feneces en el acto!')
else:
    print('Error!')


# Ejercicio 6:

socio = input('Es usted socio:(Si, No)')

# Order is important, if we want to cap actions or comands by conditions they must be in order

if(socio == 'Si'):
    user_type = input('Elija que tipo de usuario: Básico(0), Premium(1), PRO(2)')

    book_choice = input('Elija libros pequeños(0) o libros grandes(1)')

    sueldo = float(input('Su sueldo:'))
    if(user_type == '0'):
        if(book_choice == '0'):
            if(sueldo <= 1200):
                print('Se te aplica un 80%, y por tanto este seria el precio de tu libro:', round(24.95 - (24.95 * 0.8),2))
            elif(sueldo > 1200):
                print('Se te aplica un 5%, y por tanto este seria el precio de tu libro:', round(24.95 - (24.95 * 0.05),2))
        elif(book_choice == '1'):
            if(sueldo <= 1200):
                print('Se te aplica un 80%, y por tanto este seria el precio de tu libro:', round(35 - (35 * 0.8),2))
            elif(sueldo > 1200):
                print('Se te aplica un 5%, y por tanto este seria el precio de tu libro:', round(35 - (35 * 0.05),2))
    if(user_type == '1'):
        if(book_choice == '0'):
            if(sueldo <= 1200):
                print('Se te aplica un 80%, y por tanto este seria el precio de tu libro:', round(24.95 - (24.95 * 0.8),2))
            elif(sueldo > 1200):
                print('Se te aplica un 15%, y por tanto este seria el precio de tu libro:', round(24.95 - (24.95 * 0.15),2))
        elif(book_choice == '1'):
            if(sueldo <= 1200):
                print('Se te aplica un 80%, y por tanto este seria el precio de tu libro:', round(35 - (35 * 0.8),2))
            elif(sueldo > 1200):
                print('Se te aplica un 15%, y por tanto este seria el precio de tu libro:', round(35 - (35 * 0.15),2))
    if(user_type == '2'):
        if(book_choice == '0'):
            if(sueldo <= 1200):
                print('Se te aplica un 80%, y por tanto este seria el precio de tu libro:', round(24.95 - (24.95 * 0.8),2))
            elif(sueldo > 1200):
                print('Se te aplica un 45%, y por tanto este seria el precio de tu libro:', round(24.95 - (24.95 * 0.45),2))
        elif(book_choice == '1'):
            if(sueldo <= 1200):
                print('Se te aplica un 80%, y por tanto este seria el precio de tu libro:', round(35 - (35 * 0.8),2))
            elif(sueldo > 1200):
                print('Se te aplica un 45%, y por tanto este seria el precio de tu libro:', round(35 - (35 * 0.45),2))
elif(socio == 'No'):
    print('No es usted socio de nuestra plataforma')
else:
    print('Error')
        

# Ejercicio 7:

a = float(input('Numero 1:'))
b = float(input('Numero 2:'))
c = float(input('Numero 3:'))

if(a > b and a > c):
    print('a es el numero mayor')
    #if(a < b and a < c):
        #print('a no es el numero mayor')
elif(b > a and b > c):
    print('b es el numero mayor')
    #if(b < a and b < c):
        #print('b no es el numero mayor')
elif(c > a and c > b):
    print('c es el numero mayor')
    #if(c < b and c < a):
        #print('c no es el numero mayor')
else:
    print('Error!')
    
# Ejercicio 8:

# week_day = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes']
# week_end = ['Sabado', 'Domingo']
week_day_choice = input('¿Qué dia de la semana es?')

if week_day_choice in ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes']:
    print('¡Todavia tienes dias de clase!')
elif week_day_choice in ['Sabado', 'Domingo']:
    print('¡Es Fin de Semana!')
else:
    print('Error!')

# Ejercicio 9:

my_list = [1, 'Amuno', 'Gal', 2, 'Cervan', 3, ['tor', 4]]
print(my_list [2])
print(my_list [3])
# print(my_list[6][0])
print(len(my_list)) # len: no lee por posiciones de la lista, si no que lee la lista entera y devuelve la cantidad de elementos dentro de la misma

listaJuegos = [ 'a', [1, 2], 'bbbb', 23, [1, 32, 'b', '$$$$', [-99], 4], -2, 3, 4, 6, 2.22 ]

# Cual es el número de elementos en esta lista?
print(len(listaJuegos))
# Cual es la posición de 23?
print(listaJuegos[3], 'esta en la tercera posición de la lista')
# Como puedo acceder a-99?
print(listaJuegos[4][4][0])
print(type(listaJuegos[4][4][0])) # type: nos ayuda a identificar el tipo de dato

# si queremos ver datos desde una posicion en adelante --> x:(x = nunmero de posicion en la lista)
# print(lista[2:]): hasta el final de la lista, print(lista[2:6]): desde 2 hasta 6
# print(lista[:4]): desde el incio hasta la cuarta posicion, print(lista[-2]): empieza a contar desde el ultimo elemento de la lista

mi_frase = 'Python is di bestie'

print(mi_frase.upper())
print(mi_frase.lower()) # tanto lower como upper puedes escribirse en un elemento como x.upper() o x.lower()

mi_frase = 'riukiratb2@gmail.com'

print(mi_frase.split('@')[0]) # separa el contenido del elemento con una criterio dado

mi_frase = 'pato00pato0pato'

print(mi_frase.replace('0', '332')) # remplaza los criterios originales del elemento por otro valor

# Ejercicio 10:

linea = [1, 4, 'H@la', 'me,', 'llamo', '1b8n', '.PyTHon Mola']


linea[2] = linea[2].replace('@', 'o')

linea[3] = linea[3].replace(',', ' ')

linea[5] = linea[5].replace('1', 'I')
linea[5] = linea[5].replace('8', 'o')

linea[6] = linea[6].replace('TH', 'th')
linea[6] = linea[6].replace('M', 'm')
linea[6] = linea[6][1:]

print(linea[2:]) # pendiente de revision

# Ejercicio 11:

'''#lineaCSV = '24, ibonreinsothevalley@gmail.com,n_partidas,bajas,micropagos'

lineaOriginal = '24,ibonreinsothevalley, gmail.com, n_partidas_completadas,n_partidas_no_completadas,bajas,129' #USD --> EURO
lineaSeparada = lineaOriginal.split(',')
print(lineaSeparada)
#1. Crear Variables
edad = lineaSeparada[0]


#2. Manipulamos

lineaDestino = [edad, email, n_partidas, bajas, micropagos]
print(lineaDestino)
# 24,ibonreinsothevalley@gmail.com,n_partidas,bajas,micropagos'''


#lineaCSV = '24, ibonreinsothevalley@gmail.com,n_partidas,bajas,micropagos'

lineaOriginal = '24,ibonreinsothevalley, gmail.com, 22,56,125,129' #USD --> EURO
linea_buena = lineaOriginal.split(',')

edad = int(linea_buena[0])
print('Edad:', edad)
email = linea_buena[1] + '@' + linea_buena[2][1:]
print('Email', email)
n_partidas = int(linea_buena[3]) + int(linea_buena[4])
print('El numero de partidas:', n_partidas)
bajas = int(linea_buena[-2])
print('Numero de bajas:', bajas)
micropagos = int(linea_buena[-1]) * 0.95
print('Micropagos (EUR):', micropagos, '€')

# Ejercicio 12:

# nba_line = ['48, 34, 0.585, 13, 106.4, 104, 2.33, 1991, Milwaukee Bucks']

nba_line = '24, 58, 0.293, 30, 93.9, 99.3, -5.23, 2009, Memphis Grizzlies'

line_new = nba_line.split(',')
percentage = str(round((float(line_new[2]) * 100),2)) + '%'
difference = round(float(line_new[4]) - float(line_new[5]),1)
team = line_new[-3]
if(float(team) > 2):
    team = 'NORMAL'
else:
    team = 'MALO'
year = line_new[-2].replace('1991', '91') #line_new[-2][3:]
capital_let = line_new[-1][1]
if('mil' in capital_let.lower()):
    capital_let = 'M'
elif('mem' in capital_let.lower()):
    capital_let = 'MG'

result = [percentage, difference, team, year, capital_let]
print(result)

# 58.5% = porcentaje 
# 2.4 = diferencia de 106.4 - 104
# >2 entonces equipo = 'NORMAL'
# 91 --> anyo, últimos dos digitos
# Si es Milwaukee entonces inicial = M

'''resultado = [porcentaje, diferencia, equipo, anyo, inicial]
print(resultado)''' #58.5%, 2.4, NORMAL, 91, M

# Ejercicio 13:

# csv COVID: need year as f ([3:])| need difference as diff where high - low| need close as c rounded to 4 (round(x),4)| need volume as v| need name as e where  Facebook = 1 

lineaOrigen = '712, 2020-02-13, 214.3300018310547, 209.17999267578125, 209.52000427246094, 213.13999938964844, 15396600.0, 213.13999938964844, Facebook'

line_new = lineaOrigen.split(',')[1:] # if limited by '[line:]' it starts counting by 0 again
f = line_new[0][3:5]
c = round(float(line_new[-4]),6) #no redondea a 4 debido al 9 periodico del decimal
diff = round(float(line_new[1]) - float(line_new[2]),2)
v = line_new[-3][:-4] # correct coding: float(line_new[-3])/100
e = line_new[-1]
if('FACEBOOK' in e.upper()): # other code way: if(e.lower() == 'facebook')
    e = 1
else:
    e = 2

result = [f, c, diff, v, e]
print(result)

# Ejercicio 14, 15:

import csv


with open('Measurement_info_clean.csv', 'w', newline = '') as f:
  writer = csv.writer(f)
  

  with open('Measurement_info.csv', newline='', encoding="utf8") as file:
    micsv = csv.reader(file, delimiter=',')
    next(file)
    for lineaCSV in micsv:
      #print(lineaCSV)
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



      resultado = [mes_dia, horario, valor, estado]
      #print(resultado)
      writer.writerow(resultado)

    # Ejercicio 16:

    # Age,Attrition,BusinessTravel,DailyRate,Department,DistanceFromHome,Education,EducationField,EmployeeCount,EmployeeNumber,EnvironmentSatisfaction,Gender,HourlyRate,JobInvolvement,JobLevel,JobRole,JobSatisfaction,MaritalStatus,MonthlyIncome,MonthlyRate,NumCompaniesWorked,Over18,OverTime,PercentSalaryHike,PerformanceRating,RelationshipSatisfaction,StandardHours,StockOptionLevel,TotalWorkingYears,TrainingTimesLastYear,WorkLifeBalance,YearsAtCompany,YearsInCurrentRole,YearsSinceLastPromotion,YearsWithCurrManager

    import csv

with open('CSV_clean.csv', 'w', newline='') as j:
  writeibm = csv.writer(j)

  with open('WA_Fn-UseC_-HR-Employee-Attrition.csv', newline= '', encoding='utf8') as job:
    ibmcsv = csv.reader(job, delimiter=',')
    next(job)
    for line_new in ibmcsv:
      jefe = int(line_new[-1])
      if(jefe >5):
        jefe = 'BUENO'
      else:
        jefe = 'MALO'
      anyos_en_ese_puesto = int(line_new[-3])
      if(anyos_en_ese_puesto >3):
        anyos_en_ese_puesto = 'BASTANTES'
      anyos_en_empresa = int(line_new[-4])
      diferencia = int(line_new[-4]) - int(line_new[-3])
      # diferencia = anyos_en_empresa - anyos_en_ese_puesto
      # if(anyos_en_ese puesto >3):
      #     anyos_en_ese_puesto = 'BASTANTES'

      resultado = [jefe, anyos_en_ese_puesto, anyos_en_empresa, diferencia]
      #print(resultado)
      writeibm.writerow(resultado)