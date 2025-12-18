FilmSET = {
    'RODA 3', 'REI DO FORRO', 'MATRIX'
}

print(type(FilmSET))


# 2 - TRUE e 1  são considerados o mesmo valor 

# adicionar item de outro set

newmovie = {'NOVO FILME'}
FilmSET.update(newmovie)
print(FilmSET)