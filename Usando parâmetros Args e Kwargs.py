

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total
    
print(soma(2,3,5,6,7))

def mostrar_info(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

mostrar_info(nome="Ana", idade=16)