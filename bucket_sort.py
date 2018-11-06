'''
Time Complexity
Best : O(n + k)
Average : O(n + k)
Worst : O(n ^ 2)

Note: This sorting is used for decimal numbers.
'''

def INSERTION_SORT(A):
	for j in range(2, len(A)):
		key = A[j]
		#Insert A[j] into the sorted sequence A[1....j-1]
		i = j - 1

		while i > 0 and A[i] > key:
			A[i + 1] = A[j]
			i -= 1

		A[i + 1] = key
	return A


def BUCKET_SORT(A):
	B = [list() for _ in range(10)]

	for i, x in enumerate(A):
		B[int(x * len(B))].append(x)

	output = []

	for buckets in B:
		output += INSERTION_SORT(buckets)

	return output

A = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
print(BUCKET_SORT(A))




