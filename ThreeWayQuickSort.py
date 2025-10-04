#quick sort 3 way, quicksort a 3 way partitioning, per numeri minori,uguali e maggiori di un pivot

def threeWaySort(A, low, high):

    if low < high:
        lt, gt = threeWayPartition(A, low, high)
        threeWaySort(A, low, lt - 1)
        threeWaySort(A, gt + 1, high)

    return A

def threeWayPartition(A, low, high):

    pivot = A[low]
    lt = low      # A[low..lt-1] < pivot
    gt = high     # A[gt+1..high] > pivot
    i = low       # A[lt..i-1] == pivot

    while i <= gt:
        if A[i] < pivot:
            A[lt], A[i] = A[i], A[lt]
            lt += 1
            i += 1
        elif A[i] > pivot:
            A[i], A[gt] = A[gt], A[i]
            gt -= 1
        else:
            i += 1
            
    return lt, gt

def ThreeWayQuickSort(A):
    return threeWaySort(A, 0, len(A) - 1)

#questa parte è per testare il codice, deve essere commentata quando si importa il modulo
s = list(map(int, input().split()))
p = ThreeWayQuickSort(s)
print(p)
