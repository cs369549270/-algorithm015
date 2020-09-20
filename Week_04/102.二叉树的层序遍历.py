#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        visited = []
        queue = []
        if root:
            queue.append([root])
        while queue:
            node = queue.pop()
            child = []
            r = []
            for i in node:
                r.append(i.val)
                if i.left:
                    child.append(i.left)
                if i.right:
                    child.append(i.right)
            visited.append(r)
            if child:
                queue.append(child)
        return visited
# @lc code=end

