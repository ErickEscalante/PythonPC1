num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
print("Elige una opción:")
print("1. Sumar los dos números")
print("2. Restar los dos números (el primero menos el segundo)")
print("3. Multiplicar los dos números")
opcion = int(input("Introduce el número de la opción elegida: "))
if opcion == 1:
    resultado = num1 + num2
    print(f"La suma de {num1} y {num2} es: {resultado}")
elif opcion == 2:
    resultado = num1 - num2
    print(f"La resta de {num1} menos {num2} es: {resultado}")
elif opcion == 3:
    resultado = num1 * num2
    print(f"La multiplicación de {num1} y {num2} es: {resultado}")
else:
    print("Opción inválida. Por favor elige una opción correcta del menú.")