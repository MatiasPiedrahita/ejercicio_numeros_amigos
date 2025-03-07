def obtener_suma_divisores(numero):
        sumaDivisores = 0
        for i in range (1, numero):
            if numero % i == 0:
                sumaDivisores += i
        return sumaDivisores

error = True
while error is True:
    try:
        numero = int(input("Ingresa el primer numero: "))
    except ValueError:
        print("Ingresa unicamente numeros enteros")
    else:
         error = False
         valor1 = numero
         sumaDivisores1 = obtener_suma_divisores(numero)
error = True
while error is True:
    try:
        numero = int(input("Ingrese el segundo numero: "))
    except ValueError:
        print("Ingresa unicamente numeros enteros")
    else:
         error = False
         valor2 = numero 
         sumaDivisores2 = obtener_suma_divisores(numero)

if valor2 == sumaDivisores1 and valor1 == sumaDivisores2:
    print(f"Los 2 numeros son amigos, pues la suma de los divisores de {valor1} es = a {valor2} y viceversa")
else:
    print(f"Los 2 numeros NO son amigos, pues la suma de los divisores de {valor1} NO es = a {valor2} y viceversa")