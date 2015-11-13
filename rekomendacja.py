#  Wzorowane na przykładzie Rona Zacharskiego
#

from math import sqrt
from numpy import corrcoef

users = {
    "Ania":
        {"Blues Traveler": 1.,
         "Broken Bells": 1.5,
         "Norah Jones": 2,
         "Deadmau5": 2.5,
         "Phoenix": 3.0,
         "Slightly Stoopid": .5,
         "The Strokes": 0.0,
         "Vampire Weekend": 2.0},
    "Bonia":
        {"Blues Traveler": 4.0,
         "Broken Bells": 4.5,
         "Norah Jones": 5.0,
         "Deadmau5": 5.5,
         "Phoenix": 6.0,
         "Slightly Stoopid": 3.5,
         "The Strokes": 2.0,
         "Vampire Weekend": 5.0}
}


def manhattan(rating1, rating2):
    """Oblicz odległość w metryce taksówkowej między dwoma  zbiorami ocen
       danymi w postaci: {'The Strokes': 3.0, 'Slightly Stoopid': 2.5}
       Zwróć -1, gdy zbiory nie mają… wspólnych elementów"""

    # TODO: wpisz kod
    klucze1 = rating1.keys()
    klucze2 = rating2.keys()
    odleglosc = 0
    udaloSiePorownac = False

    for klucz in klucze1:
        if klucz in rating2.keys():
            udaloSiePorownac = True
            odleglosc = odleglosc + abs(rating2[klucz] - rating1[klucz])

    if (udaloSiePorownac == True):
        return odleglosc
    else:
        return -1


def pearson(rating1, rating2):
    sumax = 0
    sumay = 0
    sumaxy = 0
    sumax2 = 0
    sumay2 = 0
    n = 0
    for k in rating1.keys():
        if k in rating2.keys():
            sumax += rating1[k]
            sumax2 += rating1[k] * rating1[k]
            sumay += rating2[k]
            sumay2 += rating2[k] * rating2[k]
            sumaxy += rating1[k] * rating2[k]
            n += 1
    return (sumaxy-sumax*sumay/n)/(sqrt(sumax2-sumax*sumax/n)*sqrt(sumay2-sumay*sumay/n))


def pearsonNumpy(rating1, rating2):
    return corrcoef(list(rating1.values()), list(rating2.values()))[0, 1]


print(pearson(users["Ania"], users["Bonia"]))
print(pearsonNumpy(users["Ania"], users["Bonia"]))