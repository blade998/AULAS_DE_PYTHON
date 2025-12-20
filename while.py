movielist = [
    "blade",'chicago34','trui','Guerra2'
]

movielist2 = [
    "Hade",'c4','trtv','Guerra2'
]



# iterando valores de uma lista


index = 0

while index < len(movielist):
    print(movielist[index])
    index += 1



count = 0

while count < len(movielist2): 

    if  movielist2[count] == "trtv":
        break
    print(movielist2[count])
    count += 1
