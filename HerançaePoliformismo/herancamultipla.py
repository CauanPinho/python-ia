#classe avo

class Animal:
    def __init__(self, nome):
        self.nome=nome
#classes pai
class Predador(Animal):
    def cacando(self):
        print(f'O animal {self.nome} esta cacando')

class Presa(Animal):
    def fugindo(self):
        print(f'O animal {self.nome} esta fugindo')

#classes filho

class Coelho(Presa):
    pass
    

class Tigre(Predador):
    pass

class Golfinho(Predador,Presa):
    pass

coelho1= Coelho('Bunny')

coelho1.fugindo()

tigre1= Tigre('Leo')

tigre1.cacando


golfinho1= Golfinho('Bylly')
golfinho1.fugindo()
