def solution(A, K):
    n_elem = len(A)
    if not A:
        return A
    rotation = K % n_elem
    if not rotation and K >= n_elem:
        return A
    rotation = K if K < n_elem else rotation
    new_A = list(range(n_elem))

    for i, elem in enumerate(A):
        new_position = i + rotation
        if new_position >= n_elem:
            new_position = i + rotation - n_elem
        new_A[new_position] = elem
    return new_A