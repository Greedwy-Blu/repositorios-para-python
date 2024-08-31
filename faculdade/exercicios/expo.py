numero = int(input("digite um numero inteiro:"))



def expo(numero):




   array_digito = [int(n) for n in str(numero)]
   ler_digito = len(array_digito)
   narcis = sum(n **  ler_digito for n in array_digito)

   if numero == narcis  :
      print("numero é narcisista")
   else:
      print("não é narcisista")



y = expo(numero)
print(y)
