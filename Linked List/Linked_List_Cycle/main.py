from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize slow pointer
        slow = head
        # Initialize fast pointer
        fast = head

        # Iterate until fast points to null or next node of fast becomes null
        while fast and fast.next:
            # Update slow pointer
            slow = slow.next
            # Update fast pointer
            fast = fast.next.next

            # If both pointers meet, then there is a cycle
            if slow == fast:
                return True
        
        return False