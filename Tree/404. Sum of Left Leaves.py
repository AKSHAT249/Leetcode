# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        left_leaves_sum = 0

        q = deque()
        q.append(root)
        while len(q):
            levelSize = len(q)
            for i in range(levelSize):
                curr = q.popleft()
                
                if curr.left!=None:
                    if curr.left.left==None and curr.left.right==None:
                        left_leaves_sum+= curr.left.val
                    q.append(curr.left)
                if curr.right!=None: q.append(curr.right)
        return left_leaves_sum
