def sort(lijst):

    def quicksort(l, left, right):
        if left >= right:
            return lijst

        pivot = l[left]
        i = left + 1
        j = right

        while i <=j:
            while i <= j and l[i] < pivot:
                i += 1
            while i <= j and l[j] > pivot:
                j -= 1
            if i <= j:
                l[i], l[j] = l[j], l[i]
                i += 1
                j -= 1

        # pivot op juiste plaats zetten
        l[left], l[j] = l[j], l[left]

        # recursief links en rechts sorteren
        quicksort(l, left, j - 1)
        quicksort(l, j + 1, right)

    quicksort(lijst, 0, len(lijst) - 1)