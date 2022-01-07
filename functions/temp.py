# def FunctionName(Input):
#   Action
#   return Outut

def addOne(Number):
  Output = Number + 1
  return Output

Var = 0
Var2 = addOne(Var);

# 1
print(Var2);

def addOneAddTwo(NumberOne, NumberTwo):
  Output = NumberOne + 1
  Output += NumberTwo + 2
  return Output

Sum = addOneAddTwo(1, 2);

# 6
print(Sum);
