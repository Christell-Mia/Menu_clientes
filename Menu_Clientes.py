#Menu o gestor para clientes

global diccClien
diccClien = {}

def buscarClient():
    print("Buscar Cliente")
    idC = input("Ingrese Identificacion: ")
    if diccClien.get(idC, 0) == 0:
        print("Cliente No registrado")
    else:
        print(idC, diccClien[idC])


def listarClient():
    print("Listado de Clientes")
    print("Identificador    Nombre ")
    for id, cli in diccClien.items():
        print("  {}             {}".format(id, cli))
def registrarClient():
    print("Registrar Cliente")
    idClient = input("Ingrese su Identificacion ")
    NombreClient = input("Ingrese Nombre: ")
    diccClien [idClient] = NombreClient

def opciones():
    print("\n")
    msg = "Gestor de Clientes"
    print(msg)
    print("_" * len(msg))
    opcmen = {1: "Registrar Clientes" , 2: "Listar Clientes", 3: "Buscar Cliente" , 4: "Salir"}
    for op, opm in opcmen.items():
        print("{}. {}".format(op, opm))

def Menu():
    op = 0

    while op != 4:
        opciones()
        op = int(input("Indique su opción [1..4] -> "))
        if op in range(1,5):
            if op == 1:
                registrarClient()
            elif op == 2:
                listarClient()
            elif op == 3:
                buscarClient()
            else:
                print("...Hasta Pronto")
        else:
            print("Opcion no valida")
Menu()