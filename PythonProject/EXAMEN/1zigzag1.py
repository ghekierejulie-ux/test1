def iszigzag(lijst):
    for i in range(len(lijst)-1):
        if i%2 == 0:
            if lijst[i] < lijst[i+1]:
                return False
            else:
                if lijst[i] > lijst[i+1]:
                    return False

    return True

def zigzag_traag(reeks):
    reeks.sort()
    for i in range(len(reeks)-1,2):
        reeks[i], reeks[i+1] = reeks[i+1], reeks[i]

def zigzag_snel(reeks):
    for i in range(0, len(reeks)-1,2):
        if i < len(reeks)-1 and reeks[i+1] > reeks[i]:
            reeks[i], reeks[i+1] = reeks[i+1], reeks[i]
        if i > 0 and reeks[i] < reeks[i-1]:
            reeks[i], reeks[i-1] = reeks[i-1], reeks[i]

    return reeks

reeks = [10, 90, 49, 2, 1, 5, 23]
print(zigzag_snel(reeks))

print(iszigzag([90, 10, 49, 1, 5, 2, 23]))