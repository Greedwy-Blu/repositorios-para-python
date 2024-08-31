print("escolha a sua operação \n")
print("1 - somar")
print("2 - mutiplicar")
print("3 - dividir")
print("4 - subtrair")

menu = int(input("escolha um operação: "))

valor1 = int(input("digite o valor 1: "))
valor2 = int(input("digite o valor 2: "))


def somar(valor1, valor2):
   print(valor1+valor2)

def mutiplicar(valor1, valor2):
   print(valor1*valor2)

def dividir(valor1, valor2):
   print(valor1/valor2)


def subtrair(valor1, valor2):
   print(valor1-valor2)





if menu == 1:
    somar(valor1, valor2)

elif  menu == 2:
   mutiplicar(valor1, valor2)
elif  menu == 3:
  dividir(valor1, valor2)
elif  menu == 4:
   subtrair(valor1, valor2)
else:
   print("nenhuma das operação foi selecionado")