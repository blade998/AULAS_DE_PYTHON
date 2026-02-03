class ContaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

    def mostrar_saldo(self):
        print(self.saldo)

        


conta = ContaBancaria(100)        
conta.depositar(50)
conta.sacar(30)
conta.mostrar_saldo()