'''
Time Complexity
Best : O(nlog(n))
Average : O(nlog(n))
Worst : O(nlog(n))
'''

def MERGE(A,p, q, r):
    L = A[p:q]
    R = A[q:r]
    i = 0
    j = 0
    k = p
    for l in range(k,r):
        if j >= len(R) or (i < len(L) and L[i] < R[j]):
            A[l] = L[i]
            i = i + 1
        else:
            A[l] = R[j]
            j = j + 1  

def mergeSort(A,p,r):
    if r - p > 1:
        q = int((p+r)/2)
        mergeSort(A,p,q)
        mergeSort(A,q,r)
        MERGE(A,p,q,r)

A  = [20, 30, 21, 15, 42, 45, 31, 0, 9]
mergeSort(A,0,len(A))
print(A)


