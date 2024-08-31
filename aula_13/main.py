# loop control statements

# break
# continue
# pass

while True:
  name = input("Enter your name:")
  if name != "":
       break

phone_number = "16-434234423"

for i in phone_number:
  if i == "-":
    continue
print(i, end="")


for i in range(1, 21):
  if i == 13:
      pass
  else:
      print(i)