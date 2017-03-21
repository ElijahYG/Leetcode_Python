'''
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:
Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so fuck off.
'''

# ------------------------------------------------------------------------------
#没有AC，对于二叉树不知道怎么自己测试
#要自己写一个题，Input一个列表，Output一个二叉树
#测试Tree:[5,4,7,3,8,2,null,-1,null,9]
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
    

# [5,4,7,3,8,2,1,-1,5,9]
# [5,7,4,1,2,8,3,null,null,null,null,null,9,5,-1]    
# ------------------------------------------------------------------------------


# ---------------------------------Best Result----------------------------------
# # recursively
# def invertTree(self, root):
#     if root:
#         root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
#         return root
        
# # BFS
# def invertTree(self, root):
#     queue = collections.deque([(root)])
#     while queue:
#         node = queue.popleft()
#         if node:
#             node.left, node.right = node.right, node.left
#             queue.append(node.left)
#             queue.append(node.right)
#     return root
    
# # DFS
# def invertTree(self, root):
#     stack = [root]
#     while stack:
#         node = stack.pop()
#         if node:
#             node.left, node.right = node.right, node.left
#             stack.extend([node.right, node.left])
#     return root
# ------------------------------------------------------------------------------

# --------------------------------草稿------------------------------------------
# [5,4,7,3,null,2,null,-1,null,9]
#        5
#       / \
#      4   7
#     /   /
#    3   2
#   /   /
#  -1  9
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# a1 = TreeNode(5)
# b1 = TreeNode(4)
# b2 = TreeNode(7)
# c1 = TreeNode(3)
# c2 = TreeNode(2)
# d1 = TreeNode(-1)
# d2 = TreeNode(9)
 
# a1.left = b1
# a1.right = b2
# b1.left = c1
# b2.left = c2
# c1.left = d1
# c2.left = d2

# String =''.join(str(a1.val)) + ''.join(str(b1.val)) + ''.join(str(b2.val)) + 
# ''.join(str(c1.val)) + ''.join(str(c2.val)) + ''.join(str(d1.val)) + ''.join(str(d2.val))


# print(list(String))
# ------------------------------------------------------------------------------