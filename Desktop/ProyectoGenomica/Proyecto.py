import numpy as np
import matplotlib.pyplot as plt
import re
import sys

# Para el metodo UPGMA y otros si se usan
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial import distance  # Distancias
from scipy.cluster import hierarchy

lista_nombres_gen = []
colores = [
    "blue",
    "green",
    "red",
    "cyan",
    "magenta",
    "yellow",
    "black",
    "darkorange",
    "lime",
    "purple",
    "brown",
    "pink",
    "gray",
    "olive",
    "teal",
    "gold",
    "navy",
    "darkgreen",
    "salmon",
    "indigo",
    "peru",
    "deeppink",
    "slategray",
    "darkviolet",
    "sienna",
    "limegreen",
    "orchid",
    "chocolate",
    "crimson",
    "dodgerblue",
    "forestgreen",
    "hotpink",
    "steelblue",
    "saddlebrown",
    "darkslategray",
    "mediumorchid",
    "darkgoldenrod",
    "mediumblue",
    "mediumseagreen",
    "firebrick",
    "mediumvioletred",
    "cornflowerblue",
    "seagreen",
    "tomato",
    "darkorchid",
    "cadetblue",
    "darkkhaki",
    "rosybrown",
    "darksalmon",
    "mediumslateblue",
]


ventana = [
    100,
    200,
    300,
    400,
    500,
    600,
    610,
    620,
    630,
    640,
    650,
    700,
    750,
    800,
    850,
    900,
    1000,
    1100,
    1200,
    1300,
    1400,
    1500,
    1600,
    1700,
    1827,
]

# ventana = [i for i in range(1, 1827)]


