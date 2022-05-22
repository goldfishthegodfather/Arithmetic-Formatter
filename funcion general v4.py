

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

    #a1 = [i.split(" ")[0] for i in problems]
    #a2 = [i.split(" ")[2] for i in problems]
    answer = ""

    for i in range(cantidad_elementos):
        if len(a[0]) < len(a[2]):
            answer += (" " * abs(len(a[0])-len(a[2])))
        answer += ("  ")

        answer += (a[0] + "    ")

    answer += "\n"
    for i in range(cantidad_elementos):
        answer += (a[1] + " ")

        if len(a[0]) > len(a[2]):
            answer += (" " * abs(len(a[0])-len(a[2])))

        answer += (a[2] + "    ")

    answer += "\n"
    for i in range(cantidad_elementos):
        answer += ("-" * (max(len(a[0]), len(a[2])) + 2) + "    ")
    answer += "\n"

    if resultado:
        solutions = [eval(problems[i]) for i in range(len(problems))]
        for i in range(len(problems)):
            answer += (" " * (max(len(a[0]), len(a[2])
                                  ) + 2 - len(str(solutions[i]))))
        answer += (str(solutions[i]) + "    ")
    print(answer)


arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43",
                    "123 + 49"], resultado=True)
