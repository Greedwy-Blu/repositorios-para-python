def valorPagamento(valor, diasAtraso):
    if diasAtraso == 0:
        return valor
    else:
        multa = valor * 0.03
        juros = valor * (0.001 * diasAtraso)
        return valor + multa + juros

totalPrestacoes = 0
valorTotal = 0

while True:
    valorPrestacao = float(input("Digite o valor da prestação (ou 0 para encerrar): "))
    if valorPrestacao == 0:
        break

    diasAtraso = int(input("Digite o número de dias em atraso: "))

    valorAPagar = valorPagamento(valorPrestacao, diasAtraso)
    totalPrestacoes += 1
    valorTotal += valorAPagar

    print("O valor a ser pago é: R$ {:.2f}".format(valorAPagar))

print("Relatório do dia:")
print("Quantidade de prestações pagas: ", totalPrestacoes)
print("Valor total de prestações pagas: R$ {:.2f}".format(valorTotal))
