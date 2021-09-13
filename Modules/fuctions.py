from os import system
from Modules.db import *
import Modules.menu
import re


class Colors:
    white = '\033[37m'
    red = '\033[31m'
    green = '\033[32m'
    blue = '\033[34m'
    ciano = '\033[36m'
    magenta = '\033[35m'
    yellow = '\033[33m'
    reset = '\033[0;0m'
    negrito = '\033[1m'


class Functions(Colors):
    def __init__(self):
        self.menu = Modules.menu.Menu()
        db = 'banco_de_dados.db'
        self.database = BancoDeDados(db)

    def add(self):
        system('cls')
        self.menu.titulo('CADASTRAR NOVO CONTATO')
        print('Digite o Nome do Contato')
        nome = self.checkname()
        print('Digite o Email do Contato')
        email = self.checkmail()
        print('Digite o Telefone do Contato')
        telefone = self.checkfone()
        self.database.adddata(nome, email, telefone)
        print('Contato Adicionado Com Sucesso')
        data = self.database.searchdata(email)
        self.printdata(data)
        while True:
            opcao = self.menu.vertical(
                ['ADICIONAR NOVO CONTATO', 'MENU PRINCIPAL', 'SAIR'])
            if opcao == 1:
                self.add()
                break
            elif opcao == 2:
                break
            elif opcao == 3:
                exit()
            else:
                print('Digite uma Opção Válida')

    def search(self):
        system('cls')
        self.menu.titulo('PESQUISAR CONTATO')
        data = None
        while not data:
            term_search = input('Digite o Nome, Email ou Telefone que Deseja Pesquisar: ')
            data = self.database.searchdata(term_search)
            if not data:
                print(f'Não Foi Encontrado Nenhum Contato\nVerifique o Termo Buscado é Tente Novamente.')
        self.printdata(data)
        while True:
            opcao = self.menu.vertical(
                ['FAZER NOVA BUSCA', 'MENU PRINCIPAL', 'SAIR'])
            if opcao == 1:
                self.search()
                break
            elif opcao == 2:
                break
            elif opcao == 3:
                exit()
            else:
                print('Digite uma Opção Válida')

    def edit(self):
        system('cls')
        self.menu.titulo('EDITAR CONTATO')
        data = ''
        while not data:
            email = input('Digite o email do contato: ')
            data = self.database.searchdeletedata(email)
            print(f'Não Foi Encontrado Nenhum Contato\nVerifique o Termo Buscado é Tente Novamente.')

        system('cls')
        self.menu.titulo('EDITAR CONTATO')
        print('\nContato Encontrado')
        self.printdata(data)
        opcao = self.menu.vertical(
            ['EDITAR TUDO', 'EDITAR NOME', 'EDITAR EMAIL', 'EDITAR TELEFONE', 'CANCELAR', 'SAIR'])
        # Editar todos os Dados
        if opcao == 1:
            print('Digite o Novo Nome do Contato')
            nome = self.checkname()
            print('Digite o Novo Email do Contato')
            newemail = self.checkmail()
            print('Digite o Novo Telefone do Contato')
            telefone = self.checkfone()
            data = self.database.editdata('all', nome=nome, email=email,
                                          newemail=newemail, telefone=telefone)
            self.printdata(data)
        # Editar Nome
        elif opcao == 2:
            print('Digite o Novo Nome do Contato')
            nome = self.checkname()
            data = self.database.editdata('nome', nome=nome, email=email)
        # Editar Email
        elif opcao == 3:
            print('Digite o Novo Email do Contato')
            newemail = self.checkmail()
            data = self.database.editdata('email', email=email, newemail=newemail)
        # Editar Telefone
        elif opcao == 4:
            print('Digite o Novo Telefone do Contato')
            telefone = self.checkfone()
            data = self.database.editdata('telefone', email=email, telefone=telefone)
        elif opcao == 5:
            self.edit()
        elif opcao == 6:
          exit()
        else:
            print('Digite uma Opção Válida')
            system('pause')

        system('cls')
        self.menu.titulo('EDITAR CONTATO')
        print('Contato Editado com Sucesso')
        self.printdata(data)
        while True:
            opcao = self.menu.vertical(
                ['EDITAR OUTRO CONTATO', 'MENU PRINCIPAL', 'SAIR'])
            if opcao == 1:
                self.edit()
                break
            elif opcao == 2:
                break
            elif opcao == 3:
                exit()
            else:
                print('Digite uma Opção Válida')
                system('pause')

    def delete(self):
        data = ''
        system('cls')
        self.menu.titulo('EXCLUIR CONTATO')
        while not data:
            email = input('Digite o email do contato: ')
            data = self.database.searchdeletedata(email)
            print(f'Não Foi Encontrado Nenhum Contato\nVerifique o Termo Buscado é Tente Novamente.')
        system('cls')
        self.menu.titulo('EXCLUIR CONTATO')
        print('\nContato Encontrado')
        self.printdata(data)
        opcao = self.menu.vertical(
            ['EXCLUIR CONTATO', 'CANCELAR', 'SAIR'])
        if opcao == 1:
            self.database.deletedata(email)
        elif opcao == 2:
            self.delete()
        elif opcao == 3:
            exit()
        else:
            print('Digite uma Opção Válida')
            system('pause')
        system('cls')
        self.menu.titulo('EXCLUIR CONTATO')
        print('Contato Excluído Com Sucesso')
        while True:
            opcao = self.menu.vertical(
                ['EXCLUIR OUTRO CONTATO', 'MENU PRINCIPAL', 'SAIR'])
            if opcao == 1:
                self.delete()
                break
            elif opcao == 2:
                break
            elif opcao == 3:
                exit()
            else:
                print('Digite uma Opção Válida')
                system('pause')

    def listall(self):
        while True:
            system('cls')
            self.menu.titulo('LISTA DE CONTATOS')
            data = self.database.listdata()
            if data:
                self.printdata(data)

            opcao = self.menu.vertical(
                ['MENU PRINCIPAL', 'SAIR'])
            if opcao == 1:
                break
            elif opcao == 2:
                exit()
            else:
                print('Digite uma Opção Válida')
                system('pause')

    def printdata(self, data):
        linha = ('*' + ('-' * 10))
        linha1 = ('*' + ('-' * 28))
        print(f"{self.negrito}{linha}{linha1 * 3}*{self.reset}")
        print(f"{self.negrito}|{self.reset}{self.green}{'INDEX'.center(10)}{self.reset}"
              f"{self.negrito}|{self.reset}{self.green}{'NOME'.center(28)}{self.reset}"
              f"{self.negrito}|{self.reset}{self.green}{'EMAIL'.center(28)}{self.reset}"
              f"{self.negrito}|{self.reset}{self.green}{'TELEFONE'.center(28)}{self.reset}{self.negrito}"
              f"|{self.reset}")
        print(f"{self.negrito}{linha}{linha1 * 3}*{self.reset}")
        for index, nome, email, telefone in data:
            print(f"{self.negrito}|{self.reset}{self.ciano}{str(index).center(10)}{self.reset}"
                  f"{self.negrito}|{self.reset}{self.blue}{str(nome).center(28)}{self.reset}"
                  f"{self.negrito}|{self.reset}{self.yellow}{str(email).center(28)}{self.reset}"
                  f"{self.negrito}|{self.reset}{self.magenta}{str(telefone).center(28)}{self.reset}{self.negrito}"
                  f"|{self.reset}")
        print(f"{self.negrito}{linha}{linha1 * 3}*{self.reset}")

    def checkname(self):
        while True:
            name = str(input('Nome: '))
            fullname = name.split(' ')
            data = self.database.searchdata(name)

            if name == '':
                print('Nome Vazio Digitado')
            elif not re.match(r"^[^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{2,}$", name):
                print('Digite um Nome Completo Válido')

            elif len(fullname) < 2:
                print('Digite um Nome Completo Válido')

            elif data:
                print("Esse Nome já Está Cadastrado")

            else:
                return name
                break

    def checkmail(self):
        while True:
            mail = str(input('Email: '))
            data = self.database.searchdata(mail)

            if mail == '':
                print('Email Vazio Digitado')
            elif not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', mail):
                print("Por Favor Digite um Email Válido")
            elif data:
                print("Esse email já Está Cadastrado")
            else:
                return mail
                break

    def checkfone(self):
        while True:
            fone = input('Telefone: ')
            data = self.database.searchdata(fone)
            """Regex para verificação se o número de telefone é válido
            if not re.match(r'^(\(?\d{2}\)?)?\s?\d{4,5}-?\d{4,5}', telefone):
            Reduzi o numero de opções para aceitar apenas com ddd + numero
            exemplos de entradas válidas:
            91 999999999 or  91999999999 or 999999999"""

            if fone == '':
                print('Telefone Vazio Digitado')
            if not re.match(r'^(\d{2})?\s?\d{4,5}\d{4,5}', fone):
                print('Por Favor, Digite um Número de Telefone Válido')
            elif data:
                print("Esse Telefone já Está Cadastrado")
            else:
                return fone
                break
