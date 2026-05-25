# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node that points to the head.
        # This gracefully handles edge cases like removing the first node.
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy
        
        # Move the fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next
            
        # Move both pointers together until fast reaches the last node
        while fast.next:
            fast = fast.next
            slow = slow.next
            
        # slow.next is now the node to be deleted. 
        # Skip it by changing the next pointer.
        slow.next = slow.next.next
        
        # Return the actual head of the modified list
        return dummy.next