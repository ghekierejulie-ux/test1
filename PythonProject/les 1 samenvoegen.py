

def samenvoegen(seq1, seq2):
    """
    Voeg paarsgewijs elementen van seq1 en seq2 samen.
    Stop zodra de kortste reeks op is.
    """
    result = []
    for a, b in zip(seq1, seq2):
        result.extend([a, b])
    return result


def weven(seq1, seq2):
    """
    Voeg paarsgewijs elementen van seq1 en seq2 samen.
    Stop pas als de langste reeks op is.
    Herhaal de kortste reeks cyclisch.
    """
    result = []
    len1, len2 = len(seq1), len(seq2)
    maxlen = max(len1, len2)
    for i in range(maxlen):
        result.append(seq1[i % len1])
        result.append(seq2[i % len2])
    return result


def ritsen(seq1, seq2):
    """
    Voeg paarsgewijs elementen van seq1 en seq2 samen
    tot de kortste reeks op is.
    Daarna de rest van de langste reeks achteraan toevoegen.
    """
    result = []
    minlen = min(len(seq1), len(seq2))
    # Eerst paarsgewijs
    for i in range(minlen):
        result.extend([seq1[i], seq2[i]])
    # Daarna rest van langste
    if len(seq1) > minlen:
        result.extend(seq1[minlen:])
    elif len(seq2) > minlen:
        result.extend(seq2[minlen:])
    return result
