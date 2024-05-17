def cap (ent):
    num = int(ent)
    x = [str(a) for a in str(num)]
    listaa =[]
    i = 0
    for i in range (len(x)):
        listaa.append(x[i])
        if listaa[i] != "0" and listaa[i] != "1":
            print("Error")
        else:
            print(listaa[i])
        i += 1

nuu = "1013254"
cap(nuu)