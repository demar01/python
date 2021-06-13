class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        N= len(popped)
        i = 0 #pointer for popped
        for p in pushed:
            stack.append(p)
            while stack and i <N and stack[-1]==popped[i]:
                i+=1 #we move our point ahead
                stack.pop()
        return stack==[]

# Algorithm
# For each value, push it to the stack.
# Then, greedily pop values from the stack if they are the next values to pop.
# At the end, we check if we have popped all the values successfully.