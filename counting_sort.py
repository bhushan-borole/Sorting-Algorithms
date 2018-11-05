'''
ord() -> This functions inputs a character and returns its ASCII equivalent.

Time Complexity
Best : O(n+k)
Average : O(n+k)
Worst : O(n+k)
'''

def COUNTING_SORT(A):
	
	#intitalize output final array
	output = [0] * 256

	count = [0] * 256

	#storing the count of each character
	for x in A:
		count[ord(str(x))] += 1

	for i in range(256):
		count[i] += count[i - 1]

	for i in range(len(A)):
		output[ count[ord(str(A[i]))] - 1 ] = A[i]
		count[ord(str(A[i]))] -= 1

	for i in range(len(A)):
		A[i] = output[i]

A = [9, 8, 7, 6, 5, 4, 3, 2, 1]
COUNTING_SORT(A)
print(A)
