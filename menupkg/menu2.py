class Menu2(object):
   
    def __init__(self):
        self.id = 0
        self.nome = ''
        self.id_menu1 = 0
        self.ordem = 0
        self.ativo = True
        self.target = ''
        
    def __repr__(self):
        return f"Menu2('{self.id}', '{self.nome}', {self.id_menu1}, '{self.ordem}', '{self.ativo}', '{self.target}')"

