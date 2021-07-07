class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        sl=len(list(set(candyType))) # count  of different candies.
        a=len(candyType)/2 # count of how many he can eat.
        if a>sl: # if count of how many he can it is greter than count of available candies we return available candies count
            return int(sl) 
        return int(a) # else if count of available candies is greter than he can eat we return maximum no. that is a which he can eat