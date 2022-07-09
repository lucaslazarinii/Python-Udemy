from random import randint

class Pessoa:
    ano_atual = 2022
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
    def falar(self, assunto):
        if self.comendo:
            print(f"{self.nome} não pode falar sobre {assunto}, pois está comendo.")
            return
        if self.falando:
            print(f"{self.nome} já está falando.")
            return
        print(f"{self.nome} começou a falar de {assunto}.")
        self.falando = True

    def parar_falar(self):
        if self.falando:
            print(f"{self.nome} parou de falar.")
            self.falando = False
            return
        print(f"{self.nome} já está em silêncio!")

    def comer(self, alimento):
        if self.comendo:
            print(f"{self.nome} já está comendo.")
            return
        if self.falando:
            print(f"{self.nome} não pode comer {alimento} pois está falando.")
            return
        print(f"{self.nome} está comendo {alimento}.")
        self.comendo = True

    def parar_comer(self):
        if self.comendo:
            print(f"{self.nome} parou de comer.")
            self.comendo = False
            return
        print(f"{self.nome} não está comendo!")
    
    def ano_nascimento(self):
        return self.ano_atual - self.idade
    
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand

p3 = Pessoa.por_ano_nascimento("Rogério", 1972)
print(p3)
print(p3.nome, p3.idade)
print(p3.ano_nascimento())