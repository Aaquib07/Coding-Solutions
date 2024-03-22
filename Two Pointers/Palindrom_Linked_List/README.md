# Problem
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

### Constraints
- The number of nodes in the list is in the range [1, 10^5^].
- 0 <= Node.val <= 9

# Solution
## Approach (TC: O(N), SC: O(1))
The idea is that at first we are gonna find the middle node of the linked list. Then reverse the right half of the list starting from the middle node and lastly compare each node from the left half with the corresponding node from the right half. If all of the values match we return True otherwise we return False.

So, initially we take 2 pointers - `slow` and `fast`. We increment slow pointer by one node and fast pointer by two nodes. Whenever fast pointer becomes null or the next node of fast pointer becomes null, we stop the iteration. Now our slow pointer contains the middle node. After this, we initialize a pointer `prev` that is used for reversing the list and start reversing the list from the middle node. We take the middle node as the `current` and modify its next node to be `prev` and update the `prev` and `current` pointers. Lastly, we compare each node from left and right half based on their values.