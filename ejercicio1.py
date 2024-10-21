numero = int(input("Escribe un numero "))
suma = 0
temp = 1

#if numero !=0 and temp <= numero:
#   suma = numero + temp
#   temp +=1
if numero > 0:
    for temp in range(1, numero + 1):
        suma += temp


print(f"El numero escrito es {numero} y"
      f" la suma de todos los numeros desde el 1 al numero es {suma}")