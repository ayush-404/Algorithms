#Asked in Amazon
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        diff = 0
        curr_smallest = prices[0]
        for i in range(1, len(prices)):
          if prices[i] < curr_smallest:
            curr_smallest = prices[i]
          else: 
            if prices[i] - curr_smallest > diff:
              diff = prices[i] - curr_smallest
        return diff