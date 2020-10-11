#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        a,b = len(text1),len(text2)
        dp = [[0]*b for _ in range(a)]
        for i in range(a):
            for j in range(b):
                if text1[i]==text2[j]:
                    dp[i][j] = (dp[i-1][j-1] if i>0 and j>0 else 0)+1
                else:
                    dp[i][j] = max((dp[i][j-1] if j>0 else 0),(dp[i-1][j] if i>0 else 0))
        print(dp)
        return dp[-1][-1]
# @lc code=end

