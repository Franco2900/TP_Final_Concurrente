import time, random, os, winsound
#CUSTOMIZABLES: #^Puse OS para el momento en que decida agregar algun log file or something, lo que mas me viene a la cabeza es un settings text. That way podria editar estas settings customizables sin editar el programa, el mayor problema imo es, como debe llamarse el file, y en que parte de Windows sera ubicado.
lowestdomino=0 #Default = 0
highestdomino=6 #Default = 6
defeatscore=100
timer=0 #Editar para customizar delay entre acciones con temporizador. #Default=0.5
pauseinput=True #Editar para que en vez de hacer uso del timer, haya un input. En caso de activarlo da lo mismo que se escriba en el timer.
drawnumber=7 #Variable que se asegura de que en caso de no haber handicaps (variable de cuantosdominosforeachplayer estan en 0), se reemplace el numero por el draw correcto.
cuantosdominosforeachplayer=[0, 0] #Editar para poner handicap, dejar en 0 o menos los que no se van a usar (automaticamente se inserta el numero default, de la variable drawnumber.
playersmode=[0, 'a', 'ab'] #Cada posicion indica un jugador, si pones 0 le indicas 'jugador humano', en cambio '' indica AI easy (no strategy almost), 'a' indica 'AI con algoritmo de estrategia a', 'ab' indica 'AI con algoritmo de estrategia a y b' etc etc etc.
if 0 in playersmode: howmanygames=1 #NO CUSTOMIZABLE. Automaticamente se configura solo una partida si hay un jugador humano
else: howmanygames=100 #SI CUSTOMIZABLE. Si se pone mas de 1 se entra en debugging mode.
empatewarning=[False, True]	#El primero indica si debe haber una pausa de input, el 2do indica si debe haber un sonido de aviso.
errorwarning=[True, True]	#El primero indica si debe haber una pausa de input, el 2do indica si debe haber un sonido de aviso.
testendwarning=[True, True] #El primero indica si debe haber una pausa de input, el 2do indica si debe haber un sonido de aviso.

