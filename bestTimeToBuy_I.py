# Since the loop runs (n - 1) times and each operation within the loop is O(1), the overall time complexity is O(n).

prices = [7,1,5,3,6,4]

class Solution:
    def maxProfit(self,prices:list[int]) -> bool:

        left = 0
        right = 1
        maxProfit = 0

        while right < len(prices):
            if prices[left] < prices[right]:  
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit,profit)
            else:
                left = right
            right += 1

        return maxProfit
        

sol = Solution()
result = sol.maxProfit(prices)
print(result)
