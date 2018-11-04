def QUICK_SORT(A, low, high):
	if low < high:
		q = PARTITION(A, low, high)
		QUICK_SORT(A, low, q - 1)
		QUICK_SORT(A, q + 1, high)

def PARTITION(A, low, high):
	pivot = A[high]
	i = low - 1

	for j in range(low, high):
		if A[j] <= pivot:
			i += 1
			A[i], A[j] = A[j], A[i]

	A[i + 1], A[high] = A[high], A[i + 1]
	return i + 1


A = [9, 8, 7, 6, 5, 4, 3]
QUICK_SORT(A, 0, len(A) - 1)
print(A)