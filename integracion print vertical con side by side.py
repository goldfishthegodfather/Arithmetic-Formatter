arithmetic_arranger = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

for i in arithmetic_arranger:

    a = i.split(" ")
    # print(i[0]"\n" + i[1]+i[2])
    if a[1] == "+":

        var1 = int(a[0])
        var2 = int(a[2])
        res = int(var1+var2)

        # falta integrar los dos print
        print((a[0]).rjust(7) + "\n" + (a[1] + " " +
              a[2]).rjust(7) + "\n" + "------".rjust(7))
        print(str(res).rjust(7))

    if a[1] == "-":

        var1 = int(a[0])
        var2 = int(a[2])
        res = int(var1-var2)
        print((a[0]).rjust(7) + "\n" + (a[1] + " " +
              a[2]).rjust(7) + "\n" + "------".rjust(7))
        print(str(res).rjust(7))


'''lista=[11, 123, 453, 6546, 87]
print(lista, end= " ")


arithmetic_arranger=["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]



for i in arithmetic_arranger:

    a=i.split(" ")
    #print(i[0]"\n" + i[1]+i[2])
    if a[1]== "+":

        var1=int(a[0])
        var2=int(a[2])
        res=int(var1+var2)
        print((a[0]).rjust(7) + "\n" + (a[1] +" "+ a[2]).rjust(7) + "\n" + "------".rjust(7))
        print(str(res).rjust(7))

    if a[1]== "-":

        var1=int(a[0])
        var2=int(a[2])
        res=int(var1-var2)
        print((a[0]).rjust(7) + "\n" + (a[1] +" "+ a[2]).rjust(7) + "\n" + "------".rjust(7))
        print(str(res).rjust(7))'''
