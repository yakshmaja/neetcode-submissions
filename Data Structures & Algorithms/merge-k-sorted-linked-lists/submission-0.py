# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        values=[]
        for head in lists:
            while head:
                values.append(head.val)
                head = head.next
        if not values:
            return None
            
        values.sort()

        dummy = ListNode(0)
        curr = dummy
        for v in values:
            curr.next = ListNode(v)
            curr = curr.next
            
        return dummy.next
        