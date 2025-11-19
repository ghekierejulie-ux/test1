numlist = [ 100, 101, 0, "103", 104 ]

try:
    i1 = int(input("Give an index: "))
    print("100 /", numlist[i1], "=", 100 / numlist[i1])
except ValueError:
    print("Please enter an integer")
except IndexError:
    print("not a valid index")
except ZeroDivisionError:
    print("division by zero")
except TypeError:
    print("Please enter a number")