import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage #Para el metodo UPGMA y otros si se usan
from scipy.spatial import distance #Distancias
from scipy.cluster import hierarchy


	#lista con cada gen de cada pulpo
gen_cephalopoda = np.array([])


#Metrica entre dos conjuntos o mejor conocido como distancia de Jaccard
def DistancaJarccad(set1, set2):
	intersection = len(set(set1).intersection(set(set2)))
	union = len(set(set1).union(set(set2)))
	return 1 - (intersection / union)

def Ejecucion(file_name):
	global gen_cephalopoda
	fichero = open(file_name,'r')
	archivo = fichero.readlines()
	cadena = archivo[1]
	gen_cephalopoda = np.append(gen_cephalopoda,cadena)
	fichero.close()

def MatrizDistanciaJaccard():
		#Creación de la matriz de distancias usando la distancia de Jaccard
	n = len(gen_cephalopoda)
	matrix_distance = np.zeros((n, n))
	for i in range(n):
		for j in range(i):
			distancia_conjuntos = DistancaJarccad(gen_cephalopoda[i], gen_cephalopoda[j])
			matrix_distance[i, j] = distancia_conjuntos
			matrix_distance[j, i] = distancia_conjuntos
	return matrix_distance

def UPGMAJaccard():
		# Construir el árbol filogenético utilizando el método UPGMA
	linkage_matrix = linkage(MatrizDistanciaJaccard(), method='average')
		# Generar el dendrograma
	dendrogram(linkage_matrix)
		# Mostrar el árbol filogenético
	plt.xlabel('Especies')
	plt.ylabel('Distancia')
	plt.title('Árbol Filogenético (UPGMA) con distancia Jaccard')
	plt.show()

def WPGMAJaccard():
	linkage_matrix = linkage(MatrizDistanciaJaccard(), method="weighted")
	dendrogram(linkage_matrix)
	plt.xlabel('Especies')
	plt.ylabel('Distancia')
	plt.title('Árbol Filogenético (WPGMA) con distancia Jaccard')
	plt.show()

def MatrizDistanciaHamming():
	n = len(gen_cephalopoda)
	matrix_distance = np.zeros((n, n))
	for i in range(n):
		for j in range(i):
			distancia_conjuntos = distance.hamming(gen_cephalopoda[i], gen_cephalopoda[j])
			matrix_distance[i, j] = distancia_conjuntos
			matrix_distance[j, i] = distancia_conjuntos
	return matrix_distance

def UPGMAHamming():
	linkage_matrix = linkage(MatrizDistanciaHamming(), method='average')
		# Generar el dendrograma
	dendrogram(linkage_matrix)
		# Mostrar el árbol filogenético
	plt.xlabel('Especies')
	plt.ylabel('Distancia')
	plt.title('Árbol Filogenético (UPGMA) con distancia Hamming')
	plt.show()

def WPGMAHamming():
	linkage_matrix = linkage(MatrizDistanciaHamming(), method="weighted")
	dendrogram(linkage_matrix)
	plt.xlabel('Especies')
	plt.ylabel('Distancia')
	plt.title('Árbol Filogenético (WPGMA) con distancia Hamming')
	plt.show()

#Rhodopsin
#Ejecucion("A0A3G2LZK9.txt")
#Ejecucion("A0A3G2LZL0.txt")
#Ejecucion("A0A3G2LZM2.txt")
#Ejecucion("A0A3G2M004.txt")
#Ejecucion("H2B4T6.txt")
#Ejecucion("C9D7Q0.txt")
#Ejecucion("A0A6G8MYZ4.txt")
#Ejecucion("A0A6G8MZH0.txt")
#Ejecucion("A0A6G8MYM9.txt")
#Ejecucion("A0A6G8MYQ4.txt")
#Ejecucion("A0A0S2PHZ2.txt")
#Ejecucion("H2B4U5.txt")
#Ejecucion("H2B4U1.txt")

	#cytochrome b
Ejecucion("Amphioctopus fangsiao.txt")
Ejecucion("Callistoctopus minor.txt")
Ejecucion("Ectyoplasia ferox.txt")
Ejecucion("Octopus bimaculatus.txt")
Ejecucion("Octopus bimaculoides.txt")
Ejecucion("Octopus conispadiceus.txt")
Ejecucion("Octopus cyanea.txt")
Ejecucion("Octopus fitchi.txt")
Ejecucion("Octopus mimus.txt")
Ejecucion("Octopus salutii.txt")
Ejecucion("Octopus sinensis.txt")
Ejecucion("Octopus variabilis.txt")
Ejecucion("Octopus vulgaris.txt")
gen_cephalopoda = gen_cephalopoda.reshape((len(gen_cephalopoda), 1))
UPGMAJaccard()
UPGMAHamming()

WPGMAJaccard()
WPGMAHamming()