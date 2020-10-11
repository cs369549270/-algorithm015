#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid ==[[]] :
            return 0
        m,n = len(obstacleGrid),len(obstacleGrid[0])
        for i in range(m):
            for j in range(n):
                # print(obstacleGrid)
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                    continue
                if i == 0 and j==0:
                    obstacleGrid[i][j]=1
                else:
                    obstacleGrid[i][j] = (obstacleGrid[i-1][j] if i-1>=0 else 0) + (obstacleGrid[i][j-1] if j-1>=0 else 0)
        return obstacleGrid[-1][-1]
# @lc code=end

