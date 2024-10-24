from random import randint
from time import sleep
from typing import List

class Carro:
    identificacao = None
    velocidade = None
    quebrado = False

    def __init__(self, id, velocidade=0):
        self.id = id
        self.velocidade = velocidade

    def iniciar(self):
        print(f'{self.id} iniciou a corrida')

    def acelerar(self, quantidade):
        if not self.quebrado:
            self.velocidade += quantidade

    def parar(self):
        self.velocidade = 0
        self.quebrado = True

class Ferrari(Carro):
    def acelerar(self, quantidade):
        super().acelerar(quantidade * 1.1)


class Corrida:
    carros = None
    velocidades = []
    rodadas = None

    def __init__(self, carros:List[Carro], rodadas):
        self.carros = carros
        self.rodadas = rodadas
        for idx in range(len(self.carros)):
            self.velocidades.append(0)

    def largada(self):
        for carro in self.carros:
            carro.iniciar()

    def calculo_turno(self):
        for idx, carro in enumerate(self.carros):
            # Sorteio relativo a sair da corrida
            if (randint(0, 100) <= 2) and (not carro.quebrado):
                print(f'Grave acidente na pista, {carro.id} capotou 1000 vezes')
                carro.parar()
            
            # Sorteio de aceleração
            if (randint(0, 100) <= 50):
                carro.acelerar(randint(2, 7))

            self.velocidades[idx] += carro.velocidade

    def ranking(self):
        # Cria uma lista de tuplas do tipo:
        # [ (0, 25), (1, 10) ]
        novaLista = enumerate(self.velocidades)
        ordenada = sorted(novaLista, key=lambda carro: carro[1], reverse=True)
        
        print('Ranking:')
        posicao = 1
        for idx, velocidade in ordenada:
            print(f'{posicao}: {self.carros[idx].id} ({velocidade})')
            posicao+=1
    
    def corrida(self):
        for i in range(self.rodadas):
            self.calculo_turno()
        
        sleep(0.5)
        print('')
        self.ranking()

    def executar(self):
        self.largada()
        self.corrida()

carros = [
    Ferrari('Rubinho'),
    Carro('Rubinho'),
    Carro('João'),
    Carro('Maria'),
    Carro('José'),
    Carro('Marta'),
    Carro('Beatriz')
]

corrida = Corrida(carros, 16)
corrida.executar()