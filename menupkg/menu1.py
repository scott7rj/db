class Menu1(object):
   
    def __init__(self):
        self.id = 0
        self.nome = ''
        self.perfil = ''
        self.ordem = 0
        self.ativo = True
        
    def __repr__(self):
        return f"Menu1('{self.id}', '{self.nome}', '{self.perfil}', '{self.ordem}', '{self.ativo}')"

