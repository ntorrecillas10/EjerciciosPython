def ej1(num1: int, num2: int):
    milista = []
    for num in range(num1,num2):
        if num > 1:
            es_primo = True

            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    es_primo = False
                    break
            if es_primo:
                milista.append(num)

    print(milista)



def ej2():
    lista = ["pesimo", "ultimo", "mariquita", "sobador", "tornado"]
    milista = []

    for palabra in lista:
        if len(palabra).__int__() > 6:
            milista.append(palabra)

    print(milista)


def ej3():
    lista = [3,4,5,6,7]
    lista_cuadrados = []

    for num in lista:
        cuadrado = num*num
        lista_cuadrados.append(cuadrado)

    print(lista_cuadrados)

def ej4(l1 : list, l2 : list):
    lista_final = l1

    for elem in l2:
        if elem not in l1:
            lista_final.append(elem)

    print(lista_final)


def ej5():
    lista = ["pesimo", "ultimo", "mariquita", "sobador", "tornado","pesimo", "ultimo", "mariquita", "sobador", "tornado"]
    palabra = "ultimo"

    for elem in lista:
        if palabra == elem:
            lista.remove(elem)

    print(lista)


def ej6():
    lista1 = [1, 2, 3, 4, 5]
    lista2 = [0, 1]
    lista_nueva = []

    for i, elem in enumerate(lista1):
        if i not in lista2:
            lista_nueva.append(elem)

    print(lista_nueva)


def ej7():
    lista = [1, 2, 4, 3, 2, 6, 7, 5, 3]
    lista_devuelta = []
    num = 2

    for i, elem in enumerate(lista):
        if elem == num:
            lista_devuelta.append(i)

    print(lista_devuelta)


def ej8():
    lista = ['Borja', 'borja@mail.com', 989565222, 'Marta', 'marta@mail.com', 989565333, 'Ricardo', 'raicar@mail.com', 989565444]
    lista_datos = []
    num = 2

    for elem in lista:
        if elem in lista:
            lista_datos.insert(1, lista[num])

    #    for dato in lista:
    #    if dato.__pos__() == num:
    #       lista_datos.append(dato)
    #       num +=3

    print(lista_datos)










