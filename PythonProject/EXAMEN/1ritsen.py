def samenvoegen(lijst1, lijst2):
    nieuwelijst = []
    i = 0
    min = len(lijst1) if len(lijst1) < len(lijst2) else len(lijst2)
    while i < min:
        nieuwelijst.append(lijst1[i])
        nieuwelijst.append(lijst2[i])
        i += 1
    return nieuwelijst

print(samenvoegen(('A', 'B', 'C'),  [1, 2 ]))

def weven(lijst1, lijst2):
    nieuwelijst = []
    max = len(lijst1) if len(lijst1) > len(lijst2) else len(lijst2)
    for i in range(max):
        nieuwelijst.append(lijst1[i%len(lijst1)])
        nieuwelijst.append(lijst2[i%len(lijst2)])
    return nieuwelijst
print(weven(('A', 'B', 'C'), [1, 2 ]))

def ritsen(lijst1, lijst2):
    nieuwelijst = []
    min = len(lijst1) if len(lijst1) < len(lijst2) else len(lijst2)
    max = lijst1 if len(lijst1) > len(lijst2) else lijst2
    for i in range(min):
        nieuwelijst.append(lijst1[i])
        nieuwelijst.append(lijst2[i])
    nieuwelijst.extend(max[min:])
    return nieuwelijst
print(ritsen(('A', 'B', 'C'), [1, 2 ]))