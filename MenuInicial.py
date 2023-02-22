import Cards

# class Menu_Inicial:
#     def __init__(self, usuario, juego, estadisticas, salir)
#     self.usuario = usuario
#     self.juego = juego_nuevo
#     self.estadisticas = estadisticas 
#     self.salir = salir


class Card:
    def __init__(self, numero, simbolo):
        self.numero = Cards.numero
        self.simbolo = Cards.simbolo

    def print_card(self):
        print(f"El numero de la carta es {self.numero} y el simbolo es {self.simbolo}")