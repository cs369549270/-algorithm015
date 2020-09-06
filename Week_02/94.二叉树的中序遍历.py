#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # 递归
        # if not root:
        #     return []
        # return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right)
        
        # 迭代
        r = []
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            r.append(root.val)
            root = root.right
        return r
# @lc code=end

