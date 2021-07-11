class Solution(object):
    def twoSum(self, nums, target):
        index = {}
        for i, x in enumerate(nums):
            if target - x in index:
                return [index[target - x], i]
            index[x] = i