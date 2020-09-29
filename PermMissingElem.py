def solution(A):
    if not A:
        return 1
    list_ordered = sorted(A)
    for i, current in enumerate(list_ordered[1:]):
        previous = list_ordered[i]
        if current - previous > 1:
            result = previous + 1
            return result
    if list_ordered[0] == 2:
        return 1
    return list_ordered[-1] + 1
filter