# Var = input("Message to the user")

Name = input("Please enter your name: ")
print(Name)

Age = int(input("Please enter your age: "))
print(str(Age) + "1")

Scores = []

for i in range(5):
  currentScore = int(input("Please enter the score " + str(i) + ": "))
  Scores.append(currentScore)
  print("The score you entered was:\n", currentScore)
  
print(Scores)