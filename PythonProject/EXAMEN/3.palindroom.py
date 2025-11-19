def isPalindroom(woord):
        return IspalindroomHelper(woord, 0, len(woord)-1)

def IspalindroomHelper(woord, low, high):
    if high <= low:
        return True
    elif woord[low] != woord[high]:
        return False
    else:
        return IspalindroomHelper(woord, low+1, high-1)

print(isPalindroom("lepel"))
print(isPalindroom("julie"))
print(isPalindroom("lol"))