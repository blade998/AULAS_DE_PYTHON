#collections é um módulo que traz estruturas de dados avançadas além das listas, tuplas, dicionários e sets padrões do Python.

from collections import Counter

dados = ['maçã', 'banana', 'maçã', 'laranja', 'banana', 'maçã']
contagem = Counter(dados)
print(contagem)