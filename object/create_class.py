#Em Python, uma classe é como um molde para criar objetos. Ela define atributos (características) e métodos (ações).
# 
class carro:
    def __init__(self,nome,ano,marca):
        self.nome = nome
        self.ano = ano
        self.marca = marca

    def apresentar(self):
     print(f"carro {self.nome}, do ano de {self.ano} da marca {self.marca}")

lancer = carro("lancer",2000,"mitsubichi")
print(lancer.apresentar())