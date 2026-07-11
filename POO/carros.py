class Carro:
    def __init__(self,cor,ano,ligado):
        self.cor=cor
        self.ano=ano
        self.ligado=True
    
    def informacoes(self):
        print(f" A cor do carro e {self.cor}")  
        print(f"O ano do carro e {self.ano}")
    
    def ligar_sekf(self):
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


    
carro1 = Carro('Azul', 2020)

carro1.informacoes()
carro1.ligar()