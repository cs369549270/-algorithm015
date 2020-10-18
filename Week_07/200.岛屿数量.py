#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        res = 0
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        def dfs_marking(i, j):
            grid[i][j] = '#'
            for di, dj in dirs:
                _i, _j = i + di, j + dj
                if -1 < _i < m and -1 < _j < n and grid[_i][_j] == '1':
                    dfs_marking(_i, _j)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    dfs_marking(i, j)
        return res
# @lc code=end

