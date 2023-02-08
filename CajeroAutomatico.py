def menu():
    print("Cajero automático")
    print("1. Consignar")
    print("2. Retirar")
    print("3. Consultar")
    opcion = int(input("Seleccione una opción: "))
    return opcion

def consignar(saldo):
    monto = int(input("Ingrese el monto a consignar: "))
    saldo += monto
    return saldo

def retirar(saldo):
    monto = int(input("Ingrese el monto a retirar: "))
    if monto > saldo:
        print("Saldo insuficiente")
    else:
        saldo -= monto
    return saldo

def consultar(saldo):
    print("Su saldo actual es:", saldo)

saldo = 0
opcion = 0
while opcion != 4:
    opcion = menu()
    if opcion == 1:
        saldo = consignar(saldo)
    elif opcion == 2:
        saldo = retirar(saldo)
    elif opcion == 3:
        consultar(saldo)

