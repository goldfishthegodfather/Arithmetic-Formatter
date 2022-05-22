print("A continuacion tendras que introducir las cuentas matematicas que quieras resolver: ")


def arithmetic_arranger(problems):

    # menos de 5
    cantidad_elementos = len(problems)

    if cantidad_elementos > 5:
        print("Error: Too many problems.")
        exit()

    # solo operador + y /
    for i in problems:

        for e in i:
            if e == "/":
                print("Error: Operator must be '+' or '-'.")
                exit()
            elif e == "*":
                print("Error: Operator must be '+' or '-'.")
                exit()
            else:
                continue
    # detectar que los numeros solo contengan digitos

        a = i.split(" ")

        for i in a[0]:
            if i.isdigit() == False:
                print("Error: Numbers must only contain digits.")
                exit()
            else:
                continue
        for i in a[2]:
            if i.isdigit() == False:
                print("Error: Numbers must only contain digits.")
                exit()
            else:
                continue
    # debo contar que los numeros contengan menos de cuatro digitos

        if len(a[0]) > 4:
            print("Error: Numbers cannot be more than four digits.")
            exit()
        elif len(a[2]) > 4:
            print("Error: Numbers cannot be more than four digits.")
            exit()
        else:
            continue


arithmetic_arranger(["154658 - 1", "2 + 2"])
