import math
x = int(input(''))
tab = [1, 2, 3 , 10, 20, 30, 100, 200, 300]
i = -1
while tab[i] != x:
    i += 1
    i = math.floor(i + (x - tab[i])*(len(tab)-1 - i)/(tab[-1] - tab[i]))
if i == -1:
    i = len(tab) - 1
print('Szukana liczba znajduje się pod indeksem: ', i)