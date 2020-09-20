#
# @lc app=leetcode.cn id=433 lang=python3
#
# [433] 最小基因变化
#

# @lc code=start
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        # bank = set(bank)
        letter = ["A","C","G","T"]
        queue = [(start,0)]
        while queue:
            word,step = queue.pop(0)
            if word == end:
                return step
            for i in range(len(word)):
                for l in letter:
                    r = word[:i]+l+word[i+1:]
                    if r in bank:
                        bank.remove(r)
                        queue.append((r,step+1))
        return -1
# @lc code=end

