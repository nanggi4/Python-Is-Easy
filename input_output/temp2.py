# File = open("Filename", "r") # "r", "w", "a", "r+" -> read and write
# File.close()

VacationSpots = ["London", "Paris", "New York", "Utah", "Iceland"]
VacationFile = open("VacationPlaces", "w")

for Spots in VacationSpots:
  VacationFile.write(Spots)

VacationFile.close()

VacationFile = open("VactionPlaces", "r")

FirstLine = VacationFile.readline()
print(FirstLine)
for line in VacationFile:
  print(line, end = "")

# TheWholeFile = VacationFile.read()
# print(TheWholeFile)

VacationFile.close()