from classes.abstractcrud import abstractcrud

class Produto(abstractcrud):
    arquivo = 'db/produtos.json'

    def __init__(self, codigo, nome, quantidade = 0, valor = 0):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.valor = valor
    
    def inserir(self):
        lista = self.consultar()
        produtoDuplicado = filter(lambda p: p['codigo'] == self.codigo, lista)

        if len(list(produtoDuplicado)):
            print()
            print('Ja existe um produto com esse codigo')
        else:
            super().inserir()
    

