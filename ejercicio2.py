numero = int(input("Escribe un numero "))
temp = 1

if numero > 0:
    for temp in range(1, 11):
        print(temp*numero)


print(f"El numero escrito es {numero}")