def sort(lijst: list):
    def quicksort(l, low, high):
        if low < high:
            p = partition(l, low, high)
            quicksort(l, low, p - 1)
            quicksort(l, p + 1, high)

    def partition(l, low, high):
        pivot = l[low]         # eerste element als spil
        i = low + 1
        j = high

        while True:
            # zoek van links naar een element groter dan pivot
            while i <= j and l[i] <= pivot:
                i += 1
            # zoek van rechts naar een element kleiner dan pivot
            while i <= j and l[j] >= pivot:
                j -= 1
            if i <= j:
                # wissel om
                l[i], l[j] = l[j], l[i]
            else:
                break

        # zet de pivot op de juiste plek
        l[low], l[j] = l[j], l[low]
        return j  # nieuwe index van de pivot

    quicksort(lijst, 0, len(lijst) - 1)
