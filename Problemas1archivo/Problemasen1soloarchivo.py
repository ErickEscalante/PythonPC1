## PROBLEMA 1
nombre = 0
nombre = input("coloque su nombre porfavor: ")
print(f"¡Hola {nombre}!")

## PROBLEMA 2
consumo = 0
Porcentaje = 0
Propina = 0
print("bienvenido al restaurante 3B")
print("Esperando que le haya gustado su comida ahora vamos a proceder a hacer el cobro por el plato")
consumo = int(input("¿De cuanto fue el consumo que realizo por sus platos? "))
Porcentaje = int(input("¿Cuanto porcentaje le gustaría dejar de propina? "))
Propina = consumo*Porcentaje/100
print(f"¡Perfecto entonces eso sería todo!, muchas gracias por los {Propina}$ de propina")

## PROBLEMA 3
payaso = 112
muñeca = 75
print("Estimado administrador, bienvenido a Payasos y Muñecas SAC Account, aqui podrá calcular el peso total del ultimo pedido")
PedidoP = int(input("ingrese el número de payasos que tuvo el ultimo pedido: "))
PedidoM = int(input("ingrese el número de muñecas que tuvo el ultimo pedido: "))
conformidad = input("¿ingreso el número correcto? Si/No")
if conformidad.lower() == "si":
    Pesopayasos = payaso*PedidoP
    Pesomuñecas = muñeca*PedidoM
    Pesototal = Pesomuñecas*Pesopayasos
else:
    PedidoP2 = int(input("ingrese denuevo el número de payasos que tuvo el ultimo pedido: "))
    PedidoM2 = int(input("ingrese denuevo el número de muñecas que tuvo el ultimo pedido: "))
    Pesopayasos = payaso*PedidoP2
    Pesomuñecas = muñeca*PedidoM2
    Pesototal = Pesomuñecas*Pesopayasos
print(f"El peso total es: {Pesototal}")

## PROBLEMA 4
N = int(input("Introduce un número entero positivo: "))
if N > 0:
    suma = N * (N + 1) // 2  
    print(f"La suma de los primeros {N} enteros positivos es: {suma}")
else:
    print("El número debe ser un entero positivo.")

## PROBLEMA 5
Showsvistos = int(input("¿Cuántos shows musicales has visto en el último año? "))
Masdetres = Showsvistos > 3
print(f"¿Has visto más de 3 shows? {Masdetres}")

## PROBLEMA 6
edad = int(input("Introduce la edad del cliente: "))

if edad < 4:
    precio = 0 
elif 4 <= edad <= 18:
    precio = 5 
else:
    precio = 10  

print(f"El precio de la entrada es: ${precio}")

## PROBLEMA 7
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

## PROBLEMA 8
def convertiraminutos(hora, minutos):
    return hora * 60 + minutos
print("Introduce la hora en formato HH:MM Por favor")
Hora = input(" ")
hora, minutos = map(int, Hora.split(":"))
Minutos = convertiraminutos(hora, minutos)
desayunoinicio = convertiraminutos(7, 0)
desayunofin = convertiraminutos(8, 0)
almuerzoinicio = convertiraminutos(12, 0)
almuerzofin = convertiraminutos(13, 0)
cenainicio = convertiraminutos(18, 0)
cenafin = convertiraminutos(19, 0)
if desayunoinicio <= Minutos <= desayunofin:
    print("Es la hora del desayuno.")
elif almuerzoinicio <= Minutos <= almuerzofin:
    print("Es la hora del almuerzo.")
elif cenainicio <= Minutos <= cenafin:
    print("Es la hora de la cena.")

## PROBLEMA 9
PrimeraLista = ['Di', 'buen', 'día', 'a', 'papa']
Listavolteada = PrimeraLista[::-1]
print(Listavolteada)

## PROBLEMA 10
Listadecolores = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
del Listadecolores[5]  
del Listadecolores[4]  
del Listadecolores[0]  
print(Listadecolores)


## PROBLEMA 11
listaoriginal = [1, 1, 2, 3, 4, 4, 5, 1]
listasinduplicados = list(set(listaoriginal))
listasinduplicados.sort()
print(listasinduplicados)

## PROBLEMA 12
TiposdeMIME= {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip"
}
Nombredelarchivo = input("Introduce el nombre del archivo porfavor: ").strip().lower()
if '.' in Nombredelarchivo:
    extension = Nombredelarchivo[Nombredelarchivo.rfind('.'):].lower()
else:
    extension = ""
TiposdeMIME = TiposdeMIME.get(extension, "application/octet-stream")
print(TiposdeMIME)