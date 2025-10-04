#Counting Sort, conta il numero di occorrenze di ogni elemento in un array e lo ordina
#implementazione con numeri positivi e negativi
def CountingSort(A):

    min_val = min(A)
    max_val = max(A)
    offset = -min_val

    count = [0] * (max_val - min_val + 1)
    copy = [0] * len(A)

    # Conta le occorrenze
    i = 0
    for num in A:
        count[num + offset] += 1
        copy[i] = num
        i += 1

    # Calcolo indirizzo piu' a destra di un elemento in posizione i in count
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(len(A) - 1, -1, -1):
        num = copy[i]
        count[num + offset] -= 1
        A[count[num + offset]] = num

    return A


#questa parte è per testare il codice, deve essere commentata quando si importa il modulo
s = list(map(int, input().split()))
p = CountingSort(s)
print(p)


'''
#implementazione con solo numeri positivi
def CountingSort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    
    copy = [0] * len(arr)
    i = 0
    for num in arr:
        count[num] += 1
        copy[i] = num
        i += 1
    
    index = 0

    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    for i in range(len(arr) - 1, -1, -1):
        num = copy[i]
        index = count[num] - 1
        count[num] -= 1
        arr[index] = num

    return arr
'''
