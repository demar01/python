
def longestConsecutive( nums):
    #The most efficient way to check membership is with a set. Each check is O(1).
    nums, longest = set(nums), 0
    
    for n in nums:
        #For each number, we will only consider it as a start if there is no number = n -1 so that we can fully count the longest potential sequence.
        if n - 1 not in  nums:
            start = n
            #We keep checking whether n+1 is in nums through the set and increment our count.
            while start in nums:
                start+=1
            longest=max(longest,start-n)
    return longest
    