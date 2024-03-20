class Conta:
    def __init__ (self, numero, saldo: float, transacao):
        self.numero = numero
        self.saldo = 0
        transacao = []
        self.transacao = transacao

    def sacar(self, quanti):
        quanti = int(input("Quanto que você deseja sacar? "))
        self.saldo = (self.saldo - quanti)
        print (f"Sua conta agora possui {self.saldo} reais. ")
        self.transacao.append(f'Saque de {self.saldo} reais.'  )
        return self.saldo
    
    def depositar(self, quanti):
        quanti = int(input("Quanto você deseja depositar? "))
        self.saldo = (self.saldo + quanti)
        self.transacao.append(f'Deposito de {self.saldo} reais. ')
        print (f"Sua conta agora possui {self.saldo} reais. ")
        return self.saldo
    
    def registrar_trans(self, trans):
        trans.append(self.transacao)

    def exibir_e(self):
        print (self.transacao)