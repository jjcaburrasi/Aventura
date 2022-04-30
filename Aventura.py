inventario=[]
traje=False
chandal=False
ducha=False
oporatsistemas=True
oporjardinero=True
oporserviciotecnico=False
dia=1
dinero=0
hora="6:00"
def linkedin():
	global oporserviciotecnico
	print("Estas en Linkedin, entre unas cuantas publicaciones de vendehumos, ves una publicacion de Jose Miguel Garcia Muñiz")
	print("Este hombre siempre es sinonimo de calidad")
	print("Puedes MIRAR OFERTAS, MIRAR MENSAJES o SALIR")
	respuesta = input (">")
	while respuesta != ("SALIR")
		if respuesta == ("MIRAR OFERTAS"):
			print("Hay una oferta de helpdesk")
			print("¿Quieres aplicar a la oferta?")
			respuesta=("SI/NO>")
				if respuesta == ("SI")
					print("Mandas el CV, has hecho esto tantas veces que ya ni te ilusiona")
				elif respuesta ==("NO")
					oporserviciotecnico=True
				else:
					print("No te entiendo")
		elif respuesta == ("MIRAR MENSAJES"):
			if dia==(1)
				print("No tienes mensajes nuevos")
			elif dia == (2) and oporserviciotecnico == True:
				print("Te han contactado de la oferta de helpdesk, te piden que llames al numero 600-195-596")
		else:
			print("No te entiendo")
	ordenador()
def atsistemas():
	pass
def procastinar():
	global hora
	print("Te pones a jugar al buscaminas.")
	print("¿Hasta que hora quieres jugar?")
	print("Las horas deben ser en punto y entre 00:00 y 23:00")
	respuesta = input(">")
	if respuesta > ("23:00") or respuesta < ("00:00"):
		print("Hora incorrecta")
	else:
		hora = respuesta
		print("Ahora son las " + hora)

def movil():
	print("Puedes mirar la AGENDA, LLAMAR o SALIR")
def skype():
	global oporatsistemas
	global hora
	global dia
	global ducha
	print("Estas en Skype.")
	print("Escribe SALIR para volver a la seleccion de programa")
	if hora != ("10:00") or dia != (1) or oporatsistemas==False:
		print ("Abres el programa, no tienes ningun contacto, hace tiempo que te pasaste a Discord, pero algunas empresas aun prefieren hacer las entrevistas por Skype")
		respuesta=input("¿Que quieres hacer ahora, SALIR o CONTINUAR EN SKYPE?>")	
		if respuesta ==("SALIR"):
			ordenador()
		elif respuesta== ("CONTINUAR EN SKYPE"):
			skype()
		else:
			print("No te entiendo")
	elif hora ==("10:00") and dia ==(1) and oporatsistemas==True:
		print ("Tienes una llamada entrante, es Elena Cantero, responsable de seleccion de Atsistemas")
		print ("¿Quieres responder?")
		respuesta=input("SI/NO>")
		if respuesta == ("SI"):
			atsistemas()
		elif respuesta == ("NO"):
			print("Pierdes la oportunidad de trabajar en Atsistemas")
			oporatsistemas=False
			respuesta=input("¿Que quieres hacer ahora, SALIR o CONTINUAR EN SKYPE?>")	
			if respuesta ==("SALIR"):
				ordenador()
			elif respuesta== ("CONTINUAR EN SKYPE"):
				skype()
			else:
				print("No te entiendo")
		else:
			print("No te entiendo")
			respuesta=input("¿Que quieres hacer ahora, SALIR o CONTINUAR EN SKYPE?>")	
			if respuesta ==("SALIR"):
				ordenador()
			elif respuesta== ("CONTINUAR EN SKYPE"):
				skype()
			else:
				print("No te entiendo")	
