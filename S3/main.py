# #seminar 2
# #Cheie seminar: 1711 - Avramescu
# '''
#             Problema rucsacului
# caz discret (valorile sunt alese din multimea {0,1})
# caz continuu (valorile sunt alese din intervalul [0,1])
#
# Pasii unui algoritm genetic:
# 1. Determinam formei unui individ( individ = solutia problemei):
#     -determinarea numarului de gene
#     -determinarea tipului de date pe care il au genele
#     -determinarea intervalului / multimii din care se genereaza valorile genelor
#     -determinarea obiectivului problemei (scop = fitness = functie obiectiv = calitatea individului)
#     -determinarea restrictiilor problemei (daca exista)
#
# 2. Generarea unei populatii initiale de indivizi:
#     -dimensiunea populatiei se noteaza uzual cu cu "dim"
#     -dim se alege arbitrar, de ordinul zecilor / sutelor
#
# (... urmatorii pasi seminarul 3 ...)
# '''
#
# #VARIANTA DISCRETA:
# import numpy
#
# def ok(x, n, c, v, cmax):
#     val = 0 #pt calcul fitness individ x
#     cost = 0 #pt calcul cost individ x
#     for i in range(n):
#         val = val + x[i] * v[i]
#         cost = cost + x[i] * c[i]
#     return cost <= cmax, val
#     #returnez boolean daca e sau nu fezabil si fitenssul
#
# def gen(fc, fv, cmax, dim):
#     c = numpy.genfromtxt(fc)
#     v = numpy.genfromtxt(fv)
#     n = len(c)
#     pop = []    #populatia in care vor fi stocati indivizii
#     for i in range(dim):
#         flag = False
#         while flag == False:
#             x = numpy.random.randint(0,2,n)
#             flag, val = ok(x, n, c, v, cmax)
#         x = list(x) #cast la list
#         x = x + [val] # [val] -> ca sa-l adauge ca element la sfarsit
#         pop = pop + [x] # la fel ^
#     return numpy.asarray(pop) #putem vedea sub forma de matrice
#
#
# #VARIANTA CONTINUA:
# # def gen(fc, fv, cmax, dim):
# #     c = numpy.genfromtxt(fc)
# #     v = numpy.genfromtxt(fv)
# #     n = len(c)
# #     pop = []
# #     for i in range(dim):
# #         flag = False
# #         while flag == False:
# #             # x = numpy.random.randint(0,2,n)
# #             x = numpy.random.uniform(0, 1, n) #singura diferenta || restul functiilor raman la fel
# #             flag, val = ok(x, n, c, v, cmax)
# #         x = list(x)
# #         x = x + [val]
# #         pop = pop + [x]
# #     return numpy.asarray(pop)
