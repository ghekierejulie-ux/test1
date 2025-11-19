def combisom(lijst, doel):
    for i in range(len(lijst)):
        for j in range(len(lijst)):
            if i != j and lijst[i] + lijst[j] == doel:
                return True
    return False
