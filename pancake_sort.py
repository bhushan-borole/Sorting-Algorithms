'''
'''
def PANCAKE_SORT(A):
	cur = len(A)

	while cur > 1:
		# find the index of the max element
		mi = A.index(max(A[:cur]))
		# reverse list from 0 to mi
		A = A[mi::-1] + A[mi + 1:]
		# reverse the whole list
		A = A[cur - 1::-1] + A[cur:]

		cur -= 1
	return A

A = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(PANCAKE_SORT(A))