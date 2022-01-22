# | |  0
#----- 1
# | |  2
#----- 3
# | |  4
#01234

def drawField(field):
  for row in range(5): #0,1,2,3,4
    if row % 2 == 0:
      practicalRow = int(row / 2)
      for column in range(5): #0,1,2,3,4
        if column % 2 == 0:
          practicalColumn = int(column / 2)
          if column != 4:
            print(field[practicalColumn][practicalRow], end = "")
          else:
            print(field[practicalColumn][practicalRow])
        else:
          print("|", end = "")
    else:
      print("-----")

Player = 1
currentField = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
drawField(currentField)

while(True): #True == True
  print("Players turn:", Player)
  MoveRow = int(input("Please enter the row\n"))
  MoveColumn = int(input("Please enter the column\n"))
  if Player == 1:
    # Player 1
    if currentField[MoveColumn][MoveRow] == " ":
      currentField[MoveColumn][MoveRow] = "X"
      Player = 2
  else:
    # Player 2
    if currentField[MoveColumn][MoveRow] == " ":
      currentField[MoveColumn][MoveRow] = "O"
      Player = 1
  drawField(currentField)
