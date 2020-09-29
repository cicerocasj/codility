import string


def solution(N):
    all_letters = string.ascii_lowercase
    if N <= 26:
        return all_letters[:N]
    is_odd_letter = (N % 2) > 0
    letters = ''.join(['x' for i in range(N)])
    if is_odd_letter:
        return letters[2:] + 'yz'
    else:
        return letters[1:] + 'y'

######################
from collections import Counter


def solution(A):
    n_elements = Counter(A)
    if len(n_elements) == 1:
        return False
    ordered_list = sorted(A)
    count_index = len(ordered_list) - 1  # because start with 0

    for i, current_value in enumerate(ordered_list):
        if i < count_index:
            next_value = ordered_list[i + 1]
            if next_value - current_value == 1:
                return True
    return False

######################
TOTAL = 4


def slice_wooden(A, B):
    cut = 2
    while True:
        wooden_cut = int(A / cut)
        how_many_missing = TOTAL - cut
        if how_many_missing:
            missing = wooden_cut * how_many_missing
            if missing <= B:
                return wooden_cut
        else:
            return wooden_cut
        if cut == 4:
            break
        cut += 1
    return 0


def solution(A, B):
    first_case = slice_wooden(A, B)
    second_case = slice_wooden(B, A)
    return max([first_case, second_case])
