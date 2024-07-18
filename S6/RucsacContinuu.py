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
            x = numpy.random.uniform(0, 1, n)
            flag, fitness = ok(x, n, c, v, cmax)
        x = list(x)
        x = x + [fitness]
        pop = pop + [x]
    return pop, dim, n, c, v, cmax


######################### OPERATOR MUTATIE NEUNIFORMA #######################
def m_neuniforma(gena, sigma, a, b):
    zgomot = numpy.random.normal(0, sigma)
    gena_mutanta = gena + zgomot
    if gena_mutanta > b:
        gena_mutanta = b
    if gena_mutanta < a:
        gena_mutanta = a
    return gena_mutanta


########################## OPERATOR MUTATIE UNIFORMA ########################

def m_uniforma(a, b):
    gena = numpy.random.uniform(a, b)
    return gena


########################## APLICARE MUTATIE POPULATIE #########################
def mutatie_populatie(pop, dim, n, c, v, cost_max, probabilitate_m, sigma):
    pop_m = pop.copy()
    for i in range(dim):
        x = pop[i][:n].copy()
        for j in range(n):
            r = numpy.random.uniform(0, 1)
            if r <= probabilitate_m:
                x[j] = m_neuniforma(x[j], sigma, 0, 1)
                #SAU x[j] = m_uniforma(0, 1)
        fez, val = ok(x, n, c, v, cost_max)
        if fez:
            x = x + [val]
            pop_m[i] = x.copy()
    return pop_m


'''
import RucsacContinuu
populatie,dim,n,c,v,cost_max = RucsacContinuu.gen(30, 10)
populatie_m = RucsacContinuu.mutatie_populatie(populatie, dim, n, c, v, cost_max, 0.1, 0.15)
import numpy
populatie = numpy.asarray(populatie)
populatie_m = numpy.asarray(populatie_m)
'''


def crossover_singular(x1, x2, n, alpha):
    # genereaza aleator gena in care este facuta recombinarea
    i = numpy.random.randint(0, n)
    c1 = x1.copy()
    c2 = x2.copy()
    c1[i] = (alpha * x1[i] + (1 - alpha) * x2[i])
    c2[i] = (alpha * x2[i] + (1 - alpha) * x1[i])
    return c1, c2


def crossover_total(x1, x2, n, alpha):
    c1 = x1.copy()
    c2 = x2.copy()
    for i in range(0, n):
        c1[i] = (alpha * x1[i] + (1 - alpha) * x2[i])
        c2[i] = (alpha * x2[i] + (1 - alpha) * x1[i])
    return c1, c2

def crossover_populatie(pop, dim, n, c, v, cmax, probabilitate_x, alpha):
    copii = pop.copy()
    # populatia este parcursa astfel incat sunt selectati indivizii 0,1 apoi 2,3 etc
    for i in range(0, dim - 1, 2):
        # selecteaza parintii
        x1 = pop[i][0:n].copy()
        x2 = pop[i + 1][0:n].copy()
        r = numpy.random.uniform(0, 1)
        if r <= probabilitate_x:
            c1, c2 = crossover_singular(x1, x2, n, alpha)
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
import RucsacContinuu
import numpy
populatie, dim, n, c, v, cmax = RucsacContinuu.gen(30, 10)
copii = RucsacContinuu.crossover_populatie(populatie, dim, n, c, v, cmax, 0.8, 0.7)
populatie = numpy.asarray(populatie)
copii = numpy.asarray(copii)
"""



def fps(fitnessuri, dim):
    fps=numpy.zeros(dim)
    suma=numpy.sum(fitnessuri)
    for i in range(dim):
        fps[i]=fitnessuri[i]/suma
    qfps=fps.copy()
    for i in range(1,dim):
        qfps[i]=qfps[i-1]+fps[i]
    return qfps

def ruleta(pop_initiala, dim, n):
    pop_initiala=numpy.asarray(pop_initiala)
    parinti=pop_initiala.copy()
    fitnessuri=numpy.zeros(dim, dtype="float")
    for i in range(dim):
        fitnessuri[i]=pop_initiala[i][n]
    qfps=fps(fitnessuri, dim)
    for i in range(dim):
        r=numpy.random.uniform(0,1)
        pozitie=numpy.where(qfps>=r)
        # prima pozitie din qfps care respecta conditia:
        index_buzunar_ruleta=pozitie[0][0]
        # copiez genele individului care devine parinte
        parinti[i][0:n]=pop_initiala[index_buzunar_ruleta][0:n]
        # copiez fitness ul individului care devine parinte:
        parinti[i][n]=pop_initiala[index_buzunar_ruleta][n]
    return parinti

def selectieParinti():
    pop_initiala, dim,n,c,v,cmax=gen(30,10)
    parinti=ruleta(pop_initiala,dim,n)
    return numpy.asarray(pop_initiala),numpy.asarray(parinti)


#tema sus   stochastic universal sample