from random import shuffle

def createDeck():
  Deck = []
  
  faceValues = ["A", "J", "Q", "K"]
  for i in range(4):
    for card in range(2, 11):
      Deck.append(str(card))
      
    for card in faceValues:
      Deck.append(card)
  
  shuffle(Deck)
  return Deck

cardDeck = createDeck()

print(cardDeck)

class Player:
  def __init__(self):
    self.Hand = 
    self.score = 
    self.money
      