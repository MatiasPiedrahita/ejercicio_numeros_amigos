def obtener_suma_divisores(numero1, numero2, sumaDivisores):
        for i in range (1, numero1):
            if numero1 % i == 0:
                sumaDivisores += i
        if numero2 == sumaDivisores:
            print(f"Los 2 numeros son amigos, pues la suma de los divisores de {numero1} es = a {numero2}")
        else:
            print(f"Los 2 numeros NO son amigos, pues la suma de los divisores de {numero1} NO es = a {numero2}")
sumaDivisores = 0
error = True
while error is True:
    try:
        numero1 = int(input("Ingresa el primer numero: "))
        numero2 = int(input("Ingrese el segundo numero: "))
    except ValueError:
        print("Ingresa unicamente numeros enteros")
    else:
         error = False
         obtener_suma_divisores(numero1, numero2, sumaDivisores)