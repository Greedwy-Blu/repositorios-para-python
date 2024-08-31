preco_atual = float(input("digite o preço do produto"))
inflacao = float(input("digite a inflacao do ano"))

valor_aumento = preco_atual * (inflacao / 100)
preco_corrigido = preco_atual + valor_aumento


print("O valor de aumento do produto é: R$", valor_aumento)
print("O valor corrigido do produto é: R$", preco_corrigido)
