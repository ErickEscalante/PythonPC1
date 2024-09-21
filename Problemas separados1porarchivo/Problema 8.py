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