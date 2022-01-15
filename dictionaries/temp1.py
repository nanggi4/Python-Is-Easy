Sets = {"Element1", "Element2", "Element1", "Element4"}
print(Sets)
if "Element1" in Sets:
  print("Yes !")
  
CountryList = []
for i in range(5):
  Country = input("Please Enter Your Country: ")
  CountryList.append(Country)

CountrySet = set(CountryList)

print(CountryList)
print(CountrySet)

if "Brazil" in CountrySet:
  print("attended")

Dictionary = {}