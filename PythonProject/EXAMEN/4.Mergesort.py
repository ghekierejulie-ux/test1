def mergesort(lst):
    if len(lst) <= 1:
        return lst

    midden = len(lst) // 2
    links = mergesort(lst[:midden])
    rechts = mergesort(lst[midden:])

    return merge(links, rechts)


def merge(links, rechts):
    resultaat = []
    i = j = 0
    while i < len(links) and j < len(rechts):
        if links[i] <= rechts[j]:
            resultaat.append(links[i])
            i += 1
        else:
            resultaat.append(rechts[j])
            j += 1
#voegt de overschot er nog bij::
    resultaat.extend(links[i:])
    resultaat.extend(rechts[j:])