Word = "Hello"

Letters = []

# for w in Word:
#     print(w)
#     if w == "e":
#        print("What a funny letter")

for w in Word:
    Letters.append(w)

# print(Letters)

# for l in Letters:
# print(l)

Numbers = [1, 2, 3, 4, 5]

for l in Numbers:
    if l % 2 == 1:
        print(l)

for num in range(1, 10, 2):
    Numbers.append(num)
    print(num)


print(Numbers)