def leer_archivo(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        lineas = archivo.readlines()
    lista_gen = []
    gen_actual = ""
    for linea in lineas:
        linea = linea.strip()
        if linea.startswith(">"):
            if gen_actual:
                lista_gen.append(gen_actual)
            gen_actual = ""
            lista_nombres_gen.append(linea[1:])
        else:
            gen_actual += linea
    if gen_actual:
        lista_gen.append(gen_actual)
    return lista_gen


# ///Metricas(distancias)/// #


# Metrica entre dos conjuntos o mejor conocido como distancia de Jaccard
def Jaccard(set1, set2):
    intersection = len(set(set1).intersection(set(set2)))
    union = len(set(set1).union(set(set2)))
    return 1 - (intersection / union)


# Metrica entre caracteres o conocida como distancia de Hamming
def Hamming(cad1, cad2):
    if len(cad1) != len(cad2):
        raise ValueError("Las cadenas deben tener la misma longitud.")
    distancia = 0
    for i in range(len(cad1)):
        if cad1[i] != cad2[i]:
            distancia += 1
    return distancia


# Metrica entre dos secuencias utilizando su contenido ATCG
def PorContenido(cad1, cad2):
    if len(cad1) != len(cad2):
        raise ValueError("Las cadenas deben tener la misma longitud.")
    distancia = abs(ContenidoCG(cad1, len(cad1)) - ContenidoCG(cad2, len(cad2)))
    return distancia


# ///Matriz de distancias/// #


def MatrizDistancia(Distancia):
    n = len(lista_gen)
    matrix_distance = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            distancia_conjuntos = Distancia(lista_gen[i], lista_gen[j])
            matrix_distance[i, j] = distancia_conjuntos
            matrix_distance[j, i] = distancia_conjuntos
    return matrix_distance


# ///Tipos de arboles filogeneticos/// #


def ArbolUPGMADistancia(Distancia):
    linkage_matrix_upgma = linkage(MatrizDistancia(Distancia), method="average")
    return linkage_matrix_upgma


def ArbolWPGMADistancia(Distancia):
    linkage_matrix_wpgma = linkage(MatrizDistancia(Distancia), method="weighted")
    return linkage_matrix_wpgma


def ArbolUPGMA(arbolJac, arbolHam, arbolRar):
    plt.figure(figsize=(12, 6))
    plt.title("A")
    ######################
    plt.subplot(1, 3, 1)
    plt.tick_params(axis="both", which="major", labelsize=8)
    plt.title("Métrica Jaccard")
    dendrogram(
        arbolJac,
        labels=lista_nombres_gen,
        orientation="left",
        leaf_font_size=6,
    )
    ######################
    plt.subplot(1, 3, 2)
    plt.tick_params(axis="both", which="major", labelsize=8)
    plt.title("Métrica Hamming")
    dendrogram(
        arbolHam,
        labels=lista_nombres_gen,
        orientation="left",
        leaf_font_size=6,
    )
    ######################
    plt.subplot(1, 3, 3)
    plt.tick_params(axis="both", which="major", labelsize=8)
    plt.title("Métrica por Contenido A-T-C-G")
    dendrogram(
        arbolRar,
        labels=lista_nombres_gen,
        orientation="left",
        leaf_font_size=6,
    )
    ######################
    plt.suptitle("Arboles Filogenéticos (UPGMA)")
    plt.tight_layout()
    plt.show()


def ArbolWPGMA(arbolJac, arbolHam, arbolRar):
    plt.figure(figsize=(12, 6))
    plt.title("A")
    ######################
    plt.subplot(1, 3, 1)
    plt.tick_params(axis="both", which="major", labelsize=8)
    plt.title("Métrica Jaccard")
    dendrogram(
        arbolJac,
        labels=lista_nombres_gen,
        orientation="left",
        leaf_font_size=6,
    )
    ######################
    plt.subplot(1, 3, 2)
    plt.tick_params(axis="both", which="major", labelsize=8)
    plt.title("Métrica Hamming")
    dendrogram(
        arbolHam,
        labels=lista_nombres_gen,
        orientation="left",
        leaf_font_size=6,
    )
    ######################
    plt.subplot(1, 3, 3)
    plt.tick_params(axis="both", which="major", labelsize=8)
    plt.title("Métrica por Contenido A-T-C-G")
    dendrogram(
        arbolRar,
        labels=lista_nombres_gen,
        orientation="left",
        leaf_font_size=6,
    )
    ######################
    plt.suptitle("Arboles Filogenéticos (WPGMA)")
    plt.tight_layout()
    plt.show()


# ///Contenido C-G y A-T/// #


def ContenidoCG(cadena, ventana_temporal):
    if ventana_temporal > len(cadena):
        ventana_temporal = len(cadena)
    # Tomamos la ventana de longitud ventana_temporal y analizamos su contenido CG
    cad = cadena[:ventana_temporal]
    # Expresiones regulares que buscar el contenido CG y los vacios
    expC = r"C"
    expG = r"G"
    exp = r"-"
    # Buscamos la cantidad de veces que sale C, G  y los vacios en la secuencia
    contenidoC = len(re.findall(expC, cad))
    contenidoG = len(re.findall(expG, cad))
    vacios = len(re.findall(exp, cad))  # Conteo de vacios en la cadena
    # Si en esa ventana hay puros vacios, el contenido AT es cero, de hecho el CG tambien

    if (len(cad) - vacios) == 0:
        return 0

    contenidoCG = (contenidoC + contenidoG) / (len(cad))  # (len(cad) - vacios)
    return contenidoCG


def ContenidoAT(cadena, ventana_temporal):
    if ventana_temporal > len(cadena):
        ventana_temporal = len(cadena)
    # Tomamos la ventana de longitud ventana_temporal y analizamos su contenido AT
    cad = cadena[:ventana_temporal]
    # Expresiones regulares que buscar el contenido AT y los espacios
    expA = r"A"
    expT = r"T"
    exp = r"-"
    # Buscamos la cantidad de veces que sale A,T y los vacios en la secuencia
    contenidoA = len(re.findall(expA, cad))
    contenidoT = len(re.findall(expT, cad))
    vacios = len(re.findall(exp, cad))
    # Si en esa ventana hay puros vacios, el contenido AT es cero, de hecho el CG tambien
    """
    if (len(cad) - vacios) == 0:
        return 0
    """
    contenidoAT = (contenidoA + contenidoT) / len(cad)  # (len(cad) - vacios)
    return contenidoAT


def Contenido(cadena, ventana_temporal):
    if ventana_temporal > len(cadena):
        ventana_temporal = len(cadena)
    # Tomamos la ventana de longitud ventana_temporal y analizamos su contenido AT
    cad = cadena[:ventana_temporal]
    # Expresiones regulares que buscar el contenido ATCG y los espacios
    expA = r"A"
    expT = r"T"
    expC = r"C"
    expG = r"G"
    exp = r"-"
    # Buscamos la cantidad de veces que sale A,T,C,G y los vacios en la secuencia
    contenidoA = len(re.findall(expA, cad))
    contenidoT = len(re.findall(expT, cad))
    contenidoC = len(re.findall(expC, cad))
    contenidoG = len(re.findall(expG, cad))
    vacios = len(re.findall(exp, cad))
    # Si en esa ventana hay puros vacios, el contenido ATCG es cero
    """
    if (len(cad) - vacios) == 0:
        return 0
    """
    contenido = (contenidoA + contenidoT + contenidoC + contenidoG) / (
        len(cad)
    )  # (len(cad) - vacios)
    return contenido

    # Iterar sobre los datos y asignarlos a los subplots correspondientes
    for i, datos_grafica in enumerate(datos):
        ax = axs[i // 10] if num_subplots > 1 else axs
        ax.plot(ventana, datos_grafica, color=colores[i % len(colores)])
        x, y = len(ventana) - 0.05, datos_grafica[-1]
        # Añadir el nombre de la función al lado derecho de la línea
        ax.text(
            x,
            y,
            nombres[i],
            fontsize=8,
            color=colores[i % len(colores)],
            va="center",
            ha="left",
        )
        ax.set_title(f"Gráficas de línea (Grupo {int((i+1)/10)})")
        ax.set_xlabel("Ventanas")
        ax.set_ylabel("Valor")
    # Mostrar la gráfica
    plt.show()


def GraficarContenido(lista, nombres, Contenido):
    datos = []  # Lista que graficaremos
    etiqueta_ventana = [str(i + 1) for i in range(len(ventana))]
    # Llenamos la lista con la informacion
    for i in range(len(lista)):
        datos_gen = []
        for j in range(len(ventana)):
            datos_gen.append(Contenido(lista[i], ventana[j]))
        datos.append(datos_gen)
    # Crear una figura y un conjunto de subgráficas
    fig, ax = plt.subplots()
    # Iterar sobre cada lista de datos y colorear la gráfica correspondiente
    for i, datos_grafica in enumerate(datos):
        ax.plot(ventana, datos_grafica, color=colores[i % len(colores)])
        x, y = 1830, datos_grafica[-1]
        for j in range(i):
            if abs(y - ax.texts[j].get_position()[1]) < 0.0001:
                y += 0.00008
        # Añadir el nombre de la función al lado derecho de la línea
        ax.text(
            x,
            y,
            nombres[i],
            fontsize=7,
            color=colores[i % len(colores)],
            va="center",
            ha="left",
        )
    # Configurar el título y las etiquetas de los ejes
    ax.set_title("Gráficas de línea")
    ax.set_xlabel("Ventanas")
    ax.set_ylabel("Valor")
    # Mostrar la gráfica
    plt.show()


archivo_txt = "a.txt"  # Nombre del archivo
lista_gen = leer_archivo(archivo_txt)
"""for i in range(len(lista_gen)):
    print(ContenidoCG(lista_gen[i], 700), lista_nombres_gen[i])"""

#GraficarContenido(lista_gen, lista_nombres_gen, ContenidoAT)


"""
ArbolUPGMA(
    ArbolUPGMADistancia(Jaccard),
    ArbolUPGMADistancia(Hamming),
    ArbolUPGMADistancia(PorContenido),
)


ArbolWPGMA(
    ArbolUPGMADistancia(Jaccard),
    ArbolUPGMADistancia(Hamming),
    ArbolUPGMADistancia(PorContenido),
)
"""
#print(lista_nombres_gen)


if __name__ == '__main__':

    option =  int(sys.argv[2])

    if(option ==1):
        GraficarContenido(lista_gen, lista_nombres_gen, ContenidoAT)
    if(option==2):
        ArbolUPGMA(
        ArbolUPGMADistancia(Jaccard),
        ArbolUPGMADistancia(Hamming),
        ArbolUPGMADistancia(PorContenido),
        )
    if(option==3):
        ArbolWPGMA(
        ArbolWPGMADistancia(Jaccard),
        ArbolWPGMADistancia(Hamming),
        ArbolWPGMADistancia(PorContenido),
    )

