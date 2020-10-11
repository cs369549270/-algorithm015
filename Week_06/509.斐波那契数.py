#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
class Solution:
    @lru_cache()
    def fib(self, N: int) -> int:
        return N if N == 0 or N == 1 else self.fib(N-1)+self.fib(N-2)

        # a,b = 0,1
        # for i in range(N):
        #     a,b = a+b,a
        # return a
# @lc code=end

