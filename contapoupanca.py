class ContaPoupanca:
    def _init_(self, titular, saldo_inicial=0, taxa_juros=0.05):
        self.titular = titular
        self.saldo = saldo_inicial
        self.taxa_juros = taxa_juros

    def depositar(self, valor):
        self.saldo += valor
        print(f'Depósito de {valor} realizado. Novo saldo: {self.saldo}')

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f'Saque de {valor} realizado. Novo saldo: {self.saldo}')
        else:
            print('Saldo insuficiente para saque.')

    def calcular_juros(self):
        juros = self.saldo * self.taxa_juros
        self.saldo += juros
        print(f'Juros calculados. Novo saldo: {self.saldo}')
