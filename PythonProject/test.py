def hanoi(n, van = 'A', naar ='C', hulp = 'B'):
    count = 0

    def move(k, van, naar, hulp):
        nonlocal count
        if k==1:
            print(f"schijf 1 van {van} naar {naar}")
            count += 1
        else:
            move(k-1, van, hulp, naar)
            print (f"schijf {k} van {van} naar {naar}")
            count += 1
            move(k-1, hulp, naar, van)

        move(n, van, naar, hulp)
        print(f"{count} stappen gedaan")