def turnoAI(mesa, manos, mazo, turno, start, end, mazototalvalue):
	print('-------------------------------------------------------------------------------')
	print('TURNO DEL JUGADOR {} (AI):\n'.format(turno+1))
	matchfound=[]
	while len(matchfound)==0: #Comprueba que dominos pueden ser usados de la mano, para usar una nueva variable con solamente los dominos viables, sin tener en cuenta los inusables.
		for x in range(len(manos[turno])):
			if start in manos[turno][x] or end in manos[turno][x]: matchfound.append(x)
		if len(matchfound)==0: #Si no se encontro ningun domino usable:
			if len(mazo)!=0: #Si hay al menos un domino en el pozo, se toma uno y se continua con el turno de la AI, haciendo la revision anterior de nuevo
				manos, mazo=AItakesdomino(manos, mazo, turno)
				continue
			elif len(mazo)==0: #Si no hay ningun domino en el pozo se termina el turno sin necesidad de pasar por la fase de estrategias etc.
				AIfinalizaturno(turno, False, mesa)
				return(mesa, manos, mazo)
	#IDEA!: que las estrategias puedan ser por ej a80%b50%c45% y tenga esa chance de usar cada estrategia, creando un playersmode auxiliar, si el random da negativo se elimina la letra del auxiliar y el porcentaje indicado tambien, pero si da positivo solo se eliminar el porcentaje, una vez se paso por todo este proceso empieza la funcion.
	if 'c' in playersmode[turno]: #COMPROBADO que funciona con domino doble, pendiente testear some more, con other dominoes
		mesavalue=0
		manovalue=0
		for x in range(len(mesa)): mesavalue+=mesa[x][0]+mesa[x][1]
		for x in range(len(manos[turno])): manovalue+=manos[turno][x][0]+manos[turno][x][1]
		manoenemigaydominosrestantes=mazototalvalue-mesavalue-manovalue
		cuentadedominonumbers=[]
		checkmatesposibles=[]
		for x in range(highestdomino+1-lowestdomino): cuentadedominonumbers.append(0)
		for x in range(len(mesa)):
			cuentadedominonumbers[mesa[x][0]]+=1
			cuentadedominonumbers[mesa[x][1]]+=1
		for x in range(len(cuentadedominonumbers)):
			if cuentadedominonumbers[x]==highestdomino-lowestdomino:
				checkmatesposibles.append(x+lowestdomino)
		for x in range(len(matchfound)):
			if manos[turno][matchfound[x]][0] in checkmatesposibles and manos[turno][matchfound[x]][1] in checkmatesposibles:
				if start in manos[turno][matchfound[x]] and end in manos[turno][matchfound[x]]:
					asd=manos[turno].pop(matchfound[x])
					if asd[0]!=end: asd=(asd[1], asd[0])
					mesa.append(asd)
					AIfinalizaturno(turno, asd, mesa)
					#print('CHECKMATE') #DEBUG
					#input('Presione enter para continuar: ') #DEBUG
					return(mesa, manos, mazo)
	if 'b' in playersmode[turno]:
		mesa, manos, doblefound=prioridad_a_DOBLE_DOBLE(mesa, manos, start, end, turno)
		if doblefound:
			return(mesa, manos, mazo)
	if 'a' in playersmode[turno]: #Saca el dominó de valor mas alto que tenga para poner en la mesa.
		valortotal=-1
		for x in range(len(matchfound)):
			if manos[turno][matchfound[x]][0]+manos[turno][matchfound[x]][1]>valortotal:
				dominochoice=matchfound[x]
				valortotal=manos[turno][matchfound[x]][0]+manos[turno][matchfound[x]][1]
		asd=manos[turno].pop(dominochoice)
	else: #Si domino mas alto no esta activado, tirara un domino random, el primero que tenga a la izquierda de su mano. Basically almost random.
		asd=manos[turno].pop(matchfound[0])
	if asd[0]==end: mesa.append(asd) #Colocar dominó al final
	elif asd[1]==end: #Dar vuelta dominó y colocarlo al final
		asd=(asd[1], asd[0])
		mesa.append(asd)
	elif asd[0]==start: #Dar vuelta dominó y colocarlo al comienzo
		asd=(asd[1], asd[0])
		mesa.insert(0, asd)
	elif asd[1]==start: mesa.insert(0, asd) #Colocar dominó al comienzo
	AIfinalizaturno(turno, asd, mesa)
	return(mesa, manos, mazo)

