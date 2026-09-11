Definition for singly-linked list.

class ListNode:
	def __init__(self, x):
		self.val = x
        	self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a =headA
        b=headB
        while a!=b:
            if a is not None :
                a =a.next 
            else :
                a=headB
            if b is not None :
                b =b.next 
            else :
                b=headA
        return a

