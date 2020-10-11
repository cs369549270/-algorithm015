#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m==1 or n==1:
            return 1
        dp = [[0]*n]*m
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dp[i][j] = 0
                    continue
                if i>0 and j == 0:
                    dp[i][j] = 1
                    continue
                if i==0 and j>0:
                    dp[i][j] =1
                    continue
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
                # print(i,j,dp[i][j])
        return dp[m-1][n-1]
# @lc code=end