def ordenador():
	
	print("Te sientas delante del ordenador y te crujes los dedos, has visto en muchas peliculas que eso ayuda a usarlo")
	print("Puedes abrir SKYPE, LINKEDIN o GMAIL, tambien puedes SALIR")
	respuesta=input(">")
	while respuesta != ("SALIR"):
		if respuesta==("ABRIR SKYPE"):
			skype()
		elif respuesta==("ABRIR LINKEDIN"):
			linkedin()
		elif respuesta==("ABRIR GMAIL"):
			
		elif respuesta==("INVENTARIO"):
			inv()
		elif respuesta==("ESTADO"):
			estado()
		elif respuesta==("PROCASTINAR"):
			procastinar()
		elif respuesta==("DESCRIPCION"):
			print("Te sientas delante del ordenador y te crujes los dedos, has visto en muchas peliculas que eso ayuda a usarlo")
			print("Puedes abrir SKYPE, LINKEDIN o FACEBOOK, tambien puedes SALIR")
		else:
			print("No te entiendo")	
		respuesta=input(">")
	oficina()
def estado():
	print("Estas en el día " + str(dia))
	print("Son las "+ hora)
	print("Tienes " + str(dinero) + " euros")
	if ducha==False:
		print("No estas duchado")
	else:
		print("Estás duchado.") 
	if traje==False and chandal==False:
		print("Estas desnudo")
	elif traje==True:
		print("Llevas puesto el traje")
	else:
		print("Llevas puesto el chandal")
def instrucciones():
	print("LA BUSQUEDA")
	print("===========")
	print("Tu nombre es Paco Delcán, llevas en paro 1 año, y ya la situación es insostenible")
	print("Tienes tres dias para encontrar trabajo antes de que pierdas la cabeza")
	print("ESTO ES UNA DEMO, UNA MUESTRA DEL JUEGO, EN ESTA DEMO PODRÁS ENCONTRAR 3 TRABAJOS DIFERENTES")
	print("")
	print("CÓMO JUGAR")
	print("==========")
	print("Para avanzar, tendrás que indicar las acciones que deseas realizar")
	print("Los objetos con los que podras interactuar se mostrarán en MAYUSCULAS")
	print("Los verbos se escribiran en infinitivo y SIEMPRE EN MAYÚSCULAS")
	print("En cualquier momento podrás consultar tu INVENTARIO y tu ESTADO, escribiendo 'INVENTARIO' y 'ESTADO'")
	print("Tambien podrás en cualquier momento PROCASTINAR, para que pasen las horas")
	print("O podras dormir en la cama para hacer que pase un dia")
	print("")
	print("Espero que disfrutes de la aventura, al igual que yo he disfrutado haciéndola")
def oficina():
	print("Aqui es donde pasas la mayor parte del tiempo")
	print("Hay una MESA con un ORDENADOR, puedes ir al PASILLO")
	respuesta=input(">")
	while respuesta != ("IR A PASILLO"):
		if respuesta==("MIRAR MESA"):
			print("Es una mesa de oficina, al lado de la pantalla hay una AGENDA")
		elif respuesta==("MIRAR AGENDA"):
			print("Para el dia de hoy tienes apuntado, 'Entrevista de trabajo por Skype a las 10:00'")	
		elif respuesta==("COGER AGENDA"):
			print("Prefiero dejarla aqui, que si no, la pierdo")
		elif respuesta==("MIRAR ORDENADOR"):
			print("Es mi ordenador")
		elif respuesta==("USAR ORDENADOR"):
			ordenador()
		elif respuesta==("ESTADO"):
			estado()
		elif respuesta==("INVENTARIO"):
			inv()
		elif respuesta==("PROCASTINAR"):
			procastinar()
		elif respuesta==("DESCRIPCION"):
			print("Aqui es donde pasas la mayor parte del tiempo")
			print("Hay una MESA con un ORDENADOR, puedes ir al PASILLO")
		else:
			print("No te entiendo")	
		respuesta=input(">")
