#sistema de escola

class Escola():
    def __init__ (self,nome,idade):
        self.nome=nome
        self.idade=idade




class Aluno(Escola):
    def __init__(self, nome, idade, ano):
        super().__init__(nome,idade)
        self.ano= ano
    
class Professor(Escola):
    def __init__(self,nome,idade,materia):
        super().__init__(nome,idade)
        self.materia= materia


class Assistente(Escola):
    def __init__ (self,nome,idade,bloco):
        super().__init__(nome,idade)
        self.bloco = bloco 
a1=Aluno('marcos', 19, 8)

print(a1.nome)


print(a1.ano)