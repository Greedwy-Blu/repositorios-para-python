# nested loops = the "inner loop" will finish all of it s iteration

# finishing one iteration of tje "outer loop"


rows = int(input("hows many rows?: "))

columns = int(input("how many colums"))

symbol = input("Enter a sysmbol to use: ")

for i in range(rows):
  for j in range(columns):
    print(symbol, end="")
  print()
