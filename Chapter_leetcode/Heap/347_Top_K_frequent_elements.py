from collections import Counter
def topKFrequent(nums, k) :
    return [number for number, occ in Counter(nums).most_common(k)]