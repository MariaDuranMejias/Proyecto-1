import Cards

numero = Cards.numero
def Deck():
    deck = []
    if numero == "A" : 
        NewValue = 1
        deck.append(NewValue)
        
    elif numero == 'J':
        NewValue = 10
        deck.append(NewValue)
        
    elif numero == "Q":
        NewValue = 10
        deck.append(NewValue)
        
    elif numero == "K":
        NewValue = 10
        deck.append(NewValue)
        
    else:
        deck.append(numero)
    print(deck)
    return deck

Deck()