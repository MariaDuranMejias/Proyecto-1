def Mostrar_Jugadores():
    busqueda = "Jugador:"
    lineas_escribir = []
    with open("Jugadores.txt", "r") as archivo_lectura:
        numero_linea = 0
        for linea in archivo_lectura:
            numero_linea += 1
            linea = linea.rstrip()
            separado = linea.split(" ")
            if busqueda in separado:
                lineas_escribir.append(linea)
        resultado = []
        for item in lineas_escribir:
            if item not in resultado:
                resultado.append(item)
        #print(resultado)
    return resultado

