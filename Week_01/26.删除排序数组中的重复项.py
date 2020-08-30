#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        a = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            if nums[i] >= a:
                del nums[i]
            else:
                a = nums[i]
        return len(nums)
# @lc code=end

