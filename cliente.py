class Cliente:
    def __init__ (self, nome, cpf, contas):
        self.nome = nome
        self.cpf = cpf
        self.contas = contas
        
    def registrar_conta (self):
        return self.contas.append(self.contas)