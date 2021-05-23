#https://realpython.com/binary-search-python/#analyzing-the-time-space-complexity-of-binary-search
# See also bisect module in python to do binary search https://www.geeksforgeeks.org/bisect-algorithm-functions-in-python/
# https://en.wikipedia.org/wiki/Binary_search_algorithm
def binary_search(sequence, target):
    left = 0
    right = len(sequence) - 1
    while True:
        if right - left < 2:
            if sequence[left] == target:
                return left
            if sequence[right] == target:
                return right
            break
        middle = (left + right) // 2
        if sequence[middle] == target:
            return middle
        if sequence[middle] > target:
            right = middle - 1 #move the upper boundary low (will reduce search space by half on every iteration )
        else:
            left = middle + 1 #move the lower boundary up (will reduce search space by half on every iteration )

# if there was no match, and the function returns None implicitly
sequence = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
target=5
binary_search(sequence, target)
