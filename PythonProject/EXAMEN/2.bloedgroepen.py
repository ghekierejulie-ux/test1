def bloedgroep_kind(vader, moeder):
    ABO = {
        'A': ['A', 'O'],
        'B': ['B', 'O'],
        'AB': ['A', 'B'],
        'O': ['O', 'O']
    }
    Rh = {
        '+': ['+', '-'],
        '-': ['-', '-'],
    }
    mogelijk = set()
    for a1 in ABO[vader[:-1]]: #zodat het naar de letter kijkt en niet nr + of -
        for a2 in ABO[moeder[:-1]]:
            if a1 == a2 == 'A':
                kind_abo = 'A'
            elif a1 == a2 == 'B':
                kind_abo = 'B'
            elif set([a1, a2]) == set(['A', 'B']):
                kind_abo = 'AB'
            elif set([a1, a2]) == set(['O', 'A']):
                kind_abo = 'A'
            elif set([a1, a2]) == set(['O', 'B']):
                kind_abo = 'B'
            elif a1 == a2 == 'O':
                kind_abo = 'O'
            for r1 in Rh[vader[-1]]:
                for r2 in Rh[moeder[-1]]:
                    if '+' in [r1, r2]:
                        kind_rh = '+'
                    else:
                        kind_rh = '-'
                    mogelijk.add(kind_abo + kind_rh)
    return mogelijk

def bloedgroep_ouder(ouder, kind): #KIND
    bloedgroepen = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
    mogelijk = set()
    for bloedgroep in bloedgroepen:
        if kind  in bloedgroep_kind(ouder, bloedgroep):
            mogelijk.add(bloedgroep)
    return mogelijk