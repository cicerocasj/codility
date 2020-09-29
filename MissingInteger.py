def solution(A):
    just_positive_ordered = sorted(list(filter(lambda x: x > 0, A)))
    if not just_positive_ordered:
        return 1
    count_index = len(just_positive_ordered) - 1
    if not count_index:
        return 1
    for i, current_value in enumerate(just_positive_ordered):
        if i == count_index:
            return current_value + 1
        else:
            next_value = just_positive_ordered[i + 1]
            if next_value - current_value > 1:
                return current_value + 1
            continue