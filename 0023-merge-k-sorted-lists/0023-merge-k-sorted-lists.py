# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy

        # Min-heap: (node_value, index, node)
        # index breaks ties when values are equal (ListNode isn't comparable)
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        while heap:
            val, i, node = heapq.heappop(heap)

            current.next = node
            current = current.next

            # Push the next node from the same list
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next
        