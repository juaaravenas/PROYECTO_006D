def showmenu(titulo,lista_opc):
    print(titulo)
    for opcion in lista_opc:
        print(opcion)

def valida_opcion(cantidad_opcion):
    ingreso_ok = True
    while ingreso_ok:
        try:
            opcion = int(input("Ingrese la opcion seleccionada "))
            if opcion <= 0  or  opcion > cantidad_opcion:
                print("ERROR:  Opción invalida ")
            else:
                ingreso_ok = False
                return opcion
        except:
            print("ERROR:  El valor debe ser numerico.")    




lineas_menu = []
titulo_menu = "TOTEM AUTOATENCIÓN RESERVA STRIKE" 
lineas_menu.append("1.- Reservar zapatillas") 
lineas_menu.append("2.- Buscar zapatillas reservadas.") 
lineas_menu.append("3.- Ver stock de reservas.") 
lineas_menu.append("4.- Ver stock ocupado.") 
lineas_menu.append("5.- Salir.") 

showmenu(titulo_menu,lineas_menu)
opcion_elegida = valida_opcion(len(lineas_menu))

print(opcion_elegida)
