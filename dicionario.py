FilmInception = {
"Title" : "MATRIX",
"YearRelease": 2021,
"IMdbRating": 8.5,
"Genre": ["Action", "Horror"]
}

print(FilmInception)
print(len(FilmInception))
print(type(FilmInception))

# recuperar um elemento do dicionario

print(FilmInception['Genre'])
print(FilmInception.get("Title"))
                        
                        # Buscar valaores 
print(FilmInception.values())