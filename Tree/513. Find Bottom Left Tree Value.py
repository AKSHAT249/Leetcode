# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        result = []
        q = deque()
        q.append(root)

        while len(q):
            levelSize = len(q)
            liste = []
            for i in range(levelSize):
                curr = q.popleft()
                liste.append(curr.val)

                if curr.left!=None: q.append(curr.left)
                if curr.right!=None: q.append(curr.right)
            result.append(liste)
        return result[-1][0]

