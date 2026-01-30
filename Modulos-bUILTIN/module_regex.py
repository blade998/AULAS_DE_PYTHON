import re
# Regex é uma linguagem para buscar e manipular texto.
# Ela permite encontrar padrões em strings de forma muito flexível.
texto = ' Meu email e teste@exemplo.com  COSTA@EMAIL.COM'

resultado = re.findall(r"\S+@\S+", texto)

print(resultado)