ParticipantNumber = 2
participantData = []
registeredParticipants = 0
outputFile = open("ParticipantData.txt", "w")

while(registeredParticipants < ParticipantNumber):
  tempPartData = [] # name, country of origin, age
  name = input("Please enter your name: ")
  tempPartData.append(name)
  country = input("Please enter your country of origin: ")
  tempPartData.append(country)
  age = str(input("Please enter your age: "))
  tempPartData.append(age)
  print(tempPartData)
  participantData.append(tempPartData)
  print(participantData) 
  registeredParticipants += 1

for participant in participantData:
  for data in participant:
    outputFile.write(str(data))
    outputFile.write(" ");
  outputFile.write("\n")
     
outputFile.close()

inputFile = open("ParticipantData.txt", "r")

inputList = []

for line in inputFile:
  tempParticipant = line.strip().split()
  print(tempParticipant)
  inputList.append(tempParticipant)
  print(inputList)

Age = {}
for part in inputList:
  tempAge = input(part[-1])
  if tempAge in Age:
    Age[tempAge] += 1
  else:
    Age[tempAge] = 1

print(Age)

Oldset = 0
Youngest = 100
mostOccuringAge = 0
counter = 0

for tempAge in Age:
  if tempAge>Oldset:
    Oldset = tempAge
  if tempAge<Youngest:
    Youngest = tempAge
  if Age[tempAge]>=counter:
    counter = Age[tempAge]
    mostOccuringAge = tempAge

print(Oldset)
print(Youngest)
print("Most occuring age is:", mostOccuringAge, "with", counter, "part")    
inputFile.close()