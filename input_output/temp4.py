ParticipantNumber = 5
participntData = []
registeredParticipants = 0
outputFile = open("ParticipantData.txt", "w")

while(registeredParticipants < ParticipantNumber): 
  tempPartData = [] #name, country of origin, age
  name = input("Please enter your name: ")
  tempPartData.append(name)
  country = input("Please enter your country of origin: ")
  tempPartData.append(country)
  age = int(input("Please enter your age: "))
  tempPartData.append(age)
  participntData.append(tempPartData)
  registeredParticipants += 1

for participant in registeredParticipants:
  for data in participant:
    outputFile.write(str(data))
    outputFile.write(" ")
  outputFile.write("\n")

outputFile.close()

inputFile = open("ParticipantData.txt", "r")

inputList = []

for line in inputFile:
  tempParticipant = line.strip().split()
  tempParticipant.append(line)
  
  

inputFile.close()