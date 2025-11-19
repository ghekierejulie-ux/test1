def woorden_splitsen(txt):
    file = open(txt, 'r')
    inhoud = file.read()
    woorden = inhoud.split()
    gestript = []
    for woord in woorden:
        woordje = woord.strip('?;:.(),')
        gestript.append(woordje)
    return gestript

def woorden_tellen(txt):
    telling = {}
    woorden = woorden_splitsen(txt)
    for woord in woorden:
        if woord in telling:
            telling[woord] +=1
        else:
            telling[woord] = 1
    return telling
