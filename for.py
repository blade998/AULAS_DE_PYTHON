# lista

movielist = [
    "blade",'chicago34','trui'
]

#interando valores de uma lista

for movie in movielist:
    print(movie)

for movie in movielist:
    if movie == "chicago34":
        break
    print(movie)

for movie in movielist:
    if movie == "blade":
        continue
    print(movie)