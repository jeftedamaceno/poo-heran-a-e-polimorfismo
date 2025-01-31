class Carro:
    def __init__(self, velocidade_inicial):
        self.velocidade = velocidade_inicial

    def acelerar(self):
        self.velocidade +=1

    def freia(self):
        self.velocidade -=1

    def exibe_velocidade(self):
        return print(f"velocidade atual: {self.velocidade} km/h")