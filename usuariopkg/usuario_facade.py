from dbpkg.postgres import Postgres
from usuariopkg.usuario import Usuario
from dbpkg.result import Result
from pkg import bcrypt

class UsuarioFacade(object):
   
    def __init__(self):
        self.postgres = Postgres()
        self.result = Result()

    def to_usuario(self):
        usuario = Usuario()
        if self.result.rows:
            usuario.id = self.result.rows[0]
            usuario.matricula = self.result.rows[1]
            usuario.nome = self.result.rows[2]
            usuario.senha = self.result.rows[3]
            usuario.perfil = self.result.rows[4]
        return usuario

    def to_all_usuario(self):
        l = []
        for row in self.result.rows:
            usuario = Usuario()
            usuario.id = row[0]
            usuario.matricula = row[1]
            usuario.nome = row[2]
            usuario.senha = row[3]
            usuario.perfil = row[4]
            l.append(usuario)
        t = tuple(l)
        return t

    def get_user_by_id(self, id):
        conn = self.postgres.connect()
        self.result = self.postgres.query_one(f"SELECT id, matricula, nome, senha, perfil  FROM usuario WHERE id = {id}")
        #print(self.result.rows)
        #print(self.result.rowcount)
        usuario = Usuario()
        if self.result.rows:
            usuario.id = self.result.rows[0]
            usuario.matricula = self.result.rows[1]
            usuario.nome = self.result.rows[2]
            usuario.senha = self.result.rows[3]
            usuario.perfil = self.result.rows[4]
        else:
            usuario = None
        self.postgres.disconnect(conn)
        return self.result
    
    def get_user_by_matricula(self, matricula):
        conn = self.postgres.connect()
        self.result = self.postgres.query_one(f"SELECT id, matricula, nome, senha, perfil  FROM usuario WHERE upper(matricula) = '{matricula}'")
        #print(self.result.rows)
        #print(self.result.rowcount)
        usuario = Usuario()
        if self.result.rows:
            usuario.id = self.result.rows[0]
            usuario.matricula = self.result.rows[1]
            usuario.nome = self.result.rows[2]
            usuario.senha = self.result.rows[3]
            usuario.perfil = self.result.rows[4]
        else:
            usuario = None
        self.postgres.disconnect(conn)
        return self.result

    def get_all_user_by_id(self, ids):
        conn = self.postgres.connect()
        self.result = self.postgres.query_all(f"SELECT id, matricula, nome, senha, perfil  FROM usuario WHERE id IN({ids})")
        #print(self.result.rowcount)
        #for row in self.result.rows:
        #    print(row)
        self.postgres.disconnect(conn)
        return self.result

    def get_all_user_by_matricula(self, matricula):
        conn = self.postgres.connect()
        self.result = self.postgres.query_all(f"SELECT id, matricula, nome, senha, perfil  FROM usuario WHERE upper(matricula) like '{matricula.upper()}%'")
        #print(self.result.rowcount)
        #for row in self.result.rows:
        #    print(row)
        self.postgres.disconnect(conn)
        return self.result

    def get_all_user_by_nome(self, nome):
        conn = self.postgres.connect()
        self.result = self.postgres.query_all(f"SELECT id, matricula, nome, senha, perfil FROM usuario WHERE upper(nome) like '%{nome}%'")
        #for row in self.result.rows:
        #    print(row)
        self.postgres.disconnect(conn)
        return self.result

    def create_user(self, matricula, nome, senha, perfil):
        conn = self.postgres.connect()
        usuario = Usuario()
        hashed_password = bcrypt.generate_password_hash(senha).decode('utf-8')
        self.postgres.execute(f"INSERT INTO usuario(matricula, nome, senha, perfil) VALUES('{matricula.upper()}', '{nome.upper()}', '{hashed_password}', '{perfil}')")
        usuario = self.get_user_by_matricula(matricula)
        self.postgres.disconnect(conn)
        #print(usuario)
        return usuario
    
    def update_user(self, id, matricula, nome, senha, perfil):
        conn = self.postgres.connect()
        hashed_password = bcrypt.generate_password_hash(senha).decode('utf-8')
        self.postgres.execute(f"UPDATE usuario SET matricula = '{matricula.upper()}', nome = '{nome.upper()}', senha = '{hashed_password}', perfil = '{perfil}' WHERE id = {id}")
        usuario = self.get_user_by_id(id)
        self.postgres.disconnect(conn)
        return usuario
    
    def delete_user_by_id(self, id):
        usuario = self.get_user_by_id(id)
        conn = self.postgres.connect()
        self.postgres.execute(f"DELETE FROM usuario WHERE id = {id}")
        self.postgres.disconnect(conn)
        return usuario
    
    def delete_all_user_by_id(self, ids):
        self.result = self.get_all_user_by_id(ids)
        conn = self.postgres.connect()
        self.postgres.execute(f"DELETE FROM usuario WHERE id in ({ids})")
        self.postgres.disconnect(conn)
        return self.result