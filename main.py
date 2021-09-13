from Modules.menu import *
from Modules.fuctions import *

menu = Menu()
fuctions = Functions()
colors = Colors()


def main():
    while True:
        system('cls')
        menu.titulo('Lista Telefônica')
        opcao = menu.horizontal(
            ['Cadastrar Novo Contato', 'Buscar Contato', 'Editar Contato', 'Excluir Contato', 'Listar Contatos',
             'Sair'])

        if opcao == 1:
            fuctions.add()
        elif opcao == 2:
            fuctions.search()
        elif opcao == 3:
            fuctions.edit()
        elif opcao == 4:
            fuctions.delete()
        elif opcao == 5:
            fuctions.listall()
        elif opcao == 6:
            exit()
        else:
            print('A Opção Digitada é Inválida')


if __name__ == "__main__":
    main()
