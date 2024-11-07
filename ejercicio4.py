filas = int(input("Escribe el número de filas para la pirámide: "))

for i in range(1, filas + 1):
    print(""
              "")
    for j in range(1, i + 1):
        print(j, end=' ')

