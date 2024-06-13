# Problem
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, `pos` is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle.

**Note that `pos` is not passed as a parameter.**

**Do not modify the linked list.**

### Constraints
- The number of the nodes in the list is in the range [ 0, 10<sup>4</sup> ].
- -10<sup>5</sup> <= Node.val <= 10<sup>5</sup>
- `pos` is -1 or a valid index in the linked-list.

# Solution
## Approach (TC: O(N), SC: O(1))
We start by initializing two pointers, namely `slow` and `fast`. At the start, both pointers point to the head of the Linked List. Then we start iterating until `fast` becomes null or the next node pointed to by `fast` becomes null. During the iteration, `slow` pointer jumps by one node and `fast` pointer jumps by two nodes. If both the pointers meet at some point, that means there is a cycle in the Linked List. We update the `slow` pointer to point to the head again and start iterating again but this time both pointers jump by one node. If both pointers meet again, that position will be the starting position of the cycle.

**Code for this approach is given in the python file**