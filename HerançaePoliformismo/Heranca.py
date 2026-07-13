class Animal:
    def __init__ (self,nome,cor,especie):
        self.nome=nome
        self.cor=cor
        self.especie=especie
    
    def apresentar(self):
        print(f'Eu sou o {self.especie} chamado {self.nome}')


class Gato(Animal):
    def emitir_som(self):
        print(f"MIAU")
    pass


class Cachorro(Animal):
    pass
class Elefante(Animal):
    pass


Gato1 = Gato('Felix','Branco','Siamese')
Cachorro1= Cachorro('Robert','Russo','Alemao')
Elefante1 = Elefante('Jordan','Azul','Cistoide')
Gato1.emitir_som()

Gato1.apresentar()
Cachorro1.apresentar()
Elefante1.apresentar()