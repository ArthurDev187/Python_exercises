from datetime import date
class Person:
    def __init__(self, nome, idade, falando=False, comendo=False):
        self.nome = nome
        self.idade = idade
        self.falando = falando
        self.comendo = comendo
        # self.ano_nascimento = int(date.year) - int(self.idade)
    
    def comer(self, alimento):
        if self.falando:
            print(f'{self.nome} está falando, e não pode comer enquanto fala.')
            return

        if self.comendo:
            print(f'{self.nome}, já está comendo.')
            return
        
        print(f'{self.nome}, está comendo {alimento}')
        self.comendo = True

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} está comendo, e não pode falar enquanto come.')
            return

        if self.falando:
            print(f'{self.nome}, já está falando.')
            return
        
        print(f'{self.nome} está falando sobre {assunto}')
        self.falando = True