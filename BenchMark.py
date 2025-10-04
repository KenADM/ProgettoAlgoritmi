import time
import random
import math
import matplotlib.pyplot as plt
from CycleSort import CycleSort
from CountingSort import CountingSort
from QuickSort import QuickSort
from ThreeWayQuickSort import ThreeWayQuickSort

##intervallo del clock minimo di sistema
def resolution():
    start = time.perf_counter()
    while time.perf_counter() == start:
        pass
    stop = time.perf_counter()
    return stop - start

## Calcola il tempo medio di esecuzione dell'algoritmo alg su un array di lunghezza n con valori compresi tra 0 e m
def ExecutionTimeMedian(m,n,alg,min_time):
    count = 0
    start = time.perf_counter()

    while True:
        target = ArrayGenerator(n, m)
        alg(target)
        count += 1
        stop = time.perf_counter()
        if stop - start >= min_time:
            break
    
    return (stop - start) / count

# genera array secondo caratteristiche specificate
# n: lunghezza dell'array
# m: valore massimo degli elementi dell'array
def ArrayGenerator(n, m):
    arr = [0] * n

    for i in range(0, n):
        arr[i] = random.randint(0, m)

    return arr

# Funzione per eseguire il benchmark di un algoritmo su un intervallo di dimensioni e valori
# per dimensione dell'array crescente
def Benchmark( min, max, m, alg1,alg2,alg3,alg4, n_points, min_time):
    f = open("data.txt", "w")
    A = min
    B = (max / min) ** (1 / (n_points - 1))

    points = [(None, None, None, None, None)] * n_points

    for i in range(0, n_points):
        size = math.floor(A*(B**i))

        time_1 = time_2 = time_3 = time_4 = 0 

        time_1 = ExecutionTimeMedian(m, size, alg1, min_time)
        time_2 = ExecutionTimeMedian(m, size, alg2, min_time)
        time_3 = ExecutionTimeMedian(m, size, alg3, min_time)
        time_4 = ExecutionTimeMedian(m, size, alg4, min_time)


        points[i] = (size, time_1, time_2, time_3, time_4)
        print(f"n: {size}, time: {time_1:.8f}, time2: {time_2:.8f}, time3: {time_3:.8f}, time4: {time_4:.8f}")
        with open("data.txt", "a") as f:
            f.write(f"{size} {time_1:.8f} {time_2:.8f} {time_3:.8f} {time_4:.8f}\n")
        
        f.close()
    return points


# Funzione per eseguire il benchmark di un algoritmo su un intervallo di dimensioni e valori
# per dimensione del range crescente
def Benchmark_values( min, max, n, alg1,alg2,alg3,alg4, n_points, min_time):
    f = open("data_value.txt", "w")
    A = min
    B = (max / min) ** (1 / (n_points - 1))

    points = [(None, None, None, None, None)] * n_points

    for i in range(0, n_points):
        values = math.floor(A*(B**i))

        time_1 = time_2 = time_3 = time_4 = 0 

        time_1 = ExecutionTimeMedian(values, n, alg1, min_time)
        time_2 = ExecutionTimeMedian(values, n, alg2, min_time)
        time_3 = ExecutionTimeMedian(values, n, alg3, min_time)
        time_4 = ExecutionTimeMedian(values, n, alg4, min_time)


        points[i] = (values, time_1, time_2, time_3, time_4)
        print(f"n: {values}, time: {time_1:.8f}, time2: {time_2:.8f}, time3: {time_3:.8f}, time4: {time_4:.8f}")
        with open("data_value.txt", "a") as f:
            f.write(f"{values} {time_1:.8f} {time_2:.8f} {time_3:.8f} {time_4:.8f}\n")
        
        f.close()
    return points

# Funzione per disegnare un grafico con tutti gli algoritmi
def draw_graph_all(points, x_label, double_log,label_1, label_2, label_3, label_4):
    plt.rcParams.update({'font.size': 22})

    plt.xlabel(x_label)
    plt.ylabel('Tempo (secondi)')
    plt.title("Scala lineare")  
    if double_log:

        plt.xscale('log')
        plt.yscale('log')

        plt.title("Scala doppio logaritmica")
    
    plt.grid()
    x, y1, y2, y3, y4 = zip(*points)
    plt.plot(x, y1, marker=".", color="blue", label=label_1)
    plt.plot(x, y2, marker=".", color="red", label=label_2)
    plt.plot(x, y3, marker=".", color="green", label=label_3)
    plt.plot(x, y4, marker=".", color="magenta", label=label_4)

    plt.legend()
    plt.show()

