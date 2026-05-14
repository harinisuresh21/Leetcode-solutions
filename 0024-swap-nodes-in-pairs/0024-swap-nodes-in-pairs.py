# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node that points to the head
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        # We need at least two nodes ahead to perform a swap
        while current.next and current.next.next:
            # Identify the two nodes to swap
            first = current.next
            second = current.next.next
            
            # Start the swap:
            # 1. Point current node to the second node
            # 2. Point first node to whatever was after the second
            # 3. Point second node back to the first
            first.next = second.next
            second.next = first
            current.next = second
            
            # Move 'current' two nodes forward for the next pair
            current = first
            
        return dummy.next