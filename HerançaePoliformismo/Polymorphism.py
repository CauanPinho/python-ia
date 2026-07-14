#Polimorfismo

class Personagem():
    def falar(self):
        print('Eu sou um personagem')




class Guerreiro(Personagem):
    def falar(self):
        print('Eu sou um guerreiro forte e destemido')

class Mago(Personagem):
    def falar(self):
        print('Eu sou um mago bravoe e destemido')

class Arqueiro(Personagem):
    def falar(self):
        print('Eu sou um arqueiro forte e destemido')

#Cria os objetos

personagens = [Guerreiro(), Mago(), Arqueiro()]

for p in personagens:
    p.falar()