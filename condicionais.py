#


name = input("DIGITE O NOME DO FILME")
year = int(input("digite o ano do filme do filme"))
rating = float(input("DIGITE A NOTA DO FILME"))


if rating > 7:
    print(f"O filme {name} e muito bom")

elif rating < 7 and rating > 5:
    print('FILME MEDIANO')
else:
    print("QUE FILME HORROROSOOO")