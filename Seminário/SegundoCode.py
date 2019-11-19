
class Animal(object):
    def __init__(self, r, ev):
        self.raca = r
        self.expectativaVida = ev

    def fala(self):
        return ''

class Cachorro(Animal):
    def __init__(self, r, ev, cpelo):
        super().__init__(r, ev)
        self.corPelo = cpelo
        print(f'Raça {self.raca}\nExpectativa de vida {self.expectativaVida} anos\ncor do pelo {cpelo}\n')
    
    def fala():
        return print('o cachorro faz AuAu')
            
class Baleia(Animal):
    def __init__(self, r, ev, cpele):
        super().__init__(r, ev)
        self.corPele = cpele
        print(f'Raça {self.raca}\nExpectativa de vida {self.expectativaVida} anos\ncor da pele {cpele}\n')

    def fala():
        return print('A baleia faz Woooooooooooouh')

class Pato(Animal):
    def __init__(self, r, ev, cpena):
        super().__init__(r, ev)
        self.corPena = cpena
        print(f'Raça {self.raca}\nExpectativa de vida {self.expectativaVida} anos\ncor das penas {cpena}')

    def fala():
        return print('O pato faz Quack-Quack')

Poodle = Cachorro.fala()
Orca = Baleia.fala()
Pato = Pato.fala()