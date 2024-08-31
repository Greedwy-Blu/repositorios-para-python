numero = int(input("digite um numero inteiro: "))

def fatorial(numero):
    resultado = 1
    while(numero > 1):
      resultado *= numero
      numero -= 1
    return resultado

n = fatorial(numero)
print(n)


