

def arithmetic_arranger(problems, resultado=False):

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

    # variable que nos devuelve el elemento 0 del split de cada elemento i en problemas
    a1 = [i.split(" ")[0] for i in problems]
    # variable que nos devuelve el elemento 2 del split de cada elemento en los i elementos de la lista problemas
    a2 = [i.split(" ")[2] for i in problems]
    # variable que nos devuelve el elemento 1 del split de cada elemento en los i elementos de la lista problemas
    b = [i.split(" ")[1] for i in problems]

    answer = ""
    # print primer numero
    #cantidad_elementos= len(problems)
    for i in range(cantidad_elementos):

        # queremos saber cual longitur es mas larga para aplicar bien los espacios
        if len(a1[i]) < len(a2[i]):

            # abs() devuelve el valor absoluto de un elemento i
            # entonces multimplicamos los espacios por la diferencia entre los valores absolutos del largo de los numeros

            answer += (" " * abs(len(a1[i])-len(a2[i])))
        answer += ("  ")

        answer += (a1[i] + "    ")

    answer += "\n"

    # print operador + segundo numero
    for i in range(cantidad_elementos):
        answer += (b[i] + " ")

        if len(a1[i]) > len(a2[i]):
            answer += (" " * abs(len(a1[i])-len(a2[i])))

        answer += (a2[i] + "    ")

    answer += "\n"

    # print de guiones
    for i in range(cantidad_elementos):
        answer += ("-" * (max(len(a1[i]), len(a2[i])) + 2) + "    ")
    answer += "\n"

    # cuando nos pasen el parametro en verdadero imprimiremos los resultados

    if resultado == True:

        solucion = [eval(problems[i]) for i in range(cantidad_elementos)]
        for i in range(cantidad_elementos):
            answer += (" " *
                       (max(len(a1[i]), len(a2[i])) + 2 - len(str(solucion[i]))))
            answer += (str(solucion[i]) + "    ")
    print(answer)


arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43",
                    "123 + 49", "58 + 45"], resultado=True)
