#Lo primero que se debe hacer es iniciar un juego nuevo

NewGame = str(input("Iniciar nuevo juego: elige 'si' o 'no' para continuar: \n"))

if NewGame == 'si':
    file = open("jugadores.txt", "a")
    CantidadJugadores = int(input("Elige la cantidad de jugadores: '1' o '2' \n"))
    if CantidadJugadores == 1:
        NombreJugador1 = str(input("Digite el nombre del Jugador 1 \n"))
        file.write("Jugador: " +  NombreJugador1 + "\n")
    elif CantidadJugadores == 2:
        NombreJugador1 = str(input("Digite el nombre del Jugador 1 \n"))
        file.write("Jugador: " +  NombreJugador1 + "\n")
        NombreJugador2 = str(input("Digite el nombre del Jugador 2 \n"))
        file.write("Jugador: " +  NombreJugador2 + "\n")
    elif CantidadJugadores != 1 or 2: 
        print("Cantidad invalida")
if NewGame == 'no':
    print("Menu inicial")