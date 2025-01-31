
from carro_esportivo import CarroEsportivo
from carro_inteligente import CarroInteligente
from carro_corrida import CarroCorrida

def teste_drive(carro):
    print(f"\n testando carro{carro.__class__.__name__}.")
    carro.acelerar()
    carro.exibe_velocidade()    

if __name__ =="__main__":
    # carro intligente

    carro_inteligente = CarroInteligente(10)
    print("carro inteligente")
    carro_inteligente.acelerar()
    carro_inteligente.exibe_velocidade()
    carro_inteligente.estaciona()
    teste_drive(carro_inteligente)
    print()

    # carro esportivo
    carro_esportivo = CarroEsportivo(50)
    print("carro esportivo")
    carro_esportivo.turbo()
    carro_esportivo.exibe_velocidade()
    carro_esportivo.freia()
    carro_esportivo.exibe_velocidade()
    teste_drive(carro_esportivo)
    print()

    # carro corrida
    carro_corida = CarroCorrida(100)
    print("carro Corida")
    teste_drive(carro_corida)
    print()
