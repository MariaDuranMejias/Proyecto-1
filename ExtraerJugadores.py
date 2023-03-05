#Se define la funcion que extrae del archivo de texto: "Jugadores.txt" los nombres de los jugadores existentes para que el/los jugadores puedan seleccionar
def Mostrar_Jugadores():
    busqueda = "Jugador:"
    lineas_escribir = []
    with open("Jugadores.txt", "r") as archivo_lectura:
        for linea in archivo_lectura:
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