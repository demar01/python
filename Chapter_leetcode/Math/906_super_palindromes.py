class Solution:
    nums = []
    for i in range(1, 10**5):
        #odd or even number of digits
        odd = int(str(i)+str(i)[:-1][::-1])**2 #get rid of first character and reverse it
        even = int(str(i)+str(i)[::-1])**2 #we reverse it
            
        if str(odd) == str(odd)[::-1]: #then is a palindrome
            nums.append(odd)
                
        if str(even) == str(even)[::-1]:
            nums.append(even)
        
    nums = sorted(list(set(nums)))
    def superpalindromesInRange(self, left: str, right: str) -> int:
        #all possible super palindromes
        output = []
        for n in self.nums: #numbs becomes a self variable
            if int(left) <= n <= int(right): #if is imbalance
                output.append(n)
                
        return len(output)
            
        
        