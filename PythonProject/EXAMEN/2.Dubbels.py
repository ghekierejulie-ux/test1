def dubbel(lijst):
    for i in range(0, len(lijst)):
        for j in range(i+1, len(lijst)):
            if lijst[i] == lijst[j]:
                return lijst[i]
    return None

print(dubbel([1, 2, 3, 4,4]))

print(dubbel([1, 2, 3, 4, 5, 6, 100, -234, 15, 0, -20000, 15]))

def dubbels(lijst):
    dubbelen = set()
    enkelen = set()
    for getal in lijst:
        if getal in enkelen:
            enkelen.remove(getal)
            dubbelen.add(getal)
        elif getal not in dubbelen:
            enkelen.add(getal)
    return (enkelen, dubbelen)
print(dubbels([1, 2, 3, 4, 2]))

