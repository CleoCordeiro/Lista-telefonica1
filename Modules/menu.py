import Modules.fuctions


class Menu:
    def __init__(self):
        self.colors = Modules.fuctions.Colors()

    @staticmethod
    def linha(tam=117):
        print('-' * tam)

    def titulo(self, txt):
        self.linha()
        print(f'{self.colors.green}{txt.center(117)}{self.colors.reset}')
        self.linha()

    def horizontal(self, menulist):
        c = 1
        for item in menulist:
            print(f"{self.colors.ciano}{c} - {item}{self.colors.reset}")
            c += 1
        self.linha()
        opcao = self.leiaint('Digite a Opção Desejada: ')
        return opcao

    def vertical(self, menulist):
        c = 1
        menu = ''
        for item in menulist:
            menu += f"[{c}] - {item}   "
            c += 1
        print('')
        print(f'{self.colors.ciano}{menu.center(80)}{self.colors.reset}')
        self.linha()
        opcao = self.leiaint('Digite a Opção Desejada: ')
        return opcao

    def leiaint(self, msg):
        while True:
            try:
                n = int(input(msg))
            except (ValueError, TypeError):
                print(f'{self.colors.red}ERRO: Por Favor, Digite um Número Inteiro Válido.{self.colors.reset}')
            else:
                return n
