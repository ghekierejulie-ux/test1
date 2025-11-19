def overzicht(codes):
    telling = {'Engelstalige landen':0, 'Franstalige landen':0,
               'Duitstalige landen':0,
               'Japan':0, 'Russischtalige landen':0, 'China':0,
               'Overige landen':0, 'Fouten':0}

    for code in codes:
        if not (code.startswith('978') or code.startswith('979')):
            telling["Fouten"] +=1
            continue

        som = 0
        for i in range(len(code)-1):
            cijfers = [int(c) for c in code]
            if i%2 ==0:
                som += cijfers[i]
            else:
                som = som + 3*cijfers[i]

        if cijfers[12] != (10-(som)%10)%10 :
                telling["Fouten"] +=1
                continue
        vierde = int(code[3])
        if vierde == 0 or vierde == 1:
            telling["Engelstalige landen"] +=1
        elif vierde == 2:
            telling["Franstalige landen"] +=1
        elif vierde == 3:
            telling["Duitstalige landen"] +=1
        elif vierde == 4:
            telling["Japan"] +=1
        elif vierde == 5:
            telling["Russischtalige landen"] +=1
        elif vierde == 7:
            telling["China"] +=1
        elif vierde == 6 or vierde == 8 or vierde == 9:
            telling["Overige landen"] +=1

    for tel in ["Engelstalige landen", "Franstalige landen","Duitstalige landen", "Japan", "Russischtalige landen", "China", "Overige landen", "Fouten"]:
        print(f"{tel}: {telling[tel]}")

