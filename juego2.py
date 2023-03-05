import random
import ExtraerJugadores

#Se declaran las listas de simbolos, numeros y valores que se van a utilizar 
suits = ('\u2764', '\u2666', '\u2660', '\u2618')
ranks = ('Dos', 'Tres', 'Cuatro', 'Cinco', 'Seis', 'Siete', 'Ocho', 'Nueve', 'Diez', 'J', 'Q', 'K', 'A')
values = {'Dos': 2, 'Tres': 3, 'Cuatro': 4, 'Cinco': 5, 'Seis': 6, 'Siete': 7, 'Ocho': 8,'Nueve': 9, 'Diez': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

#Condiciones que se van a dar mientras se esta jugando
playing = True

# Clases:

class Card:  # Crear todas las cartas

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' de ' + self.suit

class Deck:  # Crear una baraja de las cartas

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comb = ''
        for card in self.deck:
            deck_comb += '\n ' + card.__str__()
        return 'La baraja tiene: ' + deck_comb

    def shuffle(self):  # Mezcla de todas las cartas en la baraja
        random.shuffle(self.deck)

    def deal(self):  # Repartir una carta
        single_card = self.deck.pop()
        return single_card

class Hand:   # Mostrar las cartas que el dealer y jugadores tienen

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0  # Seguimientos de las aces = As

    def add_card(self, card):  # Agregar una carta a la mano de los jugadores y dealer
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'A':
            self.aces += 1

    def ajuste_de_as(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

# Funciones:

def tomar_carta(deck, hand):  #Tomar una carta
    hand.add_card(deck.deal())
    hand.ajuste_de_as()

def tomar_carta_o_parar(deck, hand):   # Tomar carta o no tomar carta
    global playing
    while True:
        ask = input("\n" + NombreJugador1 + " ¿Desea tomar una carta? Digite 's' o 'n': ")
        if ask[0].lower() == 's':
            tomar_carta(deck, hand)
        elif ask[0].lower() == 'n':
            print( "Jugador 1 para, Dealer sigue jugando.")
            playing = False
        break
def tomar_carta_o_parar2(deck, hand):   # Tomar carta o no tomar carta
    global playing
    while True:
        ask = input("\n" + NombreJugador2 + " ¿Desea tomar una carta? Digite 's' o 'n': ")
        if ask[0].lower() == 's':
            tomar_carta(deck, hand)
        elif ask[0].lower() == 'n':
            print( "Jugador 2 para, Dealer sigue jugando.")
            playing = False
        break


def mostrar_carta(player, player2, dealer): #Muestra las cartas del dealer enmascarada y las de los jugadores
    print("\nMano del Dealer: ")
    print(" <X> ")
    print("", dealer.cards[1])
    print("Mano de " + NombreJugador1 + ":", *player.cards, sep='\n ')
    print("Mano de " + NombreJugador2 + ":", *player2.cards, sep='\n ')

def mostrar_todas_las_cartas(player, player2, dealer): #Muestra las cartas del dealer y de los jugadores
    print("\nMano del Dealer: ", *dealer.cards, sep='\n ')
    print("Mano del Dealer =", dealer.value)
    print("\nMano de " + NombreJugador1 + ":", *player.cards, sep='\n ')
    print("Mano de " + NombreJugador1 + "=", player.value)
    print("\n Mano de " + NombreJugador2 + ":", *player2.cards, sep='\n ')
    print("Mano de " + NombreJugador2 + "=", player2.value)

# Funciones para declarar los resultado de los jugadores y escribirlas en el archivo de texto: resultados.txt

def player_pierde(player, player2, dealer):
    print("¡JUGADOR 1 PERDIO!")
    resultados.write(NombreJugador1 + " " + "PERDIO" "\n")

def player_gana(player, player2, dealer):
    print("¡JUGADOR 1 GANA!")
    resultados.write(NombreJugador1 + " " + "GANA" "\n")

def player2_pierde(player, player2, dealer):
    print("¡JUGADOR 2 PERDIO!")
    resultados.write(NombreJugador2 + " " + "PERDIO" "\n")

def player2_gana(player, player2, dealer):
    print("¡JUGADOR 2 GANA!")
    resultados.write(NombreJugador2 + " " + "GANA" "\n")


def empate_player_dealer(player, dealer):
    print("¡OHH! ¡Empate entre Dealer y " + NombreJugador1)
    resultados.write(NombreJugador1 + " " + "EMPATA" "\n")

def empate_player2_dealer(player2, dealer):
    print("¡OHH! ¡Empate entre Dealer y " + NombreJugador2)
    resultados.write(NombreJugador2 + " " + "EMPATA" "\n")

def empate_player_player2(player2, dealer):
    print("¡OHH! ¡Empate entre " + NombreJugador1 + "y" + NombreJugador2)
    resultados.write(NombreJugador2 + " " + "EMPATA" "\n")

# Inicio del juego
# Se pregunta si se quiere iniciar un juego nuevo
# Si la respuesta es si, se abre el archivo jugadores.txt donde se va a almacenar el historial de jugadores
# Se pregunta si quiere usar un jugador existente o crear uno nuevo
# Si elige un jugador existente, tendra las estadisticas de este jugador
while True:
    print("¡Bienvenido al Juego BlackJack!")

    NewGame = str(input("Para iniciar el juego entre 2 jugadores, digite 'si': \n"))

    if NewGame == 'si':
        file = open("jugadores.txt", "a")
        resultados = open("resultados.txt", "a")
        opcion = int(input("Jugador 1 digite '1' si desea utilizar el nombre de un jugador existente o '2' si es un nuevo nombre  \n"))
        if opcion == 1:
            print(ExtraerJugadores.Mostrar_Jugadores())
            NombreJugador1 = input("Eliga el nombre del jugador\n")
        elif opcion == 2:
            NombreJugador1 = str(input("Digite el nombre del Jugador 1: \n"))
            file.write("Jugador: " +  NombreJugador1 + "\n")
    deck = Deck()
    deck.shuffle()
    print("Estadisticas jugador " + NombreJugador1 + ":")
    with open("resultados.txt", "r") as archivo_lectura:
        for linea in archivo_lectura:
            linea = linea.rstrip()
            if NombreJugador1 in linea:
                print(linea)
						

			
        opcion1 = int(input("Jugador 2 digite '1' si desea utilizar el nombre de un jugador existente o '2' si es un nuevo nombre  \n"))
        if opcion1 == 1:
            print(ExtraerJugadores.Mostrar_Jugadores())
            NombreJugador2 = input("Eliga el nombre del jugador\n")
        elif opcion1 == 2:
            NombreJugador2 = str(input("Digite el nombre del Jugador 2: \n"))
            file.write("Jugador: " +  NombreJugador2 + "\n")
    print("Estadisticas jugador " + NombreJugador2 + ":")
    with open("resultados.txt", "r") as archivo_lectura:
        for linea in archivo_lectura:
            linea = linea.rstrip()
            if NombreJugador2 in linea:
                print(linea)
				
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    player2_hand = Hand()
    player2_hand.add_card(deck.deal())
    player2_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

# mostrar las cartas
    mostrar_carta(player_hand, player2_hand, dealer_hand)

    while playing:

        tomar_carta_o_parar(deck, player_hand)
        mostrar_carta(player_hand, player2_hand, dealer_hand)
        tomar_carta_o_parar2(deck, player2_hand)
        mostrar_carta(player_hand, player2_hand, dealer_hand)

    if player_hand.value <= 21 and player2_hand.value <= 21:

        while dealer_hand.value <= 21:
            tomar_carta(deck, dealer_hand)

        mostrar_todas_las_cartas(player_hand, player2_hand, dealer_hand)                  

    if player_hand.value > 21 and player2_hand.value > 21:
        player_pierde(player_hand, player2_hand, dealer_hand)
        player2_pierde(player_hand, player2_hand, dealer_hand)
        break
    if dealer_hand.value == 21:
        player_pierde(player_hand, player2_hand, dealer_hand)
        player2_pierde(player_hand, player2_hand, dealer_hand)

    if dealer_hand.value > 21:
        if player_hand.value < 21 and player2_hand.value > 21:
            player_gana(player_hand, player2_hand, dealer_hand)

        if player_hand.value > 21 and player2_hand.value < 21:
            player2_gana(player_hand, player2_hand, dealer_hand)

        if player_hand.value == 21:
            player_gana(player_hand, player2_hand, dealer_hand)

        if player2_hand.value == 21:
            player2_gana(player_hand, player2_hand, dealer_hand)

        if player_hand.value == player2_hand.value:
            empate_player_player2(player_hand, player2_hand, dealer_hand)

    elif dealer_hand.value < player_hand.value and player2_hand.value < player_hand.value:
        player_gana(player_hand, player2_hand, dealer_hand)

    elif dealer_hand.value < player2_hand.value and player_hand.value < player2_hand.value:
        player2_gana(player_hand, player2_hand, dealer_hand)

    elif dealer_hand.value < 21 and player_hand.value < 21  and player2_hand.value < 21 and dealer_hand.value > player_hand.value and dealer_hand.value > player2_hand.value:
        player_pierde(player_hand, player2_hand, dealer_hand)
        player2_pierde(player_hand, player2_hand, dealer_hand)

    elif dealer_hand.value < 21 and player_hand.value < 21 and dealer_hand.value < player_hand.value and player2_hand.value < 21 and player2_hand.value < player_hand.value:
        player_gana(player_hand, player2_hand, dealer_hand)

    elif dealer_hand.value < 21 and player2_hand.value < 21 and dealer_hand.value < player2_hand.value and player_hand.value < 21 and player_hand.value < player2_hand.value:
        player2_gana(player_hand, player2_hand, dealer_hand)

    new_game = input("\n¿Desea jugar otra partida? Escriba 's' o 'n': ")
    if new_game[0].lower() == 's':
        playing = True
        continue
    if new_game[0].lower() == 'n':
        import menu as menu
        break