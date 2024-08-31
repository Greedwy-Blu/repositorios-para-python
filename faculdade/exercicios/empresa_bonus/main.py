anos_na_empresa = int(input("digite o anos trabalhados na empresa: "))
salario = float(input("digite o seu salario ganho: "))


if anos_na_empresa > 5 :
    percentual = 30/100.0
    aumento = percentual * salario
    novo_salario = salario + aumento

    print('Aumento: R$ ',aumento)
    print('Novo salário: R$ ', novo_salario)

elif anos_na_empresa  == 5 :
    percentual = 20/100.0
    aumento = percentual * salario
    novo_salario = salario + aumento

    print('Aumento: R$ ',aumento)
    print('Novo salário: R$ ', novo_salario)
else:
    percentual = 10/100.0
    aumento = percentual * salario
    novo_salario = salario + aumento

    print('Aumento: R$ ',aumento)
    print('Novo salário: R$ ', novo_salario)


