
i = 0
numbers = []
while i < 10:
     numbers.insert(i, int(input("digite um numero: ")))
     i+=1

i=9
while i < len(numbers):
   total = sum(numbers)
   media = total/10
   print("soma:", total)
   print("media", media)
   print(max(int(value) for value in numbers))
   print(min(int(value) for value in numbers))
   i+=1



