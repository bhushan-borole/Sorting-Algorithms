def MERGE_SORT(A):
    start = []
    end = []
    while len(A) > 1:
        a = min(A)
        b = max(A)
        start.append(a)
        end.append(b)
        A.remove(a)
        A.remove(b)
    if A: start.append(A[0])
    end.reverse()
    return (start + end)

A = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(MERGE_SORT(A))
