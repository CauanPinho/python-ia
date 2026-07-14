
class Cachorro:
    def emitir_som(self):
        print('au au au au ')


class Gato:
    def emitir_som(self):
        print('miuau miau ')


animais = [Cachorro(), Gato()]

for animal in animais:
    animal.emitir_som()

