# while condition:
#    Action
#    Action2
#    Action3

KeepTrack = 1;
counter = 1
Sum = 0

while (KeepTrack <= 100):
    print(KeepTrack)
    # print(counter)
    Sum += KeepTrack
    # counter = counter + 1
    KeepTrack += 1

print(Sum)

Letters = ["a" , "b", "c", "d", "e"]

Index = 0
while (Index < len(Letters)):
    print(Index)
    print(Letters[Index])
    Index += 1
    
height = 5000
velocity = 50
time = 0
while (height > 0):
    height -= velocity
    time += 1
    
print(height)
print(time)