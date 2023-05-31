def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()
    
    lista_gen = []
    gen_actual = ""
    
    for linea in lineas:
        linea = linea.strip()
        
        if linea.startswith(">"):
            if gen_actual:
                lista_gen.append(gen_actual)
            gen_actual = ""
        else:
            gen_actual += linea
    
    if gen_actual:
        lista_gen.append(gen_actual)
    
    return lista_gen


archivo_txt = 'a.txt'  # Reemplaza con el nombre de tu archivo

lista_gen = leer_archivo(archivo_txt)
print(lista_gen)