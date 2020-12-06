kol_people = 0
health_people = []     #массив, в котором отображается имя человека, его состояние здоровья, его "порядковый номер"
proverka = 0 # проверка новый ли человек
time = []
doma=[]   # массив с коэфицентами заражения домов (в последствии на основании данных массива будет оповещение о заразности домов)
kk=0
time_print = []
time_print_2 = []
time_interval = 30
dangerous_homes = []
very_dangerous_homes = []
print ('-------- Data base ---------')
people = '0'        
for i in range (kol_people):
	health_people.append([i,0])


while people!='':
	proverka = 0
	time = []        # time - масcив, в которм содержится все временные точки 1 дня. точки задаются интервалами time_interval (10 строка)
	for i in range (0, 24 * 60 + time_interval,time_interval):
		time.append([i])
	time_print =[]     # time_print - массив, где будут только важные временные точки (когда примерно находились люди где-то )
	# проверка введено ли имя
	people = ''
	people = input('имя человека')
	if people == '':
		break
	#информация о человеке, в будующем получение данных с сайта
	health = int(input('самочувствие')) # актуализация своего состояния
	for s in range (len(health_people) - 1):
		if health_people[s][2] == people:
			if health_people[s][1] > 0:
				health_people[s][1] = health
			proverka = 1
	# зачисление нового человека в базу данных
	if proverka == 0:
		health_people.append([kol_people,health,people])

	print(kol_people,'человек. ',end = '')
	if proverka == 0:
		kol_people+=1

	kol_domov = int(input('сколько точек пребывания '))
	for i in range (0,1):
		for l in range (kol_domov):
			time_people_1 = int(input('начало пребывания '))

			if time_people_1 % time_interval < time_interval // 2:
				time_people_1 = time_people_1 // time_interval
			else:
				time_people_1 = time_people_1 // time_interval + 1
			time_people_2 = int(input('конец пребывания '))

			if time_people_2 % time_interval < time_interval // 2:
				time_people_2 = time_people_2 // time_interval
			else:
				time_people_2 = time_people_2 // time_interval + 1
			ooo = 0
			dom = input('дом ')
			for i in range (len(doma)): # зачисление нового дома в базу домов
				if dom == doma[i][0]:
					ooo = 1
					break
			if ooo == 0:
				doma.append([dom,0])
			for j in range (time_people_1,time_people_2 + 1):
				time[j].append([dom,kol_people - 1,health_people[kol_people - 1][1]])
	for i in range(len(time)):
		if len(time[i])>1:
			time_print.append(time[i])
	#обновление списка людей 
	# time_print_2 отличается от time_print тем, что он не обнуляется каждую итерацию и имеет симуляцию заражения (конечный массив)
	if kol_people == 1: #первичное заполнение
		for i in range (len(time_print)):       
	
			time_print_2.append([time_print[i][0]])  
			for j in range (1,len(time_print[i])):
				time_print_2[i].append([])
				time_print_2[i][j] = [time_print[i][j][0], health_people[ time_print[i][j][1] ][0],health_people[ time_print[i][j][1] ][1]]
	else:	#вторичное заполнение

		
		for x in range(len(time_print)):
			kk = 0

			if time_print[x][0] < time_print_2[0][0]:
				time_print_2.append([time_print[x][0]])
				time_print_2[len(time_print_2)-1].append([])
				time_print_2[len(time_print_2)-1][1] = [time_print[x][1][0], health_people[ time_print[x][1][1] ][0],health_people[ time_print[x][1][1] ][1]]
				kk = 1
			for i in range(len(time_print_2)):
				if kk == 1:
					break
				
				if time_print[x][0] ==time_print_2[i][0]:

					time_print_2[i].append([])
					time_print_2[i][len(time_print_2[i])-1].append(time_print[x][1][0])
					time_print_2[i][len(time_print_2[i])-1].append(health_people[ time_print[x][1][1] ][0])
					time_print_2[i][len(time_print_2[i])-1].append(health_people[ time_print[x][1][1] ][1])	
					kk = 1
					break


			if kk == 0:
				time_print_2.append([time_print[x][0]])
				time_print_2[len(time_print_2)-1].append([])
				time_print_2[len(time_print_2)-1][1] = [time_print[x][1][0], health_people[ time_print[x][1][1] ][0],health_people[ time_print[x][1][1] ][1]]

	for i in range (len(time_print_2)):                         #сортировка массива по значениям времени
		for j in range (len(time_print_2)):
			if time_print_2[i][0] < time_print_2[j][0]:
				time_print_2[i],time_print_2[j] = time_print_2[j],time_print_2[i]

	#Симуляция заражения
	for i in range (len(time_print_2)):     # 6 - больной 3 - контакт с больным 4 - ожидание тестов 5 - есть симптомы коронавируса 2 - конакт с неподтверждённым случаем 1 - очень маловероятно болен (контакт с 2) 0 - здоров или контакт с 1
		for j in range (1,len(time_print_2[i])):
			if health_people[ time_print_2[i][j][1] ][1] == 6: 
				for z in range (1,len(time_print_2[i]) ):
					
					if time_print_2[i][j][0] == time_print_2[i][z][0]  and time_print_2[i][z][2] < 3 and j!=z:
						health_people[time_print_2[i][z][1]] = ([[ time_print_2[i][z][1] ][0], 2 , health_people[time_print_2[i][z][1]][2]])						
						time_print_2[i][z][2] = health_people[time_print_2[i][z][1]][1]

						for l in range (i,len(time_print_2)):
							for o in range (1,len(time_print_2[l])):
								if time_print_2[l][o][1] == time_print_2[i][z][1]:
									time_print_2[l][o][2] = 3
			elif health_people[ time_print_2[i][j][1] ][1] > 2: 
				for z in range (1,len(time_print_2[i]) ):
					
					if time_print_2[i][j][0] == time_print_2[i][z][0]  and time_print_2[i][z][2] < 2 and j!=z:
						health_people[time_print_2[i][z][1]] = ([[ time_print_2[i][z][1] ][0], 2 , health_people[time_print_2[i][z][1]][2]])						
						time_print_2[i][z][2] = health_people[time_print_2[i][z][1]][1]

						for l in range (i,len(time_print_2)):
							for o in range (1,len(time_print_2[l])):
								if time_print_2[l][o][1] == time_print_2[i][z][1]:
									time_print_2[l][o][2] = 2

			elif health_people[ time_print_2[i][j][1] ][1] > 1:
				for z in range (1,len(time_print_2[i]) ):
					
					if time_print_2[i][j][0] == time_print_2[i][z][0]  and time_print_2[i][z][2] < 1 and j!=z:
						health_people[time_print_2[i][z][1]] = ([[ time_print_2[i][z][1] ][0], 1 , health_people[time_print_2[i][z][1]][2]])
						time_print_2[i][z][2] = health_people[time_print_2[i][z][1]][1]

						for l in range (i,len(time_print_2)):
							for o in range (1,len(time_print_2[l])):
								if time_print_2[l][o][1] == time_print_2[i][z][1]:
									time_print_2[l][o][2] = 1 
	

	print()
	print ('---------- people ----------')
	print(health_people )
	print()
	print('-------- time --------')

	
	# вывод массива времени и вычесление коэффицентов на домах	
	for i in range(len(time_print_2)):
			
		for j in range(1,len(time_print_2[i])):
			
			if time_print_2[i][j][2] > 0:
				for k in range (len(doma)):
					if time_print_2[i][j][0] == doma[k][0]:
						doma[k][1] += time_print_2[i][j][2]
		print(time_print_2[i])
	print()
	print('-----homes-----')
	print(doma)
	dangerous_homes = [] #опасные и особо опасные дома
	very_dangerous_homes = [] 
	for i in range (len(doma)): # обновление коэффицентов на домах, вывод массива домов и просчитывание опасных домов
		if doma[i][1] > 1000:
			very_dangerous_homes.append(doma[i][0])
		elif doma[i][1] > 100:
			dangerous_homes.append(doma[i][0])
		doma[i][1] = 0	

	# вывод опасных домов
	if len (very_dangerous_homes) != 0:
		print ('особо опасные дома (если зайти, точно заразишься) : ', end = '' )
		for i in range (len(very_dangerous_homes) - 1 ):
			print(very_dangerous_homes[i], end = ', ')
		print(very_dangerous_homes[i])
	
	if len (dangerous_homes) != 0:
		print ('опасные дома: ', end = '' )
		for i in range (len(dangerous_homes) -1 ):
			print(dangerous_homes[i], end = ', ')
		print(dangerous_homes[i])
	
	
