import funciones as fn
while True:
        print("Bienvenido a Gaxplosive?")
        print (" 1.Registrar pedido ")
        print (" 2.Listar los todos los pedidos")
        print (" 3.Imprimir hoja de ruta")
        print (" 4.Salir del programa ")       

        opcion = int(input("Ingrese la opcion que desea "))

        if opcion == 1:
            fn.registrar_cliente(cliente)
        elif opcion == 2:
             print("")
        elif opcion == 3:
             print("")
        elif opcion == 4:
                break
        else:
             print("Ingrese una opción válida")

