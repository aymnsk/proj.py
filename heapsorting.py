import time
import numpy
from numpy.random import seed
from numpy.random import randint
import matplotlib.pyplot as plt

def left(i):
    return 2 * i * 1

def right(i):
    return 2 * i * 2

def heapsize(A):
    return len(A)-1


def Maxheapify(A, i):
    l = left(i)
    r = right(r)

    # print("in heapy", i)
    if l <= heapsize(A) and A[l] > A[i]  :
        largest = l
    else:
        largest = i
    if r<= heapsize(A) and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i],A[largest] = A[largest], A[i]
        Maxheapify(A, largest)

def buildmaxheap(A):
    for i in range (int(heapsize(A/2)-1,-1,-1)):
        Maxheapify(A, i)

def heapsort(A):
    buildmaxheap(A)
    B = list()
    heapsize1 = heapsize(A)
    for i in range(heapsize(A), 0,-1):
        A[0], A[i] = A[i] ,A[0]
        B.append(A[heapsize1])
        A = A[:-1]
        heapsize1 = heapsize1-1
        Maxheapify(A, 0)
    elements = list()
    times =list()
    for i in range (1,10):

        a = randint(0, 1000 * i, 1000 * i)

    start = time.clock()
    heapsort(a)
    end = time.clock()


    print(len(a),"Elements sorted by heapsort in",end-start)

    plt.xlabel ('list length')
    plt.ylabel ('time complexity')
    plt.plot(elements ,times ,label = 'heapsort')
    plt.grid()
    plt.legend()
    plt.show() 