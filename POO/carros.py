class Carro:
    def __init__(self,cor,ano,ligado):
        self.cor=cor
        self.ano=ano
        self.ligado=True
        self.seta= None
    
    def informacoes(self):
        print(f" A cor do carro e {self.cor}")  
        print(f"O ano do carro e {self.ano}")
    
    def ligar_self(self):
        if not self.ligado:
            self.ligado=True
            print("O carro ja está ligado")
        else:
            print("O carro está desligado")
    
    def desligar(self):
        if self.ligado:
            self.ligado=False
            print("O carro está desligado")
        else:
            print("O carro já está desligado")
    def ligarSeta(self,direcao):
        self.seta= direcao
        print(f"A seta do carro está ligada para a {self.seta}")

    
carro1 = Carro('Azul', 2020,True)
carro1.ligarSeta('direita')
carro1.informacoes()
carro1.ligar_self()