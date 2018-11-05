'''
Time Complexity
Best : O(n)
Average : O(n^2)
Worst : O(n^2)
'''

def BUBBLE_SORT(A):
	n = len(A)
	for i in range(n - 1):
		for j in range(n - 1):
			if A[j] > A[j + 1]:
				A[j], A[j + 1] = A[j + 1], A[j]

A = [9, 8, 7, 6, 5, 4, 3, 2, 1]
BUBBLE_SORT(A)
print(A)