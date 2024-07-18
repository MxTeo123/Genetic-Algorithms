import numpy

######################## CALCUL FUNCTIE FITNESS ######################
def fitnessTSP(x, n, cost):
    fitness = 0
    for i in range(n - 1):
        fitness = fitness + cost[x[i]][x[i + 1]]
    fitness = fitness + cost[x[0]][x[n - 1]]
    return fitness

######################## GENERAREA UNEI POPULATII ####################
def gen(dim):
    c = numpy.genfromtxt("costuri_tsp.txt")
    n = len(c)
    pop = []
    for i in range(dim):
        x = numpy.random.permutation(n)
        fitness = fitnessTSP(x, n, c)
        x = list(x)
        x = x + [fitness]
        pop = pop + [x]
    return pop, dim, n, c


##################### OPERATOR MUTATIE INTERSCHIMBARE #################
def m_perm_interschimbare(x, n):
    poz = numpy.random.randint(0, n, 2)
    while poz[0] == poz[1]:
        poz = numpy.random.randint(0, n, 2)
    p1 = numpy.min(poz)
    p2 = numpy.max(poz)
    y = x.copy()
    y[p1] = x[p2]
    y[p2] = x[p1]
    return y

####################### APLICARE MUTATIE POPULATIE #####################
def mutatie_populatie(pop, dim, n, c, probabilitate_m):
    pop_m = pop.copy()
    for i in range(dim):
        r = numpy.random.uniform(0, 1)
        if r <= probabilitate_m:
            x = pop[i][0:n].copy()
            x = m_perm_interschimbare(x, n)
            fitness = fitnessTSP(x, n, c)
            x = x + [fitness]
            pop_m[i] = x.copy()
    return pop_m



'''
import TSP
populatie,dim,n,c = TSP.gen(10)
populatie_m = TSP.mutatie_populatie(populatie, dim, n, c, 0.2)
import numpy
populatie = numpy.asarray(populatie)
populatie_m = numpy.asarray(populatie_m)
'''


