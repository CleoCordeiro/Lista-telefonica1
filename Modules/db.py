import sqlite3
from sqlite3 import Error


class BancoDeDados:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS agenda (
                            nome TEXT NOT NULL UNIQUE,
                            email TEXT NOT NULL UNIQUE,
                            telefone INTEGER NOT NULL UNIQUE)""")

    def adddata(self, nome, email, telefone):
        try:
            self.cur.execute("INSERT INTO agenda (nome, email, telefone) VALUES(?, ?,?)", (nome, email, telefone))
            self.conn.commit()
        except Error as err:
            if 'UNIQUE' in str(err):
                print(f'Não Foi Possível Adicionar o Contato Na Agenda\nO Contato Já Existe.')

    def searchdata(self, term_search):
        data = []
        sql = f"""SELECT rowid, nome, email, telefone FROM agenda Where
        nome Like '{term_search}' or
        email Like '{term_search}' or
        telefone Like '{term_search}'"""

        for rowid, nome, email, telefone, in self.cur.execute(sql):
            data.append([rowid, nome, email, telefone])
        if not data:
            return None
        else:
            return data

    def editdata(self, mode, nome=None, email=None, newemail=None, telefone=None):
        sql = ''
        if not newemail:
            newemail = email
        if mode == 'all':
            sql = f"""UPDATE agenda SET nome='{nome}',
                     email ='{newemail}',
                     telefone ='{telefone}'
                     WHERE email='{email}'"""

        elif mode == 'nome':
            sql = f"""UPDATE agenda SET nome='{nome}'
                     WHERE email='{email}'"""
        elif mode == 'email':
            sql = f"""UPDATE agenda SET email ='{newemail}'
                     WHERE email='{email}'"""
        elif mode == 'telefone':
            sql = f"""UPDATE agenda SET telefone ='{telefone}'
                     WHERE email='{email}'"""
        self.cur.execute(sql)
        self.conn.commit()
        data = self.searchdata(newemail)
        return data

    def searchdeletedata(self, email):
        data = []
        sql = f"SELECT rowid, nome, email, telefone FROM agenda WHERE email == '{email}'"

        for rowid, nome, email, telefone, in self.cur.execute(sql):
            data.append([rowid, nome, email, telefone])
        if not data:
            return None
        else:
            return data

    def deletedata(self, email):
        self.cur.execute(f"DELETE FROM agenda WHERE email = '{email}'")
        self.conn.commit()

    def listdata(self):
        data = []
        sql = 'SELECT rowid, nome , email, telefone FROM agenda'
        for rowid, nome, email, telefone, in self.cur.execute(sql):
            data.append([rowid, nome, email, telefone])
        if not data:
            print('Não Existe Nenhum Contato')
            return data
        else:
            return data
