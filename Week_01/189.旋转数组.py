#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 将被动移动的元素一个个复制到列表末尾，再删除掉被复制的列表片段
        m = 0
        for i in range(len(nums)-k%len(nums)):
            nums.append(nums[i])
            m += 1
        del nums[:m]
# @lc code=end

