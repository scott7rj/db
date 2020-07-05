class Usuario(object):
   
    def __init__(self):
        self.id = 0
        self.matricula = ''
        self.nome = ''
        self.sobrenome = ''
        self.senha = ''
        self.perfil = ''
        
    def __repr__(self):
        return f"Usuario('{self.id}', '{self.matricula}', '{self.nome}', '{self.senha}', '{self.perfil}')"

