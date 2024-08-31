def hash_password(password):
    hash_val = 0
    for char in password:
        hash_val += ord(char)
    return str(hash_val)

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class ContaBancaria:
    def __init__(self, numero_conta, cliente, saldo_inicial=0.0):
        self.numero_conta = numero_conta
        self.cliente = cliente
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso. Novo saldo: R${self.saldo:.2f}")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso. Novo saldo: R${self.saldo:.2f}")
        elif valor > self.saldo:
            print("Saldo insuficiente para o saque.")
        else:
            print("O valor do saque deve ser positivo.")

    def transferir(self, valor, conta_destino):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            conta_destino.depositar(valor)
            print(f"Transferência de R${valor:.2f} para a conta {conta_destino.numero_conta} realizada com sucesso.")
        elif valor > self.saldo:
            print("Saldo insuficiente para a transferência.")
        else:
            print("O valor da transferência deve ser positivo.")

    def extrato(self):
        print(f"Extrato da conta {self.numero_conta} - Saldo atual: R${self.saldo:.2f}")

class SistemaBancario:
    def __init__(self):
        self.contas = {}
        self.usuarios = {}

    def criar_conta(self, numero_conta, nome_cliente, cpf_cliente, senha):
        if numero_conta in self.contas:
            print("Número da conta já existe.")
        else:
            cliente = Cliente(nome_cliente, cpf_cliente)
            conta = ContaBancaria(numero_conta, cliente)
            self.contas[numero_conta] = {'conta': conta, 'senha': hash_password(senha)}
            print(f"Conta {numero_conta} criada com sucesso para {nome_cliente}.")

    def autenticar(self, numero_conta, senha):
        if numero_conta in self.contas:
            return self.contas[numero_conta]['senha'] == hash_password(senha)
        return False

    def visualizar_conta(self, numero_conta, senha):
        if self.autenticar(numero_conta, senha):
            self.contas[numero_conta]['conta'].extrato()
        else:
            print("Autenticação falhou. Verifique o número da conta e a senha.")

sistema = SistemaBancario()
sistema.criar_conta("12345", "João Silva", "12345678900", "senha123")
sistema.criar_conta("67890", "Maria Oliveira", "09876543211", "senha456")

numero_conta = "12345"
senha = "senha123"
if sistema.autenticar(numero_conta, senha):
    conta1 = sistema.contas[numero_conta]['conta']
    conta1.depositar(500)
    conta1.sacar(100)
    sistema.visualizar_conta(numero_conta, senha)

    conta2 = sistema.contas["67890"]['conta']
    conta1.transferir(200, conta2)
    sistema.visualizar_conta(numero_conta, senha)
    sistema.visualizar_conta("67890", "senha456")
else:
    print("Falha na autenticação. Verifique o número da conta e a senha.")
