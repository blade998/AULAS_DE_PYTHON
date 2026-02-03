

class pessoa :
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade


class vitor(pessoa):
    def falar():
     print('Meu nome e vitor')


vitinho = vitor('vitor',14)
print(vitinho.nome)
vitinho.falar