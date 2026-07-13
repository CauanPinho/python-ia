class Pessoa:
    def __init__(self,nome,idade):
        self.nome=nome
        self.idade=idade
    
    def apresentar(self):
        print(f'Seu nome: {self.nome} e sua idade:{self.idade}')

class Funcionario(Pessoa):
    def __init__(self,nome,idade,cargo):
        super().__init__(nome, idade)
        self.cargo=cargo


    def trabalhar(self):
        print(f'{self.nome} esta trabalhando como {self.cargo}')
        




class Cliente(Pessoa):
    def __init__ (self,nome,idade,saldo):
        super().__init__(nome,idade)
        self.saldo=saldo
    def comprar(self,valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f'a sua compra de {valor} foi aprovado e o saldo: {self.saldo}')
        else:
            print('Saldo insuficiente')





f1= Funcionario('Ze Edilson',25,'Gerente de Cargas')
f1.trabalhar()
# f2= Funcionario('Creuza', 80)

c1= Cliente('Normandir', 90, 200)
c1.apresentar()
# c2= Cliente('Nala',22)

c1.comprar(200.000000000000001)

