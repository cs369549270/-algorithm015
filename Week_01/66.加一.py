#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return list(int(x) for x in str(int("".join(map(str,digits)))+1))
# @lc code=end

