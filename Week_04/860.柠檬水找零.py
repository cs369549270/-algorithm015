#
# @lc app=leetcode.cn id=860 lang=python3
#
# [860] 柠檬水找零
#

# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five,ten = 0,0
        for i in bills:
            if i == 5:
                five += 1
            if i == 10:
                five -= 1
                ten += 1
            if i == 20:
                ten -= 1
                five -= 1
            if ten <0:
                five -= 2
                ten += 1
            if five < 0:
                return False
        return True
# @lc code=end

