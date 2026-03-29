def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    pass

    # ________________________________________RESOLUCION EJERCICIO 2_______________________________________

    gasto = float(input("Ingresa el gasto: "))
    recibido = int(input("Ingresa el dinero recibido: "))
    vuelto = recibido - gasto

    pesos = int(vuelto)
    centavos = float(round((vuelto - pesos) * 100))

    print("Ingresar gasto:")
    print(gasto)
    print("Dinero recibido")
    print(recibido)
    print("")
    print("Vuelto")
    print("")
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(int(centavos))