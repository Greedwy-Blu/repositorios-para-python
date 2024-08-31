# logical operators

temp = int(input("What in the temperature outside?: "))

if temp >= 0  and temp <= 30:
   print("ok")
elif temp < 0 or temp > 30:
   print("not good")