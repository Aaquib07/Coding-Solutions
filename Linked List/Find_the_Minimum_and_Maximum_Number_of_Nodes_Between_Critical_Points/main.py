from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        result = [-1, -1]

        # Initialize minimum distance to be the max possible distance
        min_distance = float('inf')

        # Pointers to track the previous node, current node and indices
        previous_node = head
        current_node = head.next
        current_index = 1
        previous_critical_index = 0
        first_critical_index = 0

        while current_node.next:
            # Check if the current node is a local maxima or minima
            if (current_node.val < previous_node.val and current_node.val < current_node.next.val) or (current_node.val > previous_node.val and current_node.val > current_node.next.val):
                # If this is the first critical point
                if previous_critical_index == 0:
                    previous_critical_index = current_index
                    first_critical_index = current_index
                else:
                    # Calculate min distance between critical points
                    min_distance = min(min_distance, current_index - previous_critical_index)
                    previous_critical_index = current_index
            
            # Move to the next node and update indices
            current_index += 1
            previous_node = current_node
            current_node = current_node.next
        
        # If at least two critical points were found
        if min_distance != float('inf'):
            max_distance = previous_critical_index - first_critical_index
            result = [min_distance, max_distance]
        
        return result


if __name__ == '__main__':
    head = ListNode(5)
    a = ListNode(3)
    b = ListNode(1)
    c = ListNode(2)
    d = ListNode(5)
    e = ListNode(1)
    f = ListNode(2)

    head.next = a
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    result = Solution().nodesBetweenCriticalPoints(head)
    print(result)