def turnoplayer(mesa, mazo, manos, puntaje, enemyhandcheat, memory, start, end, turno):
	print('-------------------------------------------------------------------------------')
	print('TURNO DEL JUGADOR {}:\n'.format(turno+1))
	while True:  #Either podria agregar una seleccion que al hacerla te actualice la informacion, y asi hacer uso de este while True:, o borrar esta linea y todos los espacios que le puse a los codigos siguientes
		print('DOMINÓS RESTANTES:', len(mazo))
		if enemyhandcheat or (memory and len(mazo)==0 and players == 2): cheater(manos, turno)
		elif memory and len(mazo)==0: memorymultiplayer(manos, turno)
		else:
			print('DOMINÓS DE OTROS JUGADORES:', end='')
			for x in range(players):
				if x!=turno: print(" Jugador {}: {}.".format(x+1, len(manos[x])), end='')
		print('\nTU MANO (use el número a la derecha para seleccionarlo):')
		for x in range(len(manos[turno])): print(manos[turno][x], ' ', x+1)
		print('Por favor elija que dominó usar con el número que le corresponde.')
		print('Use -1 para mostrar el historial de puntajes y 0 para tomar un dominó más o pasar si no hay más dominós: ', end= '')
		while True:
			while True:
				choice=input()
				if len(choice)==0 or choice=='-': pass
				elif choice=='Quit' or choice=='quit': quit()
				elif choice[0]!='-' and not choice[0].isdigit(): pass
				else:
					if len(choice)>1:
						if not choice[1:].isdigit(): pass
						else: break
					else: break
			choice=int(choice)
			if choice==0:
				if len(mazo)>0:
					asd=mazo.pop()
					manos[turno].append(asd)
					print('Tu nuevo dominó es {} y se usa con el número {}.'.format(asd, len(manos[turno])))
					if len(mazo)==0:
						if memory and not enemyhandcheat:
							if players>2: memorymultiplayer(manos, turno)
							else: cheater(manos, turno)
						advertencia=input('Advertencia! No quedan más dominos. Presione enter para continuar: ')
						while advertencia!='': advertencia=input('Advertencia! No quedan más dominos. Presione enter para continuar: ')
				elif len(mazo)==0:
					print('No quedan más dominós. Tendrá que pasar el turno.')
					return(mesa, manos, mazo, False, enemyhandcheat, memory)
			elif choice==1994: cheater(manos, turno)
			elif choice==20031994:
				enemyhandcheat=not enemyhandcheat
				if not enemyhandcheat: print("Truco de mano enemiga desactivado.")
				elif enemyhandcheat:
					print("Truco de mano/s enemiga/s activado.")
					cheater(manos, turno)
			elif choice==333081:
				memory=not memory
				if not memory: print("Truco de memoria desactivado.")
				elif enemyhandcheat: print("Truco de memoria activado. Pero de que sirve si ya tenés truco de mano enemiga...")
				elif memory:
					print("Truco de memoria activado.")
					if len(mazo)==0 and players==2: cheater(manos, turno)
					elif len(mazo)==0 and players>2: memorymultiplayer(manos, turno)
			elif choice==-1:
				if len(puntaje)>1: mostrarpuntaje(puntaje)
				elif len(puntaje)==1: print('Recién empezó el juego... no hay historial aún.') #0, 0 es un dato inecesario, y solamente existe para evitar crash cuando la AI verifica poder hacer checkmate en ronda 1
			elif choice<0 or choice>len(manos[turno]): print('Cometió un error. Intentelo de nuevo.')
			else: #Si se introdujo un domino de tu mano
				if manos[turno][choice-1][0] != start and manos[turno][choice-1][1] != start and manos[turno][choice-1][0] != end and manos[turno][choice-1][1] != end: print('El dominó no encaja.')
				else:
					if start==end:
						asd=manos[turno].pop(choice-1)
						if end!=asd[0]: asd=(asd[1], asd[0]) #Domino flip
						mesa.append(asd)
					elif start in manos[turno][choice-1] and end not in manos[turno][choice-1]:
						asd=manos[turno].pop(choice-1)
						if start!=asd[1]: asd=(asd[1], asd[0]) #Domino flip
						mesa.insert(0, asd)
					elif end in manos[turno][choice-1] and start not in manos[turno][choice-1]:
						asd=manos[turno].pop(choice-1)
						if end!=asd[0]: asd=(asd[1], asd[0]) #Domino flip
						mesa.append(asd)
					elif start in manos[turno][choice-1] and end in manos[turno][choice-1]:
						if len(manos[turno])==1: ladodeconexion=end #Si es el ultimo domino da lo mismo de que lado se pone, por lo tanto se hace automaticamente
						else:
							ladodeconexion='while activator'
							while not ladodeconexion.isdigit(): ladodeconexion=input('Su dominó tiene 2 números distintos y de ambos lados puede ser colocado, cual desea conectar?: ')
							ladodeconexion=int(ladodeconexion)
						if ladodeconexion==manos[turno][choice-1][1]:
							asd=manos[turno].pop(choice-1)
							if end==ladodeconexion:
								asd=(asd[1], asd[0]) #Domino flip
								mesa.append(asd)
							elif start==ladodeconexion: mesa.insert(0, asd)
						elif ladodeconexion==manos[turno][choice-1][0]:
							asd=manos[turno].pop(choice-1)
							if end==ladodeconexion: mesa.append(asd)
							elif start==ladodeconexion:
								asd=(asd[1], asd[0]) #Domino flip
								mesa.insert(0, asd)
						else:
							print('Dato incorrecto, vuelva a intentarlo de cero.')
							continue
					return(mesa, manos, mazo, True, enemyhandcheat, memory)

