#https://leetcode.com/study-plan/dynamic-programming/?progress=wea3zss

class Solution(object):
    memo = dict()
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
          return 0
        elif n == 1:
          return 1
        elif self.memo.get(n) == None:
          self.memo[n] = self.fib(n-1) + self.fib(n-2)
        return self.memo[n]