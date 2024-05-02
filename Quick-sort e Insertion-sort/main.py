import sys
import matplotlib.pyplot as plt
import numpy as np
import time
import random

inf = sys.maxsize

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def QuickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        QuickSort(arr, low, pi - 1)
        QuickSort(arr, pi + 1, high)
    
    
    

def InsertionSort(A):
    for j in range(2,len(A)):
        key = A[j]
        i = j - 1
        while i > 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key


def plotSortGraph(algType, insertType, arrayDim, plot=True):
    x, y = [], []
    for i in range(1, arrayDim, 5):
        x.append(i)
        A = np.arange(i) if insertType == 0 else random.sample(range(i), i)
        if algType == 0:
            start = time.perf_counter()
            InsertionSort(A)
            end = time.perf_counter()
        else:
            start = time.perf_counter()
            QuickSort(A, 0, len(A) - 1)
            end = time.perf_counter()
        z = y[-1] if (len(y) != 0) else 0
        y.append((end - start) / i + z)
    if plot:
        plt.plot(x, y)
        title = 'Insertion-Sort' if algType == 0 else 'Quick-Sort'
        title += ' on Ordered List ' if insertType == 0 else ' on Randomized List '
        title += str(arrayDim)
        plt.title(title)
        plt.show()
    else:
        return x, y


if __name__ == '__main__':
    plt.plot(plotSortGraph(1, 1, 500, False)[0], plotSortGraph(1, 1, 500, False)[1], label='QuickSort')
    plt.plot(plotSortGraph(0, 1, 500, False)[0], plotSortGraph(0, 1, 500, False)[1], label='InsertionSort')
    plt.legend()
    plt.show()