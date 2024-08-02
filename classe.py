class Animal():
    coracao:bool
    racional:bool
    def __init__(self, nome):
        self.nome = nome
        

class Humano(Animal):
    def __init__(self, nome, idade, sexo):
        super().__init__(nome)
        self.sexo = sexo
        self.idade = idade
        self.coracao = True
        self.racional = True

    # def ver_humano(self):
    #     print(f'\n{self.nome}')
    #     print(self.sexo)
    #     print(self.coracao)
    #     print(self.racional)

class Cachorro(Animal):
    def __init__(self, nome, raca, cor, tamanho, sexo):
        self.nome = nome
        self.raca = raca
        self.cor = cor
        self.tamanho = tamanho
        self.sexo = sexo
        self.coracao = True
        self.racional = False
    
    def latir(self):
        print('au-au')

    def comer(self):
        pass

    def passear(self):
        pass

    # def ver_cachorro(self):
    #     print(self.nome)
    #     print(self.raca)
    #     print(self.cor)
    #     print(self.tamanho)
    #     print(self.sexo)
    #     print(self.coracao)
    #     print(self.racional)