#Jorge Casas#
#Punto 1#
mat= [[11, 23, 76, 34, 11],
            [14, 30, 92, 30, 101],
            [12, 45, 58, 92, 22],
            [74, 56, 49, 56, 100],
            [99, 5, 28, 47, 99]]

esCapicua1 = [42, 12, 90, 90, 12, 42]
def verificarDiagonales(mat):
   
    diagonal1 = []
    diagonal2 = []
    i = 0
    j = 0
    resultado = True
    for i in range(len(mat)):
        for j in range(len(mat)):
            if i == j:
                diagonal1.append(mat[i][j])
    for i in range(len(mat)):
        for j in range(len(mat)):
            if (i + j) == (len(mat)-1) :
                diagonal2.append(mat[i][j])

    for i in range(len(diagonal1)):
        if diagonal1[i] != diagonal2[i]:
            resultado = False
    
    print(resultado)

verificarDiagonales(mat)

#Punto 2#
def esCapicua(esCapicua1):
    i = 0
    veracidad = True
    j = len(esCapicua1)
    for i in range(len(esCapicua1)):
        if veracidad == True:
            if esCapicua1[i] == esCapicua1[j-i-1]:
                veracidad = True
            else:
                i=len(esCapicua1)+1
                veracidad = False
    print (veracidad)

esCapicua(esCapicua1)

#Punto 3#
#Sección A#
listaA = [40, 10, 22, 12, 33, 33, 33]
listaB = [41, 22, 31, 15, 13, 12, 33, 19]

def diferenciadeListas(listaA, listaB):
    listaTemporalA = listaA
    listaTemporalB = listaB
    diferencia = list(set(listaTemporalA).intersection(set(listaTemporalB)))
    
    for i in range(len(diferencia)):
        listaTemporalA.remove(diferencia[i])
    
    print (listaTemporalA)
                
#diferenciadeListas(listaB, listaA)
#Seccion B#
def lecturaDatos():
    i = 0
    dato = input()
    for i in range(int(dato)):
        tamano1 = input()
        lista1 = []
        lista2 = []
        for j in range(int (tamano1)):
            lista1.append(int(input()))
        tamano2 = input()
        for k in range(int (tamano2)):
            lista2.append(int(input()))
        diferenciadeListas(lista1, lista2)
#lecturaDatos()

#Punto 4#
N = 100
def mostrarPrimos(N):
    print("Números primos entre 1 y ", N)
    i = 1
   
    separadorString = 0
    arrayPrimosSum = []
    while i < N:
        numeroReferencia = 1
        contadorPrimos = 0
        while numeroReferencia <= i:
            if i % numeroReferencia == 0:
                contadorPrimos+=1
            numeroReferencia+=1
        if contadorPrimos == 2:
            print ("-->", i,"\n")
            separadorString = i
            sum = 0
            digito = 0
            k = 0
            for digito in str(separadorString):
                sum += int(digito)
            contadorDigitos = 0
            digitosReferencia = 1
            while digitosReferencia <= sum:
                if sum % digitosReferencia == 0:
                    contadorDigitos+=1
                digitosReferencia+=1
            if contadorDigitos == 2:
                arrayPrimosSum.append(i)
        i+=1
    print ("Números entre 1 y", N,"con suma de dígitos con valor primo:")
    for j in range(len(arrayPrimosSum)):
        print (arrayPrimosSum[j])
        j+=1

#mostrarPrimos(N)

#Punto 5#
matriz = {0 : [(0, 1), (5, 4), (7, 5)],
       1 : [(6, 4), (7, 7)],
       2 : [(0, 2), (1, 2), (4, 9), (6, 1)],
       4 : [(2, 8), (3, 1), (5, 7)],
       6 : [(0, 3), (5, 6), (7, 2)],
       7 : [(0, 4), (1, 4), (2, 7)],
       8 : [(1, 9), (3, 8), (5, 7), (7, 6)]}

def sumarValoresMatriz(matriz, par):
    i = 0
    j = 0
    k = 0
    l = 0
    sumaParejas = 0
    for i, j in par:
        if i in matriz:
            for k, l in matriz[i]:
                if j == k:
                    sumaParejas += l
    return sumaParejas
print(sumarValoresMatriz(matriz, [(0, 0), (8, 3), (3, 5), (7, 2), (4, 3), (4,6)]))
