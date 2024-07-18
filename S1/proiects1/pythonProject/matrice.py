import numpy as numpy

#generam matrice 4 x 5
mat=numpy.zeros([4,5], dtype="double")
print("matrice dupa initializare\n ")
print(mat)

#citire matrice din fisier
mat[0:4, 0:4]=numpy.genfromtxt("date.txt") # inseamna de la 0 la 3

print("matrice dupa initializare \n")

print(mat)

for i in range(4):
    mat[i,4]=numpy.sum(mat[i,0:4])  #doar la range se face excludere de capat

print("matrice dupa calcul ult coloana \n")
print(mat)

#matrice 5 x 3 val generate aleator

mat_aleator=numpy.random.uniform(-1, 1, [5,3])
print("matricea cu valori aleatoare \n")
print(mat_aleator)

#tema 1
#calculati produsul mat x mat_aleator

print("produsul mat\n")
prod = numpy.dot(mat, mat_aleator)
print(prod)



#tema 2
#generati o matrice de dimensiune 20 x 5 cu valori aleatoare
#din distributia normala- pe ce interval vrem si calculati lista de dimensiune 1 x 20
#care contine media valorilor pe linii ale matricei generate

print("matrice 20 x 5 random\n")
matrix=numpy.random.uniform(-100,100,[20,5])
print(matrix)

print("media pe linii\n")
media_linii=numpy.mean(matrix,axis=1)
print(media_linii)

