from collections import Counter


def solution(A):
    counter = Counter(A)
    counter_sorted = sorted(counter, key=counter.get, reverse=True)
    return counter_sorted[-1]

if __name__ == '__main__':
    print(solution([1,2,1,2,3,50,4,4,3,8,50]))