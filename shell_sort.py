'''
The idea of shellSort is to allow exchange of far items. 
In shellSort, we make the array h-sorted for a large value of h.

Time Complexity 
Best : O(n log(n))
Average : O(n(log(n))^2)
Worst : O(n(log(n))^2)
'''

def SHELL_SORT(A):
	length = len(A)
	#initalize gap to mid of the array
	gap = length // 2

	while gap > 0:
		for i in range(gap, length):
			temp = A[i]
			j = i

			while j >= gap and A[j - gap] > temp:
				A[j] = A[j - gap]
				j -= gap

			A[j] = temp
		gap = gap // 2


A = [9, 8, 7, 6, 5, 4, 3, 2, 1]
SHELL_SORT(A)
print(A)