def dominoagainstAI():
	"""Ejecuta el juego, y es el encargado de decidir de quien es el turno etc (cada turno es una definicion distinta)"""
	print('Bienvenido a dominó contra computadora.')
	for x in range(players): print('El jugador {} toma {} dominós'.format(x+1, cuantosdominosforeachplayer[x]))
	print('-------------------------------------------------------------------------------')
	print('GAME START: ')
	print('')
	puntaje=[[]]
	for x in range(players): #Asigna un puntaje inicial (0) por cada jugador.
		puntaje[0].append(0) #Parece un dato inecesario pero NO CAMBIARLO, es importante que diga [[0, 0]] al comienzo para que no crashee si la AI hard encuentra un checkmate en la primer ronda.
	#FOR SOME REASON COPYPASTEARLO AFUERA DE CUALQUIER FUNCION NO HACE QUE MAZO SEA GLOBAL, thus causing a crash V
	mazo=[] #Creación del mazo, mazobackup, y mazototalvalue
	empates=0
	lowestdominotemporal=lowestdomino
	mazototalvalue=0
	for asd in range(lowestdominotemporal, highestdomino+1):
		for asd in range(lowestdominotemporal, highestdomino+1):
			mazo.append((asd, lowestdominotemporal))
			mazototalvalue+=asd+lowestdominotemporal #Igual cambiandolo de 168 a metiendolo a loop, solamente paso de 1 linea para programarlo, a 2, asi que meh.
		lowestdominotemporal+=1
	mazobackup=tuple(mazo) #Fin de la creación del mazo, mazobackup, y mazototalvalue
	#FOR SOME REASON COPYPASTEARLO AFUERA DE CUALQUIER FUNCION NO HACE QUE MAZO SEA GLOBAL, thus causing a crash ^
	enemyhandcheat=False
	memory=False
	while True:
		random.shuffle(mazo)
		manos=[]
		for x in range(players): manos.append([])
		mesa=[]
		for x in range(players):
			if playersmode[x]!=-1:
				for y in range(cuantosdominosforeachplayer[x]):
					asd=mazo.pop()
					manos[x].append(asd)
			elif playersmode[x]==-1: manos[x].append("No")
		x=highestdomino
		doblenotification = True
		while mesa==[]:
			for y in range(players):
				if (x, x) in manos[y]:
					turno=y
					print('El jugador', y+1, 'tiene el dominó doble más alto.')
					manos[y].remove((x, x))
					mesa.append((x, x))
			if mesa==[]:
				if doblenotification: print('Ninguno de los jugadores tiene el domino ({},{})'.format(x, x))
				x-=1
				if x<lowestdomino:
					doblenotification = False #Podria poner if doblenotificacion: doblenotificacion = False pero no se cual forma seria mas eficiente
					print('Como ninguno de los jugadores tiene un dominó doble, cada uno tomará uno más. ', end = 'Presione enter para continuar: ')
					pause()
					x=highestdomino
					asd=[]
					for y in range(players):
						if playersmode[y]!=-1: manos[y].append(mazo.pop())
		print('Mesa=', mesa)
		pause()
		roundongoing=True
		while roundongoing:
			turno+=1
			if turno>players-1: turno=0
			mesadebugger(mesa)
			start=mesa[0][0]
			end=mesa[len(mesa)-1][1]
			lockdown='Checkmate'
			for x in range(len(mazo)): #Comprobar que no se haya hecho checkmate
				if start in mazo[x] or end in mazo[x]: lockdown='No checkmate'
			for x in range(players): #Comprobar que no se haya hecho checkmate
				for y in range(len(manos[x])):
					if start in manos[x][y] or end in manos[x][y]: lockdown='No checkmate' #Poner y-1 no resolvio el crash :/ #14/10/2019: sospecho que el crash mencionado ya fue arreglado, investigar
			roundfinishflag=False
			if playersmode[turno]==0 and lockdown=='No checkmate':
				mesa, manos, mazo, returnmesa, enemyhandcheat, memory=turnoplayer(mesa, mazo, manos, puntaje, enemyhandcheat, memory, start, end, turno)
				if returnmesa: print('Dominó agregado, mesa:', mesa)
			elif playersmode[turno]!=0 and lockdown=='No checkmate': mesa, manos, mazo=turnoAI(mesa, manos, mazo, turno, start, end, mazototalvalue)			
			if len(manos[turno])==0: roundongoing=False
			elif lockdown=='Checkmate': roundongoing=False
		mesadebugger(mesa)
		if len(manos[turno])==0: print('\nEl jugador', turno+1, 'se quedó sin dominós y ganó la ronda.')
		elif lockdown=='Checkmate':
			print('\nJAQUE MATE.')
			if turno+1==players:
				while len(mazo)!=0: manos[0].append(mazo.pop())
			else:
				while len(mazo)!=0: manos[turno+1].append(mazo.pop())
		puntaje.append([])
		for x in range(players):
			handscore=0
			if x==turno and len(manos[turno])==0: puntaje[len(puntaje)-1].append(puntaje[len(puntaje)-2][turno])
			else:
				for y in range(len(manos[x])):
					handscore+=manos[x][y][0]+manos[x][y][1]
				print("La mano del jugador {} ({}) vale {} y ahora tiene en total {}.".format(x+1, manos[x], handscore, handscore+puntaje[len(puntaje)-2][x]))
				puntaje[len(puntaje)-1].append(puntaje[len(puntaje)-2][x]+handscore)
		puntaje[len(puntaje)-1].append(lockdown)
		puntaje[len(puntaje)-1].append(turno)
		lost=0
		winner=[999999, 0]
		for x in range(players): #ERROR: No tiene en consideracion que pasa en caso de empate.
			if puntaje[len(puntaje)-1][x]>=defeatscore: lost+=1
		if lost>=players-1:
			for x in range(players):
				if puntaje[len(puntaje)-1][x]<winner[0]: winner=[puntaje[len(puntaje)-1][x], x]
			print("EL JUGADOR {} GANÓ DEFINITIVAMENTE!".format(winner[1]+1))
			victorias[winner[1]]+=1
			mostrarpuntaje(puntaje)
			return [empates, victorias]
		mazo=list(mazobackup)
		if howmanygames==1: input('\nPresione enter para empezar la siguiente ronda: ')
		elif howmanygames>1: print('\nEmpieza la siguiente ronda: ')
		print('-------------------------------------------------------------------------------')
		print('SIGUIENTE RONDA:\n')
		"""if playerscore>=defeatscore and playerscore==AIscore: #PENDIENTE BORRAR/EDITAR
			print('AMBOS JUGADORES TIENEN {} PUNTOS! El juego continua hasta que uno de ambos jugadores tenga mas puntos y pierda.'.format(playerscore))
			if empatewarning[1]: winsound.Beep(500, 300)
			if empatewarning[0]: input('Presione enter para continuar: ')
			empates+=1"""

