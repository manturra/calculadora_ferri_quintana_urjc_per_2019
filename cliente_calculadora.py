import socket

puerto = 8080
ip = "10.108.33.37"
def calculadora(cliente):
    condicion = True

    while condicion:
        print("MENU")
        print("\n")
        print("0. Salir")
        print("1. Sumar")
        print("2. Multiplicar")
        print("\n")
        opcion_menu = input("Introduzca la opcion a realizar: ")
        opcion_menu1 = str.encode(opcion_menu)
        cliente.send(opcion_menu1)
        if opcion_menu == "0":
            condicion = False
            print("Usted seleccionó salir.")
            cliente.close()
        else:
            numero1 = str(input("Introduzca el primer numero a operar: "))
            numero1 = str.encode(numero1)
            cliente.send(numero1)
            numero2 = str(input("Introduzca el segundo numero a operar: "))
            numero2 = str.encode(numero2)
            cliente.send(numero2)
            mensaje_servidor = cliente.recv(2048).decode("utf-8")
            print(mensaje_servidor)
            print("\n")

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    cliente.connect((ip, puerto))
    calculadora(cliente)
except KeyboardInterrupt:
    cliente.close()
    print("Usted salió")
