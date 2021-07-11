class Solution(object):
def twoSum(self, nums, target):
    dic = {}
    for i, n in enumerate(nums): 
        if n in dic:
            return [dic[n], i]
        dic[target-n] = i