from poo_heranca_e_polimorfismo.carro import Carro

class CarroCorrida(Carro):
    def __init__(self, velocidade_inicial):
        super().__init__(velocidade_inicial)

    def acelerar(self):
        self.velocidade += 5
        print("Aceleraçâo de corrida! a velocidade aumentou em 5 km/h ")