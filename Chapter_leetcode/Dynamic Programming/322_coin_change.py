def coinChange(coins, amount):
    dp= [amount+1] * (amount +1 )
    #base case
    dp[0]=0
    #DP bottom up
    for a in range(1, amount +1):
        #brute force
        for c in coins:
            if a -c >=0:
                dp[a] = min(dp[a], 1 + dp[ a- c]) #1 + dp [7-4] is a possible solution. This is the recurrence relation.
                
    return dp[amount] if dp[amount] != amount + 1 else -1
    # if the value that is stored is not the default value. In that case we return -1 meaning we could not return that amount
                

# time complexity O(amount * len(coins))
# memory complexity O(amount) dp array that has a potential value for each variable in the array

#coins = [1,3,4,5]
#amount = 7
# coinChange(coins,amount)
#https://www.youtube.com/watch?v=H9bfqozjoqs


