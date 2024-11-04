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
        i = 0
        if len(lista[i].split(None)) > 6:
            milista.append(palabra)
            i *= 1

    print(milista)