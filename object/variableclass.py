


class pessoa :
    tipo = 'humano'
    def __init__(self,nome,idade):
        self.nome= nome
        self.idade = idade

vitor = pessoa('vitor',14)
print(vitor.idade)
print(vitor.tipo)