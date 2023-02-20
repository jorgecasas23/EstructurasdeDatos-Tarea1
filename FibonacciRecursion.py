#Jorge Casas y Juan Camilo Quiceno#
#Grupo A#

#Punto 6 Recursión#
def fibonacciRecursion(entrada):
    if entrada <= 1:
        return entrada
    else:
        return fibonacciRecursion(entrada - 1) + fibonacciRecursion(entrada - 2)

#for i in range(20):
    #print(fibonacciRecursion(i))

#Punto 7 Ciclos#
def fibonacciCiclos(entrada):
    if entrada <= 1:
        return 0
    else:
        a = 0
        b = 1
        for i in range(1, entrada):
            c = a + b
            a = b
            b = c
        return b

#for i in range(10000):
    #print(fibonacciCiclos(i))
