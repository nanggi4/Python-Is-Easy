from re import L


Length = 10
ToPrint = "b"

for pos in range(1, Length+1):
  print(ToPrint*pos)

for pos in range(Length,0,-1):
  print(ToPrint*pos)