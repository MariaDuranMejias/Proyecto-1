import Cards
import JoinToGame
import ejemplo
import MenuInicial

def turno_casa():
    print("Las cartas de la casa son:")
    MenuInicial.Card()
    resultado_casa2 = print("?")
    return 


def turno_Jugador1():

    print("Las cartas de", JoinToGame.NombreJugador1, "son:")
    resultado1 = Cards.Cards()
    valor_resultado1 = ejemplo.Deck

    # resultado2 = (Cards.Cards())
    # valor_resultado2 = Cards.Deck()

    # turno1 = valor_resultado1 + valor_resultado2
    # resultado_turno1 = sum(turno1)
    # print( resultado_turno1)

        #     if resultado_turno1 < 21:
        #         print("Su resultado es: ", resultado_turno1)
        #         turno2 = input("Este resultado es menor a 21, quiere otra carta: 'si' o 'no' \n")
        #         resultado3 = (Cards.Cards())
        #         turno2 = resultado1 + resultado2 + resultado3
        #         resultado_turno2 = sum(turno2)
        #         print(resultado_turno2)

        #     print("Las cartas de la casa son: \n")
        #     print(resultado_casa1)
        #     resultado_casa2 = print("?")
        #     print("Las cartas de", JoinToGame.NombreJugador1, "son:")
        #     print(resultado1)
        #     print(resultado2)
        #     print(resultado3)

        #     if resultado_turno2> 21:
        #         print("Su resultado es mayor a 21, ha perdido la partida \n")

        #     if resultado_turno1 == 21:
        #         print("Su resultado es igual a 21, ha ganado la partida \n")

        # if Cantidad_de_jugadores == 2:
        #     resultado1_jugador1 = (Cards.Cards())
        #     resultado2_jugador1 = (Cards.Cards())
        #     turno1_jugador1 = resultado1_jugador1 + resultado2_jugador1
        #     resultado_turno1_jugador1 = sum(turno1_jugador1)
        #     print(resultado_turno1_jugador1)
        #     if resultado_turno1_jugador1 < 21:
        #         print("El resultado del jugador:,  resultado es: ", resultado_turno1_jugador1)
        #         turno2 = input("Este resutlado es menor a 21, quiere otra carta: 'si' o 'no' \n")

        #     if resultado_turno1_jugador1 > 21:
        #         print("Su resultado es mayor a 21, ha perdido la partida \n")

        #     if resultado_turno1_jugador1 == 21:
        #         print("Su resultado es igual a 21, ha ganado la partida \n")


    return

Game = JoinToGame.NewGame
Cantidad_de_jugadores = JoinToGame.CantidadJugadores

if Game == 'si':

    if Cantidad_de_jugadores == 1:
        turno_casa()
        #turno_Jugador1()

