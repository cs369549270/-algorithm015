#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        a,b = 1,0
        for i in range(n):
            a,b = a+b,a
        return a 
# @lc code=end

