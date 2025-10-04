def CycleSort(A):
    n = len(A)

    # Scorri ogni elemento tranne l'ultimo
    for start in range(n - 1):
        item = A[start]      # Elemento corrente da posizionare
        pos = start          # Posizione dove dovrebbe andare 'item'

        # Conta quanti elementi a destra sono minori di 'item'
        for i in range(start + 1, n):
            if A[i] < item:
                pos += 1

        # Se è già nella posizione giusta, salta
        if pos == start:
            continue

        # Se ci sono duplicati, salta le posizioni occupate
        while item == A[pos]:
            pos += 1

        # Scambia l'elemento con quello nella sua posizione corretta
        A[pos], item = item, A[pos]

        # Continua a ciclare gli elementi finché non si chiude il ciclo
        while pos != start:
            pos = start
            # Ricalcola la posizione corretta dell'item corrente
            for i in range(start + 1, n):
                if A[i] < item:
                    pos += 1

            # Salta eventuali duplicati
            while item == A[pos]:
                pos += 1

            # Scambia nuovamente
            A[pos], item = item, A[pos]

    return A



#questa parte è per testare il codice, deve essere commentata quando si importa il modulo
s = list(map(int, input().split()))
p = CycleSort(s)
print(p)
