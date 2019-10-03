sumSerie = 0
for i in range(1, 1001):
    sumSerie += (i**i)
sumSerie = str(sumSerie)
tam = len(sumSerie)
serie = ""
for i in range((tam-11), tam):
    serie += sumSerie[i]
print(serie)