class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max profit is buy the lowest and sell the highest 
        # consider negative numbers
        # the order of lowest needs to be earlier than highest
        # if all the earlier ones are larger than the later ones
        # return 0 
        # dynamic sliding window

        min_val, max_profit = float('inf'), float('-inf')

        for i in range(len(prices)): 
            min_val = min(min_val, prices[i])
            max_profit = max(max_profit, prices[i]-min_val)
         

        return max_profit if max_profit > 0 else 0