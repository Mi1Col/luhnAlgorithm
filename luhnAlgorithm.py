
# Pide el numero de tarjeta y comprueba si mide 16
numberCard = input("Introduzca su numero de tarjeta: ")
if len(str(numberCard)) != 16:
    numberCard = int(input("Introduzca su numero de tarjeta: "))

# Invierte el numero de tarjeta
numberCardInv = str(numberCard)[::-1]

# Transforma los numeros en enteros y los añade a una lista
lista = []
for i in numberCardInv:
    lista.append(int(i))

# Multiplica los numeros en una posicion par y si el resultado tiene dos digitos, los suma
for j in lista:
    if lista.index(j) % 2 == 0:
        a = j * 2
        if len(str(a)) != 1:
            suma = int(str(a)[0]) + int(str(a)[1])
            lista[lista.index(j)] = suma
        else:
            lista[lista.index(j)] = a

# Sumar todos los digitos
suma2 = sum(lista)

# Si la suma es divisible entre 10 (acaba en 0) el numero de tarjeta es valido

if suma2 % 10 == 0:
    print("El numero de tarjeta es VALIDO")