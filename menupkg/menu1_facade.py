from dbpkg.postgres import Postgres
from menupkg.menu1 import Menu1
from dbpkg.result import Result

class Menu1Facade(object):
   
    def __init__(self):
        self.postgres = Postgres()
        self.result = Result()

    def to_menu1(self):
        if self.result.rows:
            menu1 = Menu1()
            menu1.id = self.result.rows[0]
            menu1.nome = self.result.rows[1]
            menu1.perfil = self.result.rows[2]
            menu1.ordem = self.result.rows[3]
            menu1.ativo = self.result.rows[4]
        return menu1

    def to_all_menu1(self):
        l = []
        for row in self.result.rows:
            menu1 = Menu1()
            menu1.id = row[0]
            menu1.nome = row[1]
            menu1.perfil = row[2]
            menu1.ordem = row[3]
            menu1.ativo = row[4]
            l.append(menu1)
        t = tuple(l)
        return t

    def get_all_menu1_by_perfil(self, perfil):
        #print(perfil)
        conn = self.postgres.connect()
        self.result = self.postgres.query_all(f"SELECT id, nome, perfil, ordem, ativo  FROM menu1 WHERE upper(perfil) = '{perfil.upper()}' ORDER BY ordem")
        #print(self.result.rowcount)
        #for row in self.result.rows:
        #    print(row)
        self.postgres.disconnect(conn)
        return self.result

    def get_all_active_menu1_by_perfil(self, perfil):
        #print(perfil)
        conn = self.postgres.connect()
        self.result = self.postgres.query_all(f"SELECT id, nome, perfil, ordem, ativo  FROM menu1 WHERE upper(perfil) = '{perfil.upper()}' AND ativo = true ORDER BY ordem")
        #print(self.result.rowcount)
        #for row in self.result.rows:
        #    print(row)
        self.postgres.disconnect(conn)
        return self.result