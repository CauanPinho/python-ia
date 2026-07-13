class Pessoa:
    def __init__(self,nome, idade,cargo):
        self.nome=nome
        self.idade=idade
        self.cargo=cargo
    def mostrarInformacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade:{self.idade}")
        print(f"Cargo: {self.cargo}")
    
    def promover(self,novo_cargo):
        print(f'{self.nome} foi promovida para o {novo_cargo}')
        self.cargo=novo_cargo
    
colaborador1= Pessoa("Ana",25,"Analista Senior")

colaborador2= Pessoa("Camile",30,"Junior plest")

colaborador3= Pessoa("Caps",45,"Gerente de projetos")

colaborador1.mostrarInformacoes()
# colaborador2.mostrarInformacoes()
# colaborador3.mostrarInformacoes()
colaborador1.promover('Assistente de chatice')
colaborador1.mostrarInformacoes()