def baño():
	global ducha
	print("Estas en el cuarto de baño, y bueno, aqui pasas el tiempo que no estas en la oficina")
	print("Hay una DUCHA, puedes ir al PASILLO")
	respuesta=input(">")
	while respuesta != ("IR A PASILLO"):
		if respuesta==("MIRAR DUCHA"):
			print("¿Que quieres ver?, es una ducha")
		elif respuesta==("USAR DUCHA"):
			print("Ya te hacia falta!!")
			ducha=True
		elif respuesta==("INVENTARIO"):
			inv()
		elif respuesta==("ESTADO"):
			estado()
		elif respuesta==("PROCASTINAR"):
			procastinar()
		elif respuesta==("DESCRIPCION"):
			print("Estas en el cuarto de baño, y bueno, aqui pasas el tiempo que no estas en la oficina")
			print("Hay una DUCHA, puedes ir al PASILLO")
		else:
			print("No te entiendo")	
		respuesta=input(">")
def pasillo():
	global dinero
	print("Hay varios cuadros colgados, un MUEBLE en la entrada, y el PORTON de salida, puedes ir al BAÑO, a la OFICINA o al SALON")
	respuesta=input(">")
	while respuesta != ("IR A SALON"):
		if respuesta==("MIRAR MUEBLE"):
			print("Es el típico mueble de entrada, sobre ella hay una CARTERA")
		elif respuesta==("COGER CARTERA"):
			if ("BONOBUS") in inventario:
				print("Ya la tienes")
			else:
				print("Coges la cartera, la abres y tiene un BONOBUS, una TARJETA BANCARIA, un PAPEL y 3,50€")
				print("Se añaden el BONOBUS, la TARJETA BANCARIA y el PAPEL a tu INVENTARIO")
			dinero+= 3.50
			inventario.append("BONOBUS")
			inventario.append("TARJETA BANCARIA")
			inventario.append("PAPEL")
		elif respuesta==("MIRAR CARTERA"):
			print("Es una cartera de piel negra")
		elif respuesta==("IR A BAÑO"):
			baño()
		elif respuesta==("IR A OFICINA"):
			oficina()
		elif respuesta==("ABRIR PORTON"):
			print("Esto es una demo, por ahora sólo vamos a centrarnos en la casa, ya habrá tiempo de salir y explorar")
		elif respuesta==("ESTADO"):
			estado()
		elif respuesta==("INVENTARIO"):
			inv()
		elif respuesta==("PROCASTINAR"):
			procastinar()
		elif respuesta==("DESCRIPCION"):
			print("Es una cocina estilo moderno, te encantaria tener una isla central, pero el espacio es limitado")
			print("Hay una NEVERA, puedes ir al SALON")
		else:
			print("No te entiendo")	
		respuesta=input(">")
	salon()
def cocina():
	print("Es una cocina estilo moderno, te encantaria tener una isla central, pero el espacio es limitado")
	print("Hay una NEVERA, puedes ir al SALON")
	respuesta=input(">")
	while respuesta != ("IR A SALON"):
		if respuesta==("MIRAR NEVERA"):
			print("Es una NEVERA plateada, la compraste de 2 metros de alto pero te sobra mas de la mitad")
		elif respuesta==("ABRIR NEVERA"):
			print("Tienes medio limón fosilizado, un tupper con macarrones con tomate y una botella de AGUA")
		elif respuesta==("BEBER AGUA") or respuesta==("USAR AGUA") or respuesta==("COGER AGUA"):
			print("Bebes AGUA, esta muy fría")
		elif respuesta==("IR A COCINA"):
			cocina()
		elif respuesta==("INVENTARIO"):
			inv()
		elif respuesta==("ESTADO"):
			estado()
		elif respuesta==("PROCASTINAR"):
			procastinar()
		elif respuesta==("DESCRIPCION"):
			print("Es una cocina estilo moderno, te encantaria tener una isla central, pero el espacio es limitado")
			print("Hay una NEVERA, puedes ir al SALON")
		else:
			print("No te entiendo")	
		respuesta=input(">")
	salon()
