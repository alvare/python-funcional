from random import randint

def quicksort(ls, start, end):
    if start < end:
        pivot = partition(ls, start, end)
        quicksort(ls, start, pivot-1)
        quicksort(ls, pivot+1, end)
    return ls

def partition(ls, start, end):
    pivot = ls[start]
    left = start + 1
    right = end
    done = False
    while not done:
        while left <= right and ls[left] <= pivot:
            left = left + 1
        while ls[right] >= pivot and right >=left:
            right = right -1
        if right < left:
            done= True
        else:
            ls[left], ls[right] = ls[right], ls[left]
    ls[start], ls[right] = ls[right], ls[start]
    return right

unsorted = map(lambda _: randint(0, 100), range(100))
quicksort(unsorted, 0, len(unsorted) - 1)
print unsorted
