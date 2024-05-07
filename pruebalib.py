import mymath

while True:
    print("Seleccione el tipo de conversión:")
    print("1 = Velocidad")
    print("2 = Distancia")
    print("3 = Tiempo")
    print("4 = Volumen del cubo")
    print("5 = Fuerza")
    print("6 = Área")
    print("7 = Trabajo")
    print("8 = Velocidad final")
    print("9 = Velocidad inicial")
    print("10 = Aceleración")
    print("fin = Salir")

    opcion = input("Ingrese la opción que desea llevar a cabo: ")

    if opcion == "fin":
        mymath.calcular(opcion)
        break
    elif opcion in ("1", "2", "3", "4", "5", "7", "8", "9", "10"):
        mymath.calcular(opcion)
    else:
        print("ERROR")