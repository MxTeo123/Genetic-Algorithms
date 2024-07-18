import numpy


######################## CALCUL FUNCTIE FITNESS + FEZ ######################
def ok(x, n, c, v, cmax):
    fitness = 0
    cost = 0
    for i in range(n):
        fitness = fitness + x[i] * v[i]
        cost = cost + x[i] * c[i]
    return cost <= cmax, fitness


########################## GENERAREA UNEI POPULATII ########################
def gen(cmax, dim):
    c = numpy.genfromtxt("cost.txt")
    v = numpy.genfromtxt("valoare.txt")
    n = len(c)
    pop = []
    for i in range(dim):
        flag = False
        while flag == False:
            x = numpy.random.randint(0, 2, n)
            flag, fitness = ok(x, n, c, v, cmax)
        x = list(x)
        x = x + [fitness]
        pop = pop + [x]
    return pop, dim, n, c, v, cmax


########################### OPERATOR MUTATIE BINARA #########################
def m_binara(gena):
    gena_mutanta = not gena
    return int(gena_mutanta)  # cast pentru trecerea True/False in 1/0


########################## APLICARE MUTATIE POPULATIE #########################
def mutatie_populatie(pop, dim, n, c, v, cost_max, probabilitate_m):
    pop_m = pop.copy()
    for i in range(dim):
        x = pop[i][:n].copy()
        for j in range(n):
            r = numpy.random.uniform(0, 1)
            if r <= probabilitate_m:
                x[j] = m_binara(x[j])
        fez, val = ok(x, n, c, v, cost_max)
        if fez:
            x = x + [val]
            pop_m[i] = x.copy()
    return pop_m


'''
import RucsacDiscret
populatie,dim,n,c,v,cost_max = RucsacDiscret.gen(30, 10)
populatie_m = RucsacDiscret.mutatie_populatie(populatie, dim, n, c, v, cost_max, 0.1)
import numpy
populatie = numpy.asarray(populatie)
populatie_m = numpy.asarray(populatie_m)
'''


def crossover_unipunct(x1, x2, n):
    # genereaza aleator gena in care este facuta recombinarea
    p = numpy.random.randint(0, n)
    c1 = x1.copy()
    c2 = x2.copy()
    c1[0:p] = x1[0:p]
    c1[p:n] = x2[p:n]
    c2[0:p] = x2[0:p]
    c2[p:n] = x1[p:n]
    return c1, c2

def crossover_populatie(pop, dim, n, c, v, cmax, probabilitate_crossover):
    copii = pop.copy()
    # populatia este parcursa astfel incat sunt selectati indivizii 0,1 apoi 2,3 s.a.m.d
    for i in range(0, dim - 1, 2):
        # selecteaza parintii
        x1 = pop[i][0:n].copy()
        x2 = pop[i + 1][0:n].copy()
        r = numpy.random.uniform(0, 1)
        if r <= probabilitate_crossover:
            c1, c2 = crossover_unipunct(x1, x2, n)
            flag, fitness = ok(c1, n, c, v, cmax)
            if flag == True:
                c1 = c1 + [fitness]
                copii[i] = c1.copy()
            flag, fitness = ok(c2, n, c, v, cmax)
            if flag == True:
                c2 = c2 + [fitness]
                copii[i + 1] = c2.copy()
    return copii

"""
import RucsacDiscret
import numpy
populatie, dim, n, c, v, cmax = RucsacDiscret.gen(30, 10)
copii = RucsacDiscret.crossover_populatie(populatie, dim, n, c, v, cmax, 0.7)
populatie = numpy.asarray(populatie)
copii = numpy.asarray(copii)
"""

