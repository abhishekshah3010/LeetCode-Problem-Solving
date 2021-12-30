"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the first Node
    @return: the answer after plus one
    """
    def plusOne(self, head):

        reversedList = self.Reverse(head) 
        cur = reversedList
        res = None
        carrying = 1
        
        while cur:
            temp = cur.val + carrying;
            cur.val = temp % 10;
            carrying = temp // 10;
            res = cur;
            cur = cur.next;
        
        if carrying != 0:
            res.next = ListNode(carrying)
        return self.Reverse(reversedList)
        

    def Reverse(self,head):
        res = None
        cur = head
        while cur:
            temp = cur.next;
            cur.next = res;
            res = cur;
            cur = temp;
        return res
