from ficha import Ficha

nome_cliente = str(input("digite o seu nome: "))
salario = float(input("digite o seu salario: "))
valor_emprestimo = float(input("digite o valor do emprestimo: "))
parcelas = int(input("digite a suas parcelas: "))

percentual = 30/100.0
valor_parcelas = valor_emprestimo / parcelas
percentual_salario = salario *  percentual
salario_descontado = salario - percentual_salario


fichas = Ficha(nome_cliente,salario,valor_emprestimo,parcelas)



if  salario_descontado > valor_parcelas  :
    print("parabens "+ fichas.nome +" seu credito de " + fichas.valor_emprestimo + " foi aprovado")
else:
    print("desculpe "+ fichas.nome + "mas seu credito não foi aprovado devido ao seu salario de "+ fichas.salario_cliente +"e o valor do emprestimo"+ fichas.valor_emprestimo +"não foi possivel realizar tente novamente")


