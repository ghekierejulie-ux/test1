def zoek(gesorteerd: list, x: int): #dit eig niet in les gzn
    low = 0 #zoals in les gezien
    high = len(gesorteerd) - 1 #zoals in les gezien

    while low <= high:
        mid = (low + high) // 2
        if x < gesorteerd[mid]:
            high = mid - 1
        elif x > gesorteerd[mid]:
            low = mid + 1
        else:
            return mid  # gevonden

    return None  # niet gevonden