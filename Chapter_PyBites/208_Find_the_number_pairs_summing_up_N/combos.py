from itertools import combinations

def find_number_pairs(numbers, N=10):
    result = [x for x in combinations(numbers, 2) if sum(x) == N]
    return result
