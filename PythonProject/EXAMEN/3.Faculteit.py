def faculteit_rec(n):
    if n == 0:
        return 1
    if n ==1:
        return 1
    else:
        return n*faculteit_rec(n-1)


aantaltesten = int(input("Aantal testen : "))
for i in range(aantaltesten):
    getal = int(input("Getal?"))
    if getal > 13:
        print("invoer te groot")
    else:
        print(faculteit_rec(getal))