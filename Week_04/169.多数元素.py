#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return nums[0]
        d = {}
        for i in nums:
            d[i] = d.get(i,0)+1
            if d[i] > l/2:
                return i
# @lc code=end

