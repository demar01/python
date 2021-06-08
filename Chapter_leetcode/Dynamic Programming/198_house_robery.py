


# nums = [2,7,9,3,1]
# rob, not_rob = 0, 0
# for num in nums:
#     rob, not_rob= not_rob + num, max(rob, not_rob)
#     print(rob, not_rob)

def rob(nums):
        rob, not_rob = 0, 0
        for num in nums:
            rob, not_rob = not_rob + num, max(rob, not_rob)
        return max(rob, not_rob)