class Motor:
    def __init__(self,marca,potencia):
        self.marca=marca
        self.potencia=potencia



class Carro:
    def __init__(self):
        self.motores=[]

    def adicionar_motor(self,motor):
        self.motores.append(motor)


    def listar_motores(self):
        for motor in self.motores:
            print(f'Marca {motor.marca} - {motor.potencia}')

#criando os motores

motor_v6= Motor('Ford',300)


#criar o carro e adicionar o motor a ele

carro1= Carro()
carro1.adicionar_motor(motor_v6)



#listar os motores

carro1.listar_motores()