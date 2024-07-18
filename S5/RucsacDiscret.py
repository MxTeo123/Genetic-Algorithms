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