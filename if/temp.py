# if condition:
#  Action

click = False

Like = 0

click = True

if click == True:
    Like = Like + 1
    click = False

print(Like)

Temperature = 20
Thermo = 15

if Temperature < 15:
    Thermo = Thermo + 5

print(Thermo)

Time = "Day"
Sleepy = False
Pajamas = "Off"

if Time == "Night" and Sleepy == True:
    Pajamas = "On"
elif Time == "Morning":
    Pajamas = "On"
else:
    Pajamas = "Off"
