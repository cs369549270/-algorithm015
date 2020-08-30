#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = 0
        k = 0
        while n < len(nums):
            if nums[k]==0:
                del nums[k]
                nums.append(0)
            else:
                k += 1
            n+=1

# @lc code=end

