
def maxProfit(prices):
    
    # It is impossible to have stock to sell on first day, so -infinity is set as initial value
    cur_hold, cur_not_hold = -float('inf'), 0
    
    
    for stock_price in prices:
        
        prev_hold, prev_not_hold = cur_hold, cur_not_hold
        
        # either keep in hold, or just buy today with stock price
        cur_hold = max(prev_hold, -stock_price)
        
        # either keep in not holding, or just sell today with stock price
        cur_not_hold = max(prev_not_hold, prev_hold + stock_price)
        
        
    # max profit must be in not-hold state
    return cur_not_hold if prices else 0
            

prices = [7,1,5,3,6,4]
maxProfit(prices)