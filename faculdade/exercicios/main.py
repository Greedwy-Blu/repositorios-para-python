nota1 = int(input("digite a nota1: "))
nota2 = int(input("digite a nota2: "))
nota3 = int(input("digite a nota3: "))

media = (nota1+nota2+nota3)/3

if media<=6 and media>=4:
    print("recuperação")
    print("a sua media foi de", media)
elif media<=4:
   print("reprovou")
   print("a sua media foi de", media)
elif media>=6:
   print("passou")
   print("a sua media foi de", media)

