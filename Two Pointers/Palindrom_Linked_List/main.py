from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        # helper function to reverse the linked list
        def reverse_list(node: Optional[ListNode]):
            prev = None
            current = node
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev
        
        # find the middle point of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the second half of the list
        reversed_second_half = reverse_list(slow)

        # compare the first half with the reversed second half
        first_half = head
        while reversed_second_half:
            if first_half.val != reversed_second_half.val:
                return False
            first_half = first_half.next
            reversed_second_half = reversed_second_half.next
        
        return True


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(1)

    solution = Solution().isPalindrome(head=head)
    print(solution)