def cheater(manos, turno):
	if players == 2:
		print("\nAquí esta la mano del oponente:")
		for x in range(len(manos)):
			if x!=turno: print(manos[x])
	else:
		print("\nAquí esta la mano de los demas jugadores:")
		for x in range(len(manos)):
			if x!=turno: print('Jugador {}:'.format(x+1), manos[x])

def memorymultiplayer(manos, turno):
	print("\nEstos son los dominos posibles que pueden tener los oponentes:")
	dominosposibles=[]
	for x in range(players):
		if x!=turno:
			for y in range(len(manos[x])):
				dominosposibles.append(manos[x][y])
	random.shuffle(dominosposibles)
	print(dominosposibles)

def AIfinalizaturno(turno, asd, mesa):
	if asd==mesa[len(mesa)-1]:
		print('La AI (jugador {}) agregó el dominó {} al final de la mesa:\n'.format(turno+1, asd), end = "{}\n".format(mesa))
	elif asd==mesa[0]:
		print('La AI (jugador {}) agregó el dominó {} al comienzo de la mesa:\n'.format(turno+1, asd), end = "{}\n".format(mesa))
	elif not asd: print('La AI (jugador {}) pasa su turno por no haber dominós restantes.'.format(turno+1))
	pause()

def AItakesdomino(manos, mazo, turno):
	manos[turno].append(mazo.pop())
	print('El jugador', turno+1, 'tomó un dominó de los restantes.')
	pause()
	return(manos, mazo)