# Funzione per disegnare un grafico con tutti un algoritmo
def draw_graph_single(points, x_label, double_log,label_1, colour):
    # Modifica la dimensione del font del grafico
    plt.rcParams.update({'font.size': 22})

    plt.xlabel(x_label)
    plt.ylabel('Tempo (secondi)')
    plt.title("Scala lineare")  
    if double_log:

        plt.xscale('log')
        plt.yscale('log')

        plt.title("Scala doppio logaritmica")
    
    plt.grid()
    x, y1 = zip(*points)
    plt.plot(x, y1, marker=".", color=colour, label=label_1)

    plt.legend()

    plt.show()

if __name__ == "__main__":
    
    E = 0.001  # errore relativo massimo di misurazione 
    Tmin = resolution() * (1 / E + 1)  # tempo minimo misurabile
    
    # lunghezza array 
    nMin = 100       
    nMax = 100000 
    #range valori
    mMin = 10    
    mMax = 1000000
    #fisso un m e un n
    m = 100000 
    n = 10000 
    n_points = 100
    points_range = [(None, None, None, None, None)] * n_points
    points = [(None, None, None, None, None)] * n_points

    
    #calcolo i tempi di esecuzione per un range di valori
    points_range = Benchmark_values(mMin,mMax,n,CountingSort,QuickSort,ThreeWayQuickSort,CycleSort,n_points, Tmin)
    
    #calcolo i tempi di esecuzione per diverse lunghezze
    points = Benchmark(nMin,nMax,m,CountingSort,QuickSort,ThreeWayQuickSort,CycleSort,n_points, Tmin)



    # Disegna i grafici per il range di valori crescente --------------------------------------------------------------
    f = open("data_value.txt", "r")
    count = 0
    for i in range(0, n_points ):
        points_range[i] = list(map(float, f.readline().split()))
        print(points_range[i])
            
    
    draw_graph_all(points_range, "Range Valori", False, "Counting","QuickSort", "Quicksort3way", "CycleSort")
    draw_graph_all(points_range, "Range Valori", True, "Counting","QuickSort", "Quicksort3way", "CycleSort")
    
    points1 = [(None)] * n_points
    points2 = [(None)] * n_points
    points3 = [(None)] * n_points
    points4 = [(None)] * n_points

    for i in range(0, n_points):
        points1[i] = (points_range[i][0], points_range[i][1])
        points2[i] = (points_range[i][0], points_range[i][2])
        points3[i] = (points_range[i][0], points_range[i][3])
        points4[i] = (points_range[i][0], points_range[i][4])

    draw_graph_single(points1, "Range Valori", True, "Counting","magenta")
    draw_graph_single(points2, "Range Valori", True, "QuickSort","magenta")
    draw_graph_single(points3, "Range Valori", True, "Quicksort3way","magenta")
    draw_graph_single(points4, "Range Valori", True, "CycleSort","magenta")

    draw_graph_single(points1, "Range Valori", False, "Counting","magenta")
    draw_graph_single(points2, "Range Valori", False, "QuickSort","magenta")
    draw_graph_single(points3, "Range Valori", False, "Quicksort3way","magenta")
    draw_graph_single(points4, "Range Valori", False, "CycleSort","magenta")
    
    f.close()

    #disegna i grafici per la lunghezza dell'array crescente --------------------------------------------------------------
    f = open("data.txt", "r")
    count = 0
    for i in range(0, n_points ):
        points[i] = list(map(float, f.readline().split()))
        print(points[i])
            
    
    draw_graph_all(points, "Lunghezza array", False, "Counting","QuickSort", "Quicksort3way", "CycleSort")
    draw_graph_all(points, "Lunghezza array", True, "Counting","QuickSort", "Quicksort3way", "CycleSort")
    
    points1 = [(None)] * n_points
    points2 = [(None)] * n_points
    points3 = [(None)] * n_points
    points4 = [(None)] * n_points

    for i in range(0, n_points):
        points1[i] = (points[i][0], points[i][1])
        points2[i] = (points[i][0], points[i][2])
        points3[i] = (points[i][0], points[i][3])
        points4[i] = (points[i][0], points[i][4])

    draw_graph_single(points1, "Lunghezza array", True, "Counting","green")
    draw_graph_single(points2, "Lunghezza array", True, "QuickSort","green")
    draw_graph_single(points3, "Lunghezza array", True, "Quicksort3way","green")
    draw_graph_single(points4, "Lunghezza array", True, "CycleSort","green")

    draw_graph_single(points1, "Lunghezza array", False, "Counting","green")
    draw_graph_single(points2, "Lunghezza array", False, "QuickSort","green")
    draw_graph_single(points3, "Lunghezza array", False, "Quicksort3way","green")
    draw_graph_single(points4, "Lunghezza array", False, "CycleSort","green")
    
    f.close()
