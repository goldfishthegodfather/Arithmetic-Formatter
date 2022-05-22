def arithmetic_arranger(problems, resultado=False):
    cantidad_elementos = len(problems)

    if cantidad_elementos > 5:
        print("Error: Too many problems.")

    if resultado == True:
        print("se imprime resultado")
    else:
        print("no se imprime resultado")


arithmetic_arranger(["1 / 1", "2 + 2"])