def mostrarpuntaje(puntaje):
	for x in range(players):
		if playersmode[x]==0: print('Jugador {}'.format(x+1), end='')
		elif playersmode[x]==-1: pass
		else: print('Jugador {} (AI)'.format(x+1), end='')
		if x+1!=players: print(', ', end='')
	print()
	for x in range(1, len(puntaje)): #Dice 1 en vez de 0 para ignorar el dato inutil del puntaje que es 0 for each player.
		for y in range(players):
			print("{}".format(puntaje[x][y]), end='')
			if playersmode[y]==0:
				for z in range(11-len(str(puntaje[x][y]))): print(end=' ') #Calcula cuantos espacios dejar para que la tabla de puntajes se vea bien
			elif playersmode[y]==-1: pass
			else:
				for z in range(16-len(str(puntaje[x][y]))): print(end=' ')
		if 'Checkmate' in puntaje[x]:
			if puntaje[x][-1]==0: print('(Jaque mate causado por el jugador {})'.format(players))
			else: print('(Jaque mate causado por el jugador {})'.format(puntaje[x][-1])) 
		else: print('(Victoria del jugador {})'.format(puntaje[x][-1]+1))

def mesadebugger(mesa):
	for x in range(len(mesa)-1): #-1 para evitar que crashee en la comprobación
		if len(mesa)>1: #Para evitar que crashee con la comprobación (linea abajo de esta)
			if mesa[x][1]!=mesa[x+1][0]: #Comprueba que no haya 2 dominós conectados cuando tienen número incompatible.
				print("Error: Se encontró 2 dominós conectados en la mesa incorrectamente: {} {}".format(mesa[x], mesa[x+1]))
				errorenlamesa(mesa)
		asd=0
		for y in range(len(mesa)): #Comprueba que no este repetido el dominó
			if mesa[x]==mesa[y]: asd+=1
			if asd>1:
				print('Error: Se encontró un dominó duplicado: {} {}'.format(mesa[x], mesa[y]))
				errorenlamesa(mesa)
		if (mesa[x][1], mesa[x][0]) in mesa and (mesa[x][1], mesa[x][0])!=(mesa[x][0], mesa[x][1]): #Comprueba que no este repetido el dominó, pero dado vuelta. La 2da condición evita que tire error por (6, 6) por ejemplo.
			print('Error: Se encontró un dominó duplicado (invertido): {} {}'.format(mesa[x], (mesa[x][1], mesa[x][0])))
			errorenlamesa(mesa)

def errorenlamesa(mesa):
	print("Mesa: {}".format(mesa))
	raise Exception

