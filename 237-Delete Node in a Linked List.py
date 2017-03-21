'''
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3, 
the linked list should become 1 -> 2 -> 4 after calling your function.
'''

# -------------------------------------------------------------------------------------------------、
# 这题没提供测试方法，所以并没有AC，参照下面的解释和代码，就是将node逐一向前替换
# 这是一个非常简单的单链表的题，稍微拐了一点弯。一般删除一个节点是通过上一个节点来操作，
# 现在只给了当前节点，那么只能将后一节点的值赋给当前节点，将后一节点删掉，则相当于删掉了“当前节点”。
# -------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

   
# -------------------------------------------------------------------------------------------------



# -------------------------------------------------------------------------------------------------
# 
# -------------------------------------------------------------------------------------------------