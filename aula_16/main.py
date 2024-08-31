# tuple = collection whicj in ordered an unchangeable
# used to group together related data

student = ("gabriel", 18 , "male")

print(student.count("gabriel"))
print(student.index("male"))

for x in student:
  print(x)

  if "gabriel" in student:
    print("gabriel is here")