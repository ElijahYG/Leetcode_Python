'''
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
For example:
Given BST [1,null,2,2],
   1
    \
     2
    /
   2
return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).

给定具有重复的二叉搜索树（BST），找到给定BST中的所有模式（最频繁出现的元素）。

假设BST定义如下：

节点的左子树仅包含键小于或等于节点键的节点。
节点的右子树仅包含键大于或等于节点键的节点。
左和右子树都必须是二叉搜索树。

For example:
Given BST [1,null,2,2],
   1
    \
     2
    /
   2
return [2].

注意：如果树有多个模式，您可以按任何顺序返回它们。

跟进：你能没有使用任何额外的空间吗？ （假设由于递归导致的隐式堆栈空间不计数）。

'''

# -------------------------------------------------------------------------------------------------
# 完全不懂
# -------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
    

S = Solution()
print(S.findMode([1,null,2,2]))

      
# -------------------------------------------------------------------------------------------------



# ------------------------------------------草稿---------------------------------------------------

# -------------------------------------------------------------------------------------------------




# --------------------------------------Best Result------------------------------------------------
# from collections import defaultdict
# class Solution(object):
#     def helper(self, root, cache):
#         if root == None:
#             return 
#         cache[root.val] += 1
#         self.helper(root.left, cache)
#         self.helper(root.right, cache)

    
#     def findMode(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[int]
#         """
#         if root == None:
#             return []
#         cache = defaultdict(int)
#         self.helper(root, cache)
#         max_freq = max(cache.values())
#         result = [k for k,v in cache.items() if v == max_freq]
#         return result
# -------------------------------------------------------------------------------------------------

