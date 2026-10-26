"""
Variables
saldo =1000
Funciones
- Consultar saldo
- Depositar dinero
- Retirar dinero
"""

saldo = 1000


def consultar_saldo(saldo: int):
    return print(f"\nSu saldo es: ${saldo}")


def depositar_saldo(saldo):
    deposito = int(input("Ingrese el valor a depositar: "))
    if deposito <= 0:
        print("\nError, el deposito no puede ser menor o igual a cero.")
    else:
        saldo += deposito
        consultar_saldo(saldo)
    return saldo


def retirar_saldo(saldo):
    retiro = int(input("Ingrese el valor a retirar: "))
    if retiro <= saldo:
        saldo -= retiro
        consultar_saldo(saldo)
    else:
        print("\nSaldo insuficiente")


def mostrar_menu(saldo):
    flag = True
    while flag:
        print("""
===============================
Menu Principal
1. Consultar saldo
2. Depositar dinero
3. Retirar dinero
0. Salir
===============================\n
          """)
        opcion = int(input("Ingrese una opción: "))
        match opcion:
            case 1:
                consultar_saldo(saldo)
            case 2:
                saldo = depositar_saldo(saldo)
            case 3:
                saldo = retirar_saldo(saldo)
            case _:
                print("Ingreso una operación no válida, fin de la operación.")
                flag = False


# Invocar función
mostrar_menu(saldo)
