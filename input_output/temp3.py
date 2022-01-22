# | |  0
#----- 1
# | |  2
#----- 3
# | |  4
#01234

def drawField():
  for row in range(5):
    if row % 2 == 0:
      for column in range(5):
        if column % 2 == 0:
          print(" ", end = "")
        else:
          print("|", end = "")
    else:
      print("-----")

Player = 1
currentField = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

while(True):
  print("Players turn:", Player)
  MoveRow = int(input("Please enter the row"))
  MoveColumn = int(input("Please enter the column"))
  if Player == 1:
    # Player 1
    currentField[MoveColumn][MoveRow] = "X"
    Player = 2
  else:
    # Player 2
    currentField[MoveColumn][MoveRow] = "O"
    Player = 1
