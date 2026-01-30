import random 
# O random é um módulo que permite gerar números ou escolher elementos de forma aleatória.
#É muito usado em jogos, sorteios, simulações e testes.
print(random.random())

def calcularsexo():
    h = random.randint(1,10)
    if h <= 5 :
        print('Voce e uma mulherzinha')
    elif h > 5 :
        print('macho peludo')
calcularsexo()