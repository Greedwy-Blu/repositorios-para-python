nota1 = float(input("digite a nota1: "))
nota2 = float(input("digite a nota2: "))
nota3 = float(input("digite a nota3: "))
mediaExercicios = float(input("digite a sua media nos exercicios: "))

media = (nota1+nota2*2+nota3*3+mediaExercicios)/7

if media >= 9:
    print("A")
    print("a sua media foi de", media)
elif media >= 7.5  and media <= 9:
   print("B")
   print("a sua media foi de", media)
elif media>=6 and media <= 7.5:
   print("C")
   print("a sua media foi de", media)
elif media>=4 and media <= 6:
   print("D")
   print("a sua media foi de", media)
elif media <4:
   print("E")
   print("a sua media foi de", media)

