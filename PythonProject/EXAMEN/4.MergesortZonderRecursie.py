def sorteer(rij):
    size = 1
    while size < len(rij):     # Zolang de blokgrootte kleiner is dan de lijst
        nieuw = []
        # Neem telkens 2 stukjes van lengte 'size'
        for i in range(0, len(rij), 2 * size):
            left = rij[i:i + size]
            right = rij[i + size:i + 2 * size]
            # Merge ze samen
            j = k = 0
            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    nieuw.append(left[j])
                    j += 1
                else:
                    nieuw.append(right[k])
                    k += 1
            nieuw.extend(left[j:])
            nieuw.extend(right[k:])
        rij[:] = nieuw # vervang de oude lijst met de nieuwe
        size *= 2 # volgende ronde: grotere stukjes