def combisom(nummers, doel):
    n = len(nummers)
    for i in range(n):
        for j in range(i+1, n): #start bij i+1 zodat je niet hetzelfde element dubbel gebruikt
            if nummers[i] +nummers[j] == doel:
                return True
    return False