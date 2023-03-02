import random

suits = ('\u2764', '\u2666', '\u2660', '\u2618')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'J', 'Q', 'K', 'A')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,'Nine': 9, 'Ten': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

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

class Hand:   # Mostrar las cartas que el dealer y jugador tienen

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0  # Seguimientos de las aces = As

    def add_card(self, card):  # Agregar una carta a la mano del jugador y dealer
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'A':
            self.aces += 1

    def ajuste_de_as(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

# Funciones:

def tomar_carta(deck, hand):
    hand.add_card(deck.deal())
    hand.ajuste_de_as()

def tomar_carta_o_parar(deck, hand):   # Tomar carta o no tomar carta
    global playing
    while True:
        ask = input("\n" + NombreJugador1 + " desea tomar una carta? Escriba 's' or 'n': ")
        if ask[0].lower() == 's':
            tomar_carta(deck, hand)
        elif ask[0].lower() == 'n':
            print("Jugador para, Dealer sigue jugando.")
            playing = False
        break

# def tomar_carta_o_parar2(deck, hand):
#     global playing
#     while True:
#         ask = input("\n", NombreJugador1 + " desea tomar una carta? Escriba 's' or 'n': ")
#         if ask[0].lower() == 's':
#             tomar_carta(deck, hand)
#         elif ask[0].lower() == 'n':
#             ask1 = input("\n", NombreJugador2 + " desea tomar una carta? Escriba 's' or 'n': ")
#             if ask1[0].lower() == 's':
#                 tomar_carta(deck, hand)
#             elif ask1[0].lower() == 'n':
#                 print("Jugador para, Dealer sigue jugando.")
#                 playing = False
#         break

def mostrar_carta(player, dealer):
    print("\nMano del Dealer: ")
    print(" <X> ")
    print("", dealer.cards[1])
    print("Mano de " + NombreJugador1 + ":", *player.cards, sep='\n ')

def mostrar_todas_las_cartas(player, dealer):
    print("\nMano del Dealer: ", *dealer.cards, sep='\n ')
    print("Mano del Dealer =", dealer.value)
    print("\nMano de " + NombreJugador1 + ":", *player.cards, sep='\n ')
    print("Mano de " + NombreJugador1 + "=", player.value)

# def mostrar_carta2(player, player2, dealer):
#     print("\nMano del Dealer: ")
#     print(" <X> ")
#     print("", dealer.cards[1])
#     print("Mano de " + NombreJugador1 + ":", *player.cards, sep='\n ')
#     print("Mano de " + NombreJugador2 + ":", *player2.cards, sep='\n ')

# def mostrar_todas_las_cartas2(player, dealer, player2):
#     print("\nMano del Dealer: ", *dealer.cards, sep='\n ')
#     print("Mano del Dealer =", dealer.value)
#     print("\nMano de " + NombreJugador1 + ":", *player.cards, sep='\n ')
#     print("Mano de " + NombreJugador1 + "=", player.value)
#     print("\nMano de " + NombreJugador2 + ":", *player.cards, sep='\n ')
#     print("Mano de " + NombreJugador2 + "=", player2.value)

# Final del juego

def player_pierde(player, dealer):
    print("¡JUGADOR PERDIO!")

def player_gana(player, dealer):
    print("¡JUGADOR GANA!")

def dealer_pierde(player, dealer):
    print("¡DEALER PERDIO!")

def dealer_gana(player, dealer):
    print("¡DEALER GANA!")

def empate(player, dealer):
    print("¡OHH! ¡Empate entre Dealer y Jugador!")

# Inicio del juego

while True:
    print("¡Bienvenido al Juego BlackJack!")

    NewGame = str(input("Iniciar nuevo juego: elige 'si' o 'no' para continuar: \n"))

    if NewGame == 'si':
        file = open("jugadores.txt", "a")
        CantidadJugadores = int(input("Elige la cantidad de jugadores: '1' o '2' \n"))
        if CantidadJugadores == 1:
            NombreJugador1 = str(input("Digite el nombre del Jugador 1 \n"))
            file.write("Jugador: " +  NombreJugador1 + "\n")
            deck = Deck()
            deck.shuffle()

            player_hand = Hand()
            player_hand.add_card(deck.deal())
            player_hand.add_card(deck.deal())

            dealer_hand = Hand()
            dealer_hand.add_card(deck.deal())
            dealer_hand.add_card(deck.deal())

            # mostrar las cartas
            mostrar_carta(player_hand, dealer_hand)

            while playing:

                tomar_carta_o_parar(deck, player_hand)
                mostrar_carta(player_hand, dealer_hand)

                if player_hand.value > 21:
                    player_pierde(player_hand, dealer_hand)
                    break

            if player_hand.value <= 21:

                while dealer_hand.value < 17:
                    tomar_carta(deck, dealer_hand)

                mostrar_todas_las_cartas(player_hand, dealer_hand)

                if dealer_hand.value > 21:
                    dealer_pierde(player_hand, dealer_hand)

                elif dealer_hand.value > player_hand.value:
                    dealer_gana(player_hand, dealer_hand)

                elif dealer_hand.value < player_hand.value:
                    player_gana(player_hand, dealer_hand)

                if player_hand.value > 21:
                    player_pierde(player_hand, dealer_hand)

        # elif CantidadJugadores == 2:
        #     NombreJugador1 = str(input("Digite el nombre del Jugador 1 \n"))
        #     file.write("Jugador: " +  NombreJugador1 + "\n")
        #     NombreJugador2 = str(input("Digite el nombre del Jugador 2 \n"))
        #     file.write("Jugador: " +  NombreJugador2 + "\n")
        #     # crear una mezcla de la baraja
        #     deck = Deck()
        #     deck.shuffle()

        #     player_hand = Hand()
        #     player_hand.add_card(deck.deal())
        #     player_hand.add_card(deck.deal())

        #     player_hand2 = Hand()
        #     player_hand2.add_card(deck.deal())
        #     player_hand2.add_card(deck.deal())

        #     dealer_hand = Hand()
        #     dealer_hand.add_card(deck.deal())
        #     dealer_hand.add_card(deck.deal())

        #     # mostrar las cartas
        #     mostrar_carta2(player_hand, player_hand2, dealer_hand)

        #     while playing:

        #         tomar_carta_o_parar2(deck, player_hand)
        #         tomar_carta_o_parar2(deck, player_hand2)
        #         mostrar_carta2(player_hand, player_hand2, dealer_hand)

        #         if player_hand.value > 21:
        #             player_pierde(player_hand, player_hand2, dealer_hand)
        #             break
        #         if player_hand2.value > 21:
        #             player_pierde(player_hand, player_hand2, dealer_hand)
        #             break

        #     if player_hand.value and player_hand2.value <= 21:

        #         while dealer_hand.value < 17:
        #             tomar_carta(deck, dealer_hand)

        #         mostrar_todas_las_cartas2(player_hand, player_hand2, dealer_hand)

        #         if dealer_hand.value > 21:
        #             dealer_pierde(player_hand, player_hand2, dealer_hand)

        #         elif dealer_hand.value > player_hand.value:
        #             dealer_gana(player_hand, player_hand2, dealer_hand)

        #         elif dealer_hand.value < player_hand.value:
        #             player_gana(player_hand, player_hand2, dealer_hand)

        #         if player_hand.value > 21:
        #             player_pierde(player_hand, player_hand2, dealer_hand)

        # elif CantidadJugadores != 1 or 2: 
        #     print("Cantidad invalida")
    if NewGame == 'no':
        print("Menu inicial")
    
    new_game = input("\n¿Desea jugar otra partida? Escriba 's' o 'n': ")
    if new_game[0].lower() == 's':
        playing = True
        continue
    else:
        print("\n¡Gracias por jugar!")
        break