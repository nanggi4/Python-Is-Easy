BlackShoese = {42:2, 41:3, 40:4, 39:1, 38: 0}

while(True):
  purchaseSize = int(input("Which shoe size would you like to buy?\n"))
  if purchaseSize < 0:
    break
  if BlackShoese[purchaseSize] > 0: 
    BlackShoese[purchaseSize] -= 1
  else:
    print("Shoes are no longer in stock")  
  print(BlackShoese)
  