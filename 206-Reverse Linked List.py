'''
Reverse a singly linked list.

click to show more hints.

Hint:
A linked list can be reversed either iteratively or recursively. Could you implement both?
反转单链表。

单击以显示更多提示。

暗示：
链接列表可以迭代地或递归地反转。 你能实现两者吗？
'''

# -------------------------------------------------------------------------------------------------
'''
leetcode中的链表和二叉树的题本地验证需要进行链表和二叉树的构造后进行验证，所以比较麻烦，建议直接在网页进行验证；
所谓链表就是提供了val和next两个方法的列表，val表示值，next表示链表的下一个节点
并没有AC，链表的题目还是需要重新回顾
'''
# -------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp=None
        while head:
            head.next,head,temp=temp,head.next,head
        return temp

  
# -------------------------------------------------------------------------------------------------



# -------------------------------------------草稿--------------------------------------------------

# -------------------------------------------------------------------------------------------------



# ----------------------------------------Best Result----------------------------------------------

# -------------------------------------------------------------------------------------------------        
