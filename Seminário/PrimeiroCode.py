
class Animal(object):
    def __init__(self, r, ev):
        self.raca = r
        self.expectativaVida = ev

class Cachorro(Animal):
    def __init__(self, r, ev, cpelo):
        super().__init__(r, ev)
        self.corPelo = cpelo
        print(f'Raça {self.raca}\nExpectativa de vida {self.expectativaVida} anos\ncor do pelo {cpelo}\n')
            
class Baleia(Animal):
    def __init__(self, r, ev, cpele):
        super().__init__(r, ev)
        self.corPele = cpele
        print(f'Raça {self.raca}\nExpectativa de vida {self.expectativaVida} anos\ncor da pele {cpele}\n')

class Pato(Animal):
    def __init__(self, r, ev, cpena):
        super().__init__(r, ev)
        self.corPena = cpena
        print(f'Raça {self.raca}\nExpectativa de vida {self.expectativaVida} anos\ncor das penas {cpena}')

Poodle = Cachorro('Poodle', 13, 'Branco')
Orca = Baleia('Orca', 30, 'Branco e Preto')
PatoReal = Pato('Pato-Real', 10, 'Marrom')