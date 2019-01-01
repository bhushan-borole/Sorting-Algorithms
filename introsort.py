import math


def heap_sort(A):
    heap_size = build_max_heap(A)

    for i in range(len(A)-1, 1, -1):
        A[0], A[i] = A[i], A[0]
        heap_size -= 1
        max_heapify(A, 0, heap_size)

def build_max_heap(A):
    heap_size = len(A)

    for i in range(int(len(A)/2), -1, -1):
        max_heapify(A, i, heap_size)
    return heap_size

def max_heapify(A, i, heap_size):
    l = 2 * i + 1
    r = 2 * i + 2

    #check if left side of root exists and is greater than root.
    if l < heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i

    #check if right side of root exists and is greater than root.
    if r < heap_size and A[r] > A[largest]:
        largest = r

    #change root if needed
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest, heap_size)

def introsort(A):
    maxdepth = (len(A).bit_length() - 1)*2
    introsort_helper(A, 0, len(A), maxdepth)
 
def introsort_helper(A, start, end, maxdepth):
    if end - start <= 1:
        return
    elif maxdepth == 0:
        heap_sort(A[start:end])
    else:
        p = partition(A, start, end)
        introsort_helper(A, start, p - 1, maxdepth - 1)
        introsort_helper(A, p + 1, end, maxdepth - 1)
 
def partition(A, start, end):
    pivot = A[start]
    i = start - 1
    j = end
 
    while True:
        i = i + 1
        while A[i] < pivot:
            i = i + 1
        j = j - 1
        while A[j] > pivot:
            j = j - 1
 
        if i >= j:
            return j
 
        A[i], A[j] = A[j], A[i]


A = [22, 78, 1, 34, 89, 423, 78, 43]
introsort(A)
print(A)