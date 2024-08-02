import os

def main_menu():
    op = int(input('\n1 - Criar Cachorro\n2 - Criar Humano\n\n3 - Listar Cachorro\n4 - Listar Humano\n\n0 - Sair\n\nEscolha uma opção: '))
    return op

def listar_dog(lista):
    limpar()
    print('LISTA DE CACHORROS: ')
    c = 1
    for i in lista:
        print(f'{c} - {i.nome}')
        c += 1
    opc = sub_dog()
    if opc:
        print(f'Nome: {lista[opc-1].nome}')
        print(f'Raça: {lista[opc-1].raca}')
        print(f'Cor: {lista[opc-1].cor}')
        print(f'Tamanho: {lista[opc-1].tamanho}')
        print(f'Sexo: {lista[opc-1].sexo}')
    else: 
        pass


def listar_humano(lista):
    limpar()
    print('LISTA DE HUMANOS: ')
    for i in lista:
        print(f'- {i.nome}')

def limpar():
     os.system('cls')

def sub_dog():
     op = int(input('\n1 - Escolher um\n2 - Voltar\n\nDigite uma opção: '))
     if op == 1:
         sub = int(input('Qual Cachorro: '))
         return sub
     else:
         return None
     
def dados_dog(a):
    b = listar_dog()
    print(b)
    for i in b:
        print(i.raca)