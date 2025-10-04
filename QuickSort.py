def QuickSortApp(A, low, high):

    if low < high:
        pi = Partition(A, low, high)
        QuickSortApp(A, low, pi - 1)
        QuickSortApp(A, pi + 1, high)  

    return A 

def Partition(A, low, high):

    pivot = A[high]
    pivot_pos = low - 1
    
    for j in range(low, high):
        if A[j] <= pivot:
            pivot_pos += 1
            A[pivot_pos], A[j] = A[j], A[pivot_pos]
    
    #posizione finale del pivot
    A[pivot_pos + 1], A[high] = A[high], A[pivot_pos + 1] 

    return pivot_pos + 1

def QuickSort(A):
    return QuickSortApp(A, 0, len(A) - 1)

#questa parte è per testare il codice, deve essere commentata quando si importa il modulo
s = list(map(int, input().split()))
p = QuickSort(s)
print(p)
