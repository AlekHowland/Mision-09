#encoding: UTF-8
#Autor: Alek Fernando Howland Aguilar, A01747765
#Descripción: Mision_09


def extraerPares(lista):    #Extrae los pares de una lista y regresa una lista con solo pares
    lista2 = []
    for n in lista:
        if n % 2 == 0:
            lista2.append(n)

    return lista2

a =  [1,2,3,2,4,60,5,8,3,22,44,55]
print(extraerPares(a))
#-----------------------------------------


def extraerMayoresPrevio(lista):      #Regresa una nueva lista con los numeros mayores a los previos intercambiados
    lista2 = []
    for n in range(0, len(lista)):
        if n+1 < len(lista):
            if lista[n] < lista[n+1]:
                lista2.append(lista[n+1])

    return lista2


b =  [5,4,3,2]
print(extraerMayoresPrevio(b))
#----------------------------------------


def intercambiarParejas(lista):
    lista2 = []
    for n in range (1, len(lista),2):   #Empieza desde el indice 1 hasta el final de la lista con saltos de dos
        lista2.append(lista[n])         #Ingresa a la nueva lista los datos en las posiciones
    for n in range(0,len(lista),2):     #Empieza desde 0 con saltos de dos
        lista2.insert(n+1, lista[n])    #Insterta en la posicion siguiente el valor tomado del ciclo

    return lista2
c =  [1,2,3,2,4,60,5,8,3,22,44,55]

print(intercambiarParejas(c))
#---------------------------------------


def intercambiarMM(lista):          #Se ingresa una lista y se intercambian de posición el mayor con el menor
    M = max(lista)
    m = min(lista)
    for n in range(0,len(lista)):
        if lista[n] == M:
            lista[n] = m
        elif lista[n] == m:
            lista[n] = M

    return lista


d = [5,9,3,22,19,31,10,7]
print(intercambiarMM(d))


#------------------------------------------
def promediarCentro(lista):         #Se obtiene el promedio eliminando el mayor y el menor de la lista
    listaPromedio = lista.copy()
    if len(listaPromedio) > 2:
        listaPromedio.sort()
        listaPromedio.pop()
        listaPromedio.pop(0)
        promedio = sum(listaPromedio) // len(listaPromedio)
        return promedio
    else:
        return 0

e =   [95, 21, 73, 24, 15, 69, 71, 80, 49, 100, 85]
print(promediarCentro(e))
#---------------------------------------------------


def calcularEstadistica(lista):         #Se hacen calculos estadisticos
    c = 0
    if len(lista) > 0:
        mean = sum(lista) / len(lista)
    else:
        mean = 0
    if len(lista) > 1:
        for n in lista:
            c += (n - mean)**2
        a = c / (len(lista) - 1)
        b = a**0.5
    else:
        b = 0
    return mean, b



f = [95,21,73,24,15,69,71,80,49,100,85]
print(calcularEstadistica(f))
#-------------------------------------------------


def calcularSuma(lista):        #Se calcula la suma de una lista eliminando los numeros adyacentes a 13 y el mismo
    listaSuma = lista.copy()
    if 13 not in listaSuma:
        return sum(listaSuma)
    else:
        for n in range(len(listaSuma)):
            if listaSuma[n] == 13:
                listaSuma[n] = 0
                if n != 0:
                    listaSuma[n-1] = 0
                if n != len(listaSuma)-1:
                    listaSuma[n+1] = 0


    total = sum(listaSuma)
    return total


g = [5, 2, 13, 4, 1, 6, 1, 8, 4, 13, 1]
print(calcularSuma(g))
