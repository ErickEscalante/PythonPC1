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