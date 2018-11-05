'''
We divides the Array into blocks known as Run. 
We sort those runs using insertion sort one by one and then merge those runs using combine function used in merge sort.
If size of Array is less than run, then Array get sorted just by using Insertion Sort.
The size of run may vary from 32 to 64 depending upon size of array. Note that merge function performs well when sizes subarrays are powers of 2. 
The idea is based on the fact that insertion sort performs well for small arrays.

Time Complexity:
Best : O(n)
Average : O(n log(n))
Worst : O(n log(n))
'''

RUN = 32

def MERGE(A, p, q, r):
    L = A[p:q]
    R = A[q:r]
    i = 0
    j = 0
    k = p
    for l in range(k, r):
        if j >= len(R) or (i < len(L) and L[i] < R[j]):
            A[l] = L[i]
            i = i + 1
        else:
            A[l] = R[j]
            j = j + 1

def INSERTION_SORT(A, left, right):
	for i in range(left + 1, right + 1):
		key = A[i]
		#Insert A[j] into the sorted sequence A[1....j-1]
		j = i - 1

		while j >= left and A[j] > key:
			A[j + 1] = A[j]
			j -= 1

		A[j + 1] = key


def TIM_SORT(A):
	for i in range(0, len(A), RUN):
		INSERTION_SORT(A, i, min((i + 31), (len(A) - 1)))

	for size in range(RUN, len(A)):
		for left in range(0, len(A)):
			mid = left + size - 1
			right = min((left + 2*size - 1), (len(A) - 1))
			MERGE(A, left, mid, right)
			left += 2*size
		size *= 2


A = [10183, 75029, 918465, 6029, 5437393, 7649494]
TIM_SORT(A)
print(A)


	



