import os
"""
INTEGRANTES:
Dozal Magnani Diego
Ramírez Cortés Hugo Giovani
"""
#####
a = "T1"
fichero = open("Cadenas/" + a + ".txt")
archivo = fichero.readlines()
cadena = archivo[1]
fichero.close()

codones_traduccion = {"GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A", # Alanina
    # Cisteina
    "UGU":"C", "UGC":"C",
    # Acido aspartico
    "GAU":"D", "GAC":"D",
    # Acido glutamico
    "GAA":"E", "GAG":"E",
    # Fenilalanina
    "UUU":"F", "UUC":"F",
    # Glicina
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",
    # Histidina
    "CAU":"H", "CAC":"H",
    # Isoleucina
    "AUA":"I", "AUU":"I", "AUC":"I",
    # Lisina
    "AAA":"K", "AAG":"K",
    # Leucina
    "UUA":"L", "UUG":"L", "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    # Metionina
    "AUG":"M", 
    # Aspargina
    "AAU":"N", "AAC":"N",
    # Prolina
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    # Glutamina
    "CAA":"Q", "CAG":"Q",
    # Arginina
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R", "AGA":"R", "AGG":"R",
    # Serina
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S", "AGU":"S", "AGC":"S",
    # Treonina
    "ACU":"U", "ACC":"U", "ACA":"U", "ACG":"U",
    # Valina
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    # Triptofano
    "UGG":"W",
    # Tirosina
    "UAU":"Y", "UAC":"Y",
    # Stop
    "UAA":"_", "UAG":"_", "UGA":"_"}
#Funcion para convertir ADN 3-5 a su complemento 5-3
def Convertir_Complemento(cad):
	cadena_complementaria = ''
	for i in range(0,len(cad)):
		#Tomamos la letra en la posición i, vemos que letra es y la cambiamos por su complementaria
		if cad[i] == 'A':
			cadena_complementaria += 'T'
		elif cad[i] == 'T':
			cadena_complementaria += 'A'
		elif cad[i] == 'C':
			cadena_complementaria += 'G'
		elif cad[i] == 'G':
			cadena_complementaria += 'C'
	return cadena_complementaria
#Funcion para convertir ADN 3-5 ah ARN
def Transcripcion(cad):
	cadena_transcripta = ''
	for i in range(0,len(cad)):
		#Cambiar en la cadena de ADN cada Timina por Uracilo
		if cad[i] == 'T':
			cadena_transcripta += 'U'
		else:
			cadena_transcripta += cad[i]
	return cadena_transcripta
#Traduccion de un codon
def Traduccion(cad):
	codon = "-"
	if cad in codones_traduccion:
		codon = codones_traduccion[cad]
	return codon
#Funcion para convertir ARN en proteinas si en el inicio de la cadena empieza con AUG ó GUG
def Traduccion_inicio_fin(cad):
	cadena_traducida = ''
	"""
	Si los primeros valores de la cadena son los codones de inicio entonces empieza la traducción, de 
	lo contrario termina el programa
	"""
	if cad[0:3] == "AUG" or cad[0:3] == "GUG":
		for i in range(0,int(1/3*len(cad))):
			#Terminar la traducción si encuentras el codon de fin
			if cad[3*i:3*i+3] == "UAA" or cad[3*i:3*i+3] == "UAG" or cad[3*i:3*i+3] == "UGA":
				cadena_traducida += Traduccion(cad[3*i:3*i+3])
				return cadena_traducida
			#Si no termina entonces traduce ese codon
			else:
				cadena_traducida += Traduccion(cad[3*i:3*i+3])
	else:
		return 'Tu cadena de ARN no comienza con los codones AUG ó GUG'
a = Convertir_Complemento(cadena)
b = Transcripcion(cadena)
c = Traduccion_inicio_fin(b)
print(c)
