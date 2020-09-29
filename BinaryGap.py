import sys


def solution(A, K):
    # write your code in Python 3.6
    n_elem = len(A)
    rotation = n_elem % K
    if not rotation:
        return A
    rotation = K if K < n_elem else rotation
    new_A = list(range(n_elem))

    for i, elem in enumerate(A):
        new_position = i + rotation
        if new_position >= n_elem:
            new_position = i + rotation - n_elem
        new_A[new_position] = elem
    return new_A


if __name__ == '__main__':
    print(solution([1, 1, 2, 3, 5] , 2))
