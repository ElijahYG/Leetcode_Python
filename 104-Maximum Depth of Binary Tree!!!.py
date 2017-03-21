'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''
'''
[5,4,7,3,null,2,null,-1,null,9]
       5
      / \
     4   7
    /   /
   3   2
  /   /
 -1  9

'''
# ------------------------------------------------------------------------------
#没有AC，需要再进行温习
#此题有两种思路：
#第一个是用DFS(Depth-Fisrt-Search)
#第二个是用BfS(Breadth-First-Search)
#此题比较经典，可以拓展练习Minimum Depth of Binary Tree
#此题自己不知道怎么测试，如何生成一个TreeNode类进行测试？
# ------------------------------------------------------------------------------

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if (root == None):
        	return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1


# -----------------------------------草稿----------------------------------------

# class Solution(object):
#     def maxDepth(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         Q = [root]
#         res = math.ceil(math.log(len(Q)+1))
#         return res


# S = Solution
# print(S.maxDepth([5,4,7,3,null,2,null,-1,null,9]))

# ------------------------------------------------------------------------------


# class Solution(object):
#     def maxDepth(self, root):
#         if (root == None):
#             return 0
#         left_depth = self.maxDepth(root.left)
#         right_depth = self.maxDepth(root.right)
#         return max(left_depth, right_depth) + 1


# Node = TreeNode()
# a1 = Node(5)
# b1 = Node(4)
# b2 = Node(7)
# c1 = Node(3)
# c2 = Node(2)
# d1 = Node(-1)
# d2 = Node(9)
 
# a1.left = b1
# a1.right = b2
# b1.left = c1
# b2.left = c2
# c1.left = d1
# c2.left = d2



# S = Solution
# print(S.maxDepth(a1))
# ------------------------------------------------------------------------------