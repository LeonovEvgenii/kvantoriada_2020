kol_people = 0
health_people = []
proverka = 0
time = []
doma=[]
kk=0
time_print = []
time_print_2 = []
time_interval = 30
people = '0'        
for i in range (kol_people):
	health_people.append([i,0])


while people!='':
	proverka = 0
	time = []
	for i in range (0, 24 * 60 + time_interval,time_interval):
		time.append([i])
	time_print =[]
	people = ''
	people = input('имя человека')
	if people == '':
		break

	
	health = int(input('самочувствие'))
	for s in range (len(health_people) - 1):
		if health_people[s][2] == people:
			if health_people[s][1] > 0:
				health_people[s][1] = health
			proverka = 1
	if proverka == 0:
		health_people.append([kol_people,health,people])
	print(health_people)

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
			for i in range (len(doma)):
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


	if kol_people == 1:
		for i in range (len(time_print)):        #обновление списка людей 
	
			time_print_2.append([time_print[i][0]])
			for j in range (1,len(time_print[i])):
				time_print_2[i].append([])
				time_print_2[i][j] = [time_print[i][j][0], health_people[ time_print[i][j][1] ][0],health_people[ time_print[i][j][1] ][1]]
	else:	

		
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

	for i in range (len(time_print_2)):
		for j in range (1,len(time_print_2[i])):
			if health_people[ time_print_2[i][j][1] ][1] > 0: #симуляция заражения
				for z in range (1,len(time_print_2[i]) ):
					pass
					if time_print_2[i][j][0] == time_print_2[i][z][0]  and time_print_2[i][z][2] == 0:
						               
						#print('время',time_print_2[i][0],'дом',time_print_2[i][j][0],'человек' ,time_print_2[i][j][1],'- заражение')
						health_people[time_print_2[i][z][1]] = ([[ time_print_2[i][z][1] ][0], 1 , health_people[time_print_2[i][z][1]][2]])
						#print(health_people[time_print_2[i][z][1]])
						time_print_2[i][z][2] = health_people[time_print_2[i][z][1]][1]
	print(health_people )
	print()

	
		
	for i in range(len(time_print_2)):
			
		for j in range(1,len(time_print_2[i])):
			
			if time_print_2[i][j][2] > 0:
				for k in range (len(doma)):
					if time_print_2[i][j][0] == doma[k][0]:
						doma[k][1] += time_print_2[i][j][2]
		print(time_print_2[i])
	print()
	print(doma)
	for i in range (len(doma)):
		doma[i][1] = 0	
	
