#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = collections.defaultdict(int)
        for i in range(len(s)):
            d[s[i]] += 1
            d[t[i]] -= 1
        for j in d.values():
            if j != 0:
                return False
        return True
# @lc code=end

