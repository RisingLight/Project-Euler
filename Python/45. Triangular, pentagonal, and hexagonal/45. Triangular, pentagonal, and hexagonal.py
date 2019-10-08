ct =285
t = 40755
listat = []

cp = 493
p = 40755
listap = []

ch = 569
h = 40755
listah = []

cont = 0

while True:

    listah.append(h)

    if p in listah:
        listap.append(p)

    if t in listap:
        listat.append(t)
        cont +=1

    if cont == 3:
        break

    ct+=1
    t+=ct
    cp+=3
    p+=cp
    ch+=4
    h+=ch

print(listat[2])
    