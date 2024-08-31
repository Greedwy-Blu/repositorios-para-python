altura = 5
for i in range(1, altura+1):
    # Imprimindo os espaços em branco antes dos números
    for j in range(altura-i):
        print(" ", end="")
    # Imprimindo os números da pirâmide
    for j in range(1, i+1):
        print(j, end="")
    # Imprimindo os números em ordem reversa para o reflexo
    for j in range(i-1, 0, -1):
        print(j, end="")
    # Imprimindo os espaços em branco após os números
    for j in range(altura-i):
        print(" ", end="")
    # Imprimindo a quebra de linha
    print()

# Imprimindo o reflexo da pirâmide
for i in range(altura, 0, -1):
    # Imprimindo os espaços em branco antes dos números
    for j in range(altura-i):
        print(" ", end="")
    # Imprimindo os números da pirâmide
    for j in range(1, i+1):
        print(j, end="")
    # Imprimindo os números em ordem reversa para o reflexo
    for j in range(i-1, 0, -1):
        print(j, end="")
    # Imprimindo os espaços em branco após os números
    for j in range(altura-i):
        print(" ", end="")
    # Imprimindo a quebra de linha
    print()