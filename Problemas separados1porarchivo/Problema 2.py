consumo = 0
Porcentaje = 0
Propina = 0
print("bienvenido al restaurante 3B")
print("Esperando que le haya gustado su comida ahora vamos a proceder a hacer el cobro por el plato")
consumo = int(input("¿De cuanto fue el consumo que realizo por sus platos? "))
Porcentaje = int(input("¿Cuanto porcentaje le gustaría dejar de propina? "))
Propina = consumo*Porcentaje/100
print(f"¡Perfecto entonces eso sería todo!, muchas gracias por los {Propina}$ de propina")