def salon():
	print("Sales al salón, esta todo desordenado")
	print("En una esquina hay un extraño ARTILUGIO, puedes ir a la COCINA, al PASILLO O al DORMITORIO")
	respuesta=input(">")
	while respuesta != ("IR A PASILLO"):
		if respuesta==("MIRAR ARTILUGIO"):
			print("Lo compré en mi ultimo viaje a Tailandia, el que me lo vendió decía que vale para teletransportarse")
		elif respuesta==("USAR ARTILUGIO"):
			print("Al tocarlo, se enciende y despide una luz brillante y un ruido ensordecedor, los vecinos estaran contentos")
		elif respuesta==("COGER ARTILUGIO"):
			print("Pesa demasiado")
		elif respuesta==("IR A COCINA"):
			cocina()
		elif respuesta==("IR A DORMITORIO"):
			dormitorio()
		elif respuesta==("INVENTARIO"):
			inv()
		elif respuesta==("ESTADO"):
			estado()
		elif respuesta==("PROCASTINAR"):
			procastinar()
		elif respuesta==("DESCRIPCION"):
			print("Sales al salón, esta todo desordenado")
			print("En una esquina hay un extraño ARTILUGIO, puedes ir a la COCINA o al PASILLO")
		else:
			print("No te entiendo")	
		respuesta=input(">")
	pasillo()
def inv():
	print("Actualmente tienes en tu inventario:")
	print('\n'.join(map(str, inventario)))
	print("Puedes MIRAR los objetos que tienes, o bien SALIR del inventario")
	respuesta=input(">")
	while respuesta!=("SALIR"):
		if respuesta==("MIRAR INSTRUCCIONES"):
			instrucciones()
		elif respuesta==("MIRAR PAPEL"):
			print("Solamente hay escrito un numero: 0212")
		elif respuesta==("MIRAR BONOBUS"):
			print("Te permite usar los autobuses de línea")
		elif respuesta==("MIRAR TARJETA BANCARIA"):
			print("Es una tarjeta de débito")
		elif respuesta==("MIRAR MOVIL") or respuesta==("USAR MOVIL"):
			movil()
		else:
			print("No te entiendo")
			print("Puedes MIRAR los objetos que tienes, o bien SALIR del inventario")
		respuesta=input(">")
	print("Has salido del INVENTARIO")
