class Solution:
    def isHappy(self, n: int) -> bool:
        #20 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 > 42 -> 20
        slow = self.squared(n)
        fast = self.squared(self.squared(n))
        while slow!=fast and fast!=1:
            slow = self.squared(slow)
            fast = self.squared(self.squared(fast))
        return fast==1
    def squared(self, n):
        result = 0
        while n>0:
            last = n%10
            result += last * last
            n = n//10
        return result
        