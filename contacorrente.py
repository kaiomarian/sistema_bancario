class contacorrente(Conta):
    def __init__(self, numero, saldo: float, transacao):
        super().__init__(numero, saldo, transacao)
        self.taxa_manutencao = 10.00
    
    def deduzir_taxa_manutencao(self):
        if self.saldo >= self.taxa_manutencao:
            self.saldo -= self.taxa_manutencao
            self.transacao.append(f'Taxa de manutenção de {self.taxa_manutencao} reais deduzida.')
            print(f"Taxa de manutenção de {self.taxa_manutencao} reais deduzida. Saldo restante: {self.saldo} reais.")
        else:
            print("Saldo insuficiente para dedução da taxa de manutenção.")

    def sacar(self, quanti):
        quanti = int(input("Quanto você deseja sacar? "))
        if self.saldo >= quanti:
            self.saldo -= quanti
            self.transacao.append(f'Saque de {quanti} reais.')
            print(f"Saque de {quanti} reais efetuado. Saldo restante: {self.saldo} reais.")
        else:
            print("Saldo insuficiente para saque.")

    def depositar(self, quanti):
        quanti = int(input("Quanto você deseja depositar? "))
        self.saldo += quanti
        self.transacao.append(f'Depósito de {quanti} reais.')
        print(f"Depósito de {quanti} reais efetuado. Saldo total: {self.saldo} reais.")