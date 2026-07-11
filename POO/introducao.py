class Casa:
    def __init__(self,cor,quartos,banheiros):
        self.cor=cor
        self.quartos=quartos
        self.banheiros=banheiros
    
    def mostrar_cor(self):
        print(f"A cor da casa e : {self.cor}")

    def mostrar_quartos(self):
        print(f"A quantidade de quartos dessa casa : {self.quartos}")
    def mostrar_banheiros(self):
        print(f"A quantidade de banheiros dessa casa : {self.banheiros}")

casa1=Casa("Azul", 3,10)
casa2=Casa("Vermelha", 2,100)


casa1.mostrar_cor()
casa2.mostrar_cor()
casa1.mostrar_quartos()
casa2.mostrar_quartos()
casa1.mostrar_banheiros()
casa2.mostrar_banheiros()
casa2.mostrar_quartos()