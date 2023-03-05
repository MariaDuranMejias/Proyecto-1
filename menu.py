#Este es el menu inicial donde se muestran las opciones que se tienen y la persona selecciona la opcion que desee
print("¡Bienvenido!")
print("Menu:")
print(" 1 = Juego de 1 jugador \n 2 = Juego de 2 jugadores \n 3 = Reglas del Juego \n 4 = Historial de jugadores \n 5 = Salir ")

jugador = int(input("Digite la opcion que desea realizar: \n"))

if jugador == 1:
    import juego1 as juego1
if jugador == 2:
    import juego2 as juego2
if jugador == 3:
    print("Gana el que tiene 21 o el mas cercano a 21\n Puedes pedir carta o plantarte\n Si tienes un valor mayor a 21 pierdes\n Tienes que tener un valor mayor al Dealer para ganar")
if jugador == 4:
    import resultados as resultados
if jugador == 5:
    print("¡Gracias por jugar!")