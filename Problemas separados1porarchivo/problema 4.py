N = int(input("Introduce un número entero positivo: "))
if N > 0:
    suma = N * (N + 1) // 2  
    print(f"La suma de los primeros {N} enteros positivos es: {suma}")
else:
    print("El número debe ser un entero positivo.")