def dormitorio():
	global traje
	global chandal
	global dia
	print ("Estrellas el despertador contra la pared, sacas otro de debajo de la cama y lo pones en hora")
	print ("Estás en tu habitación, hay una MESITA de noche, un ESPEJO, un ARMARIO, una CAMA, y una puerta hacia el SALON ")
	respuesta=input(">")
	while respuesta != ("IR A SALON"):
		if respuesta==("ABRIR MESITA"):
			print("Hay una caja de CASETTE vacia, recuerdo en mi infancia que los juegos de MSX venian en este formato")
		elif respuesta==("MIRAR MESITA"):
			print("Es la tipica mesita de noche, tienes el MOVIL encima")
		elif respuesta==("MIRAR MOVIL"):
			print("Es un Xiaomi, lo compraste hace poco, pero ya tiene la pantalla rota, eres un desastre")
		elif respuesta==("COGER MOVIL"):
			if ("MOVIL") in inventario:
				print("Ya lo tienes")
			else:
				print("Coges tu MOVIL, ahora lo encontraras en el INVENTARIO")
				inventario.append("MOVIL")
			
		elif respuesta==("MIRAR CASETTE"):
			print("En la portada hay una ilustracion muy bonita, sobre esta, resalta el nombre del juego, 'La Busqueda' ")
		elif respuesta==("ABRIR CASETTE"):
			if ("INSTRUCCIONES") in inventario:
				print("Ya lo tienes")
			else:
				print("Abres el casette y esta vacio, a saber donde está la cinta")
				print("te quedas con las INSTRUCCIONES, ahora estan en el INVENTARIO")
				inventario.append("INSTRUCCIONES")		
		elif respuesta==("COGER CASETTE"): 
			if ("INSTRUCCIONES") in inventario:
				print("Ya lo tienes")
			else:
				print("Abres el casette y esta vacio, a saber donde está la cinta")
				print("te quedas con las INSTRUCCIONES, ahora estan en el INVENTARIO")
				print("Teclea INVENTARIO, para acceder al inventario")
				inventario.append("INSTRUCCIONES")
		elif respuesta==("ABRIR ARMARIO"):
			print("Abres el armario y está mas vacio que la sala de trofeos del Cadiz C.F.")	
			print("Solo hay un TRAJE y un CHANDAL")
		elif respuesta==("MIRAR ARMARIO"):
			print("Es un armario del IKEA, ya esta un poco viejo y se cae a trozos")
		elif respuesta==("USAR TRAJE"):	
			if traje==False and chandal==False:
				print("Te pones el traje") 
				print("Te queda como un guante, eres todo un vanidoso")
				traje=True		
			elif traje==True:
				print("Ya lo tienes puesto")
			elif chandal==True:
				print("Te quitas el chandal y te pones el traje")
				print("Te queda como un guante, eres todo un vanidoso")
				chandal=False
				traje=True
		elif respuesta==("USAR CHANDAL"):
			if chandal==False and traje==False: 
				print("Te pones el chandal") 
				print("Te vale igual para hacer deporte o para ir a pillar droga")
				chandal=True
			elif chandal==True:
				print("Ya lo tienes puesto")
			elif traje==True:
				print("Te quitas el traje y te pones el chandal")
				print("Te vale igual para hacer deporte o para ir a pillar droga")
				traje=False
				chandal=True
		elif respuesta==("USAR CAMA"):
			print("¿Quieres echarte un sueñecito?")
			dormir=input("SI/NO>")
			if dormir == ("SI"):
				dia+=1
				print("Has dormido, hoy es el dia " + str(dia))			
			elif dormir!=("NO") and dormir!=("SI"):
				print("No te entiendo")
		elif respuesta==("MIRAR TRAJE"):
			print("Te lo compraste de oferta, es de Emidio Tucci")
		elif respuesta==("MIRAR CHANDAL"):
			print("Chandal de cani estandar")
		elif respuesta==("MIRAR CAMA"):
			print("Esta sin hacer, y aun huele a tigre")
		elif respuesta==("MIRAR ESPEJO"):
			print("De primeras, te asustas, tienes 40 años y aun no te has conseguido acostumbrar a tu cara")
		elif respuesta==("INVENTARIO"):
			inv()
		elif respuesta==("ESTADO"):
			estado()
		elif respuesta==("PROCASTINAR"):
			procastinar()
		elif respuesta==("DESCRIPCION"):
			print ("Estas en tu habitacion, hay una MESITA de noche, un ARMARIO, una CAMA, y una puerta hacia el SALON ")
		else:
			print("No te entiendo")
		respuesta=input(">")
	salon()
def final():
	print ("GAME OVER")



print ("La Busqueda, La Aventura")
print ("========================")
print ("")
print ("Pipipipipipi")
print ("Son las 6:00 de la mañana, ha sido una noche muy calurosa y has sudado como si fuera Écija a las 12 de la tarde en Agosto")
print ("El DESPERTADOR no deja de sonar")
print ("¿Qué quieres hacer?")
print ("Los comandos han de introducirse EN MAYUSCULAS")
oficina()
while respuesta!=("SEGUIR DURMIENDO"):
	if respuesta == ("APAGAR DESPERTADOR"):
		dormitorio()
	else:
		print("No te entiendo")

	respuesta=input(">")
print ("Te quedas dormido otra vez hasta las 2 de la tarde, así no vas a encontrar trabajo nunca")
final()
	