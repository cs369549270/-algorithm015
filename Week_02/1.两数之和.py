#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for k,v in enumerate(nums):
            if target - v in d:
                return [d[target-v],k]
            d[v] = k
# @lc code=end

