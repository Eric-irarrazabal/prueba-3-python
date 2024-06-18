CILINDROS = ["Cil. 5kg", "Cil. 15kg", 	"Cil. 45kg" ]

SECTOR = ["Centro, Colina, Industrias" ]


listacliente = []
resp = "si"


def registrar_cliente(cliente)
      while True:
        nombre = input("Ingrese su nombre: ")
        comuna = input("Ingrese su comuna: ")
        pedido = int(input("Favor Ingrese Cantidad de Cilindros de 5, 15 y 45 kilos: "))
        print("")
        resp = input("Desea ingresar otro cliente? (si/no): ").lower()
        if resp == "no":
             break
      

listacliente.append(cliente)



cliente = {
            "nombre" : nombre,
            "comuna" : comuna,
            "detalle del pedido" : pedido
        }

while True:
     print("Cilindros Disponibles")
     print("1.- Cilindro 5kg")
     print("2- Cilindro 15kg")
     print("3- Cilindro 45kg")
     print("4.- Salir del programa")

     opcioncilindro = int(input("Ingrese el tipo de cilindro que desee"))

     if opcioncilindro == 1:
           cantcil5 = int(input("Ingrese la cantidad de cilindro que desea"))
     elif opcioncilindro == 2:
           cantcil15 = int(input("Ingrese la cantidad de cilindro que desea"))
     elif opcioncilindro == 3:
           cantcil45 = int(input("Ingrese la cantidad de cilindro que desea"))
     elif opcioncilindro == 4:
           break
     else:
           print("Ingrese una opción válida")
       