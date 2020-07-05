from dbpkg.postgres import Postgres
from menupkg.menu2 import Menu2
from dbpkg.result import Result

class Menu2Facade(object):
   
    def __init__(self):
        self.postgres = Postgres()
        self.result = Result()

    def to_menu2(self):
        if self.result.rows:
            menu2 = Menu2()
            menu2.id = self.result.rows[0]
            menu2.nome = self.result.rows[1]
            menu2.id_menu1 = self.result.rows[2]
            menu2.ordem = self.result.rows[3]
            menu2.ativo = self.result.rows[4]
            menu2.target = self.result.rows[5]
        return menu2

    def to_all_menu2(self):
        l = []
        for row in self.result.rows:
            menu2 = Menu2()
            menu2.id = row[0]
            menu2.nome = row[1]
            menu2.id_menu1 = row[2]
            menu2.ordem = row[3]
            menu2.ativo = row[4]
            menu2.target = row[5]
            l.append(menu2)
        t = tuple(l)
        return t

    def get_all_menu2_by_menu1(self, id_menu1):
        #print(perfil)
        conn = self.postgres.connect()
        self.result = self.postgres.query_all(f"SELECT id, nome, id_menu1, ordem, ativo, target  FROM menu2 WHERE id_menu1 = {id_menu1} ORDER BY ordem")
        #print(self.result.rowcount)
        #for row in self.result.rows:
        #    print(row)
        self.postgres.disconnect(conn)
        return self.result

    def get_all_active_menu2_by_menu1(self, id_menu1):
        #print(perfil)
        conn = self.postgres.connect()
        self.result = self.postgres.query_all(f"SELECT id, nome, id_menu1, ordem, ativo, target  FROM menu2 WHERE id_menu1 = {id_menu1} AND ativo = true ORDER BY ordem")
        #print(self.result.rowcount)
        #for row in self.result.rows:
        #    print(row)
        self.postgres.disconnect(conn)
        return self.result