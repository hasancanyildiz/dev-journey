# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp = ListNode(0)
        temp.next =head

        simdiki = temp
        while simdiki.next is not None:
            if simdiki.next.val ==val :
                simdiki.next =simdiki.next.next
            else :
                simdiki =simdiki.next

        return temp.next

        
