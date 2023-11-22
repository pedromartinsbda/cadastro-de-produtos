from classes.abstractcrud import abstractcrud

class Categoria(abstractcrud):
    arquivo = 'db/categorias.json'

    def __init__(self, nome):
        self.nome = nome
    
    
