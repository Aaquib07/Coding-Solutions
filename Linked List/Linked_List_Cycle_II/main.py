from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize slow pointer
        slow = head
        # Initialize fast pointer
        fast = head

        # Iterate until fast point to null or next node of fast becomes null
        while fast and fast.next:
            # Update slow pointer
            slow = slow.next
            # Update fast pointer
            fast = fast.next.next

            # If both pointers meet (there is a cycle)
            if slow == fast:
                # Initialize slow pointer again
                slow = head

                # Iterate until both pointers meet again
                while slow != fast:
                    # Update slow pointer
                    slow = slow.next
                    # Update fast pointer
                    fast = fast.next
                
                # Starting position of cycle
                return slow
        
        # If no cycle found
        return None