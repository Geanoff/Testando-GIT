from classe import *
from views import *
from menus import *

lista_humano = []
lista_cao = []

def criar_cachorro():
    limpar()
    nome = input('Qual o nome do Cachorro: ')
    raca = input('Raça: ')
    cor = input('Cor: ')
    tamanho = input('Tamanho: ')
    sexo = input('Sexo: ')
    cao = Cachorro(nome, raca, cor, tamanho, sexo)
    lista_cao.append(cao)
    limpar()
    print('-> Cachorro Criado!')
    

def criar_humano():
    limpar()
    nome = input('Qual o nome do Humano: ')
    idade = input('Idade: ')
    sexo = input('Sexo: ')
    humano = Humano(nome, idade, sexo)
    lista_humano.append(humano)
    limpar()
    print('-> Humano Criado!')
    
while True:
    op = main_menu()
    if op == 1:
        criar_cachorro()

    elif op == 2:
        criar_humano()

    elif op == 3:
        listar_dog(lista_cao)
        # sub = sub_dog()
        # if not sub:
        #     pass
        # else:
        #     dados_dog(sub)
        
    elif op == 4:
        listar_humano(lista_humano)

    elif op == 0:
        limpar()
        print('-> Saindo do sistema...')
        break

    else:
        limpar()
        print('-> Opção Inválida')

# while True:
#     menu_principal()
#     op = int(input('Escolha uma opção: '))