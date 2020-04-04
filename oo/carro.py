class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1
        print(self.velocidade)

    def frear(self):
        self.velocidade -= 2
        self.velocidade =max(0, self.velocidade)
        print(self.velocidade)


NORTE='Norte'
LESTE='Leste'
SUL='Sul'
OESTE='Oeste'

class Direcao:
    rotacao_direita={
        NORTE:LESTE,
        LESTE:SUL,
        SUL:OESTE,
        OESTE:NORTE
    }
    rotacao_esquerda={
        NORTE:OESTE,
        OESTE:SUL,
        SUL:LESTE,
        LESTE:NORTE

    }
    def __init__(self):
        self.valor = NORTE
    def virar_direita(self):
        self.valor = self.rotacao_direita[self.valor]

    def virar_esquerda(self):
        self.valor = self.rotacao_esquerda[self.valor]
class Carro:
    def __init__(self, motor,direcao):
        self.motor = motor
        self.direcao = direcao
    def calcular_velocidade(self):
        return self.motor.velocidade
    def acelerar(self):
        self.motor.acelerar()
    def frear(self):
        self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor
    def girar_direita(self):
        self.direcao.virar_direita()
    def girar_esquerda(self):
        self.direcao.virar_esquerda()




