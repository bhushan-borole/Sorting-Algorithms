def MERGE_SORT(LIST):
    start = []
    end = []
    while len(LIST) > 1:
        a = min(LIST)
        b = max(LIST)
        start.append(a)
        end.append(b)
        LIST.remove(a)
        LIST.remove(b)
    if LIST: start.append(LIST[0])
    end.reverse()
    return (start + end)

A = [1, 2, 3, 9, 8, 7, 6, 5]
print(MERGE_SORT(A))