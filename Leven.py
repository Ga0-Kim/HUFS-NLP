def LevenDist(x,y) :
    if x == y:
        return 0
    elif len(x) == 0:
        return len(y)
    elif len(y) ==0 :
        return len(x)

    x = ("#" +x)
    y = ("#" +y)

    Prev_D = [0] *(len(x))
    Pres_D = [0] * (len(x))

    for i in  range(len(Prev_D)) :
        Prev_D[i] = i
    print(Prev_D)


    for j in range(1, len(y)) :
        for i in range(1, len(x))  :
            if x[i] == y[j] :
                cost = 0
            else :
                cost = 2

            Pres_D[0] = Prev_D[0] + 1
            Pres_D[i] = min(Pres_D[i-1] +1 , Prev_D[i]+)

        for i in range(len(x)) :
            Prev_D[i] = Pres_D[i]

        print(Prev_D)


    print("Distance between the two ward", Prev_D)

LevenDist("cake", "cat")
