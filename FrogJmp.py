import math


def solution(X, Y, D):
    if X == Y:
        return 0

    sub = Y - X
    return math.ceil(sub / float(D))