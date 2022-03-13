float("123.4") 
float("N/A")

keyWord = "Hello"

try:
  print(int(keyWord))
except Exception as e:
  print("Other type of exception")
  print(str(e))
finally:
  print("finally")

print("Past exception")