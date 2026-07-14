#Problema de quando a classe so existe em um contexto, e nao no global


class Computador():
    def __init__(self,modelo,gpu_nome, gpu_memoria):
        self.modelo= modelo
        self.gpu_nome = gpu_nome
        self.GPU=self.GPU(gpu_memoria, gpu_memoria)

    def mostrar_conf(self):
        print(f'Computador: {self.modelo}')

    class GPU: #classe aninhada
        def __init__ (self,nome,memoria_gb):
            self.nome= nome
            self.memoria_gb = memoria_gb

        def mostrar_gpu(self):
            print(f' GPU: {self.nome} - {self.memoria_gb}')


#utilização


pc1= Computador('Dell xps','nvidiard1',24)




pc1.mostrar_conf()
