def fatorial(n):
    if n == 1:           # caso base: parar a recursão
        return 1
    else:
        return n * fatorial(n - 1)  # chamada recursiva

# Testando a função
print(fatorial(5))  # Saída: 120

print(fatorial(1))  