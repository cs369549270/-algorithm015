#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = collections.defaultdict(list)
        for i in strs:
            count = [0]*26
            for j in i:
                count[ord(j)-ord("a")] += 1
            l[tuple(count)].append(i)
        return list(l.values())
# @lc code=end