def prioridad_a_DOBLE_DOBLE(mesa, manos, start, end, turno):
	"""Intenta sacarse de encima dominós dobles, con más prioridad a los de valor alto"""
	dobles=[]
	for x in range(len(manos[turno])):
		if manos[turno][x][0]==manos[turno][x][1] and (start in manos[turno][x] or end in manos[turno][x]): dobles.append((x, manos[turno][x][0]))
	if dobles==[]: return(mesa, manos, False)
	elif len(dobles)==1: dobles=dobles[0][0]
	elif len(dobles)==2:
		if dobles[0][1]>dobles[1][1]: dobles=dobles[0][0]
		elif dobles[1][1]>dobles[0][1]: dobles=dobles[1][0]
	dobles_print=manos[turno][dobles]
	if start in manos[turno][dobles]: mesa.insert(0, manos[turno].pop(dobles))
	elif end in manos[turno][dobles]: mesa.append(manos[turno].pop(dobles))
	AIfinalizaturno(turno, dobles_print, mesa)
	return(mesa, manos, True)

def error(errores):
	if errorwarning[1]: winsound.Beep(1000, 300)
	if errorwarning[0]: input("Presione enter para continuar: ")
	return(errores+1)

def pause():
	if pauseinput: input()
	else: time.sleep(timer)

def test(): #Preparativos para comenzar el juego. La mayor utilidad de esta funcion viene de correr tests, caso contrario no hay razon de que este dentro de una funcion
	errores=0
	empates=0
	players=0
	for x in range(len(playersmode)): #Cuenta cuantos jugadores hay (AI incluido), y en caso de haber jugador deshabilitado, se asegura de cambiar cuantos dominos debe tomar ese jugador a -1, en caso de olvidar editar esa variable.
		if playersmode[x]!=-1: players+=1
		else: cuantosdominosforeachplayer[x]=-1
	while players>len(cuantosdominosforeachplayer):
		cuantosdominosforeachplayer.append(0) #Agrega 0's a la lista de handicap (default domino number) si por ej: dice 4 jugadores, pero en cuantosdominosforeachplayer hay solo 2 numeros.
	for x in range(len(cuantosdominosforeachplayer)): #Si un jugador esta asignado a tomar menos de 1 domino, toma la cantidad default instead.
		if cuantosdominosforeachplayer[x]<=0: cuantosdominosforeachplayer[x]=drawnumber
	victorias=[]
	for x in range(players): victorias.append(0)
	for x in range(howmanygames):
		try:
			auxiliar=dominoagainstAI()
			empates+=auxiliar[0]
			victorias=auxiliar[1]
		except Exception as e:
			print("Un error ha ocurrido:", type(e), e)
			errores=error(errores)
		finally:
			if howmanygames>1 and x!=howmanygames-1: print("Comienzo de nueva partida: ")
	if howmanygames > 1:
		if errores==1: errorsingularoplural=["ó", ""]
		else: errorsingularoplural=["aron", "es"]
		if empates==1: empatesingularoplural=""
		else: empatesingularoplural="s"
		if victorias[0]==1: victoriassingularoplural="z"
		else: victoriassingularoplural="ces"
		print("Se encontr{} {} error{}.".format(errorsingularoplural[0], errores, errorsingularoplural[1], )) #IMPORTANTE: Son partidas lo que se cuenta, no rondas.
		print("Hubo en total {} empate{}.".format(empates, empatesingularoplural))
		for x in range(players):
			print("El jugador {} ganó {} ve{}.".format(x+1, victorias[x], victoriassingularoplural))
		if testendwarning[1]: winsound.Beep(500, 500)
		if testendwarning[0]: input("Presione enter para continuar: ")

def playerscount():
	players = 0
	for player in range(len(playersmode)-1, -1, -1): #Si por ej hay 5 numeros en la lista recorre del 5to al 1ro, o sea de posicion 4 a 0, en ese orden
		if type(playersmode[player])==str: players += 1
		elif type(playersmode[player])==int:	
			if playersmode[player] == 0: players += 1
			else: playersmode.pop(player) #Elimina parametros erroneos de la lista
		else: error(errores)
	return players

#NO CUSTOMIZABLES:
victorias=[]
players = playerscount()
for player in range(players): victorias.append(0)
test()

input('\nPresione enter para terminar el programa: ') #Aviso previo a finalizacion del programa, se usa tanto para debugmode como para partidas normales