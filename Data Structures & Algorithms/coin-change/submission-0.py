class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # for each coin variation when u iterate through the list
        # as long as the sum is still lower than the amount
        # you have 2 choices either to add or not add 
        # kind of like while loop 

        # to get fewest number of coins u gotta start from the 
        # largest number in the list and u gotta do 
        # amount // largest num then add whatever to the result

        # find the remainder after adding the largest nums
        # then iterate to next part of the list 

        # can i sort and then go from the last part of the list
        # the greedy approach may not actually minimise the amount of coins

        # subproblem to make amount a, can use one coin of value c, 
        # then find the fewest coins to make a - c

        INF = amount + 1 
        dp = [INF] * (amount + 1)
        dp[0] = 0 

        for a in range(1, amount+1):
            for c in coins:
                # since c < a its basically a - c >= 0 
                # coins must be less than the amount
                if a - c >= 0: 
                    # 1 + dp[a-c] -> number of coins if we use
                    # one coin of the value c now 

                    # dp[a-c] = fewest coins needed 
                    dp[a] = min(dp[a], 1 + dp[a - c])

        return dp[amount] if dp[amount] != INF else -1
