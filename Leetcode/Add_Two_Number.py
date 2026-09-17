"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        # Carry stores the extra digit produced when a column sum is 10 or more.
        carry = 0

        # A dummy node makes it easy to build the result list from the first digit.
        dummy_head = ListNode(0)
        current = dummy_head

        # Continue while either list has digits or a final carry remains.
        while l1 or l2 or carry:
            # Use 0 when one list is shorter than the other.
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Add the current digits and the carry from the previous column.
            total = val1 + val2 + carry
            carry = total // 10

            # Store the current digit in the result and move to its last node.
            current.next = ListNode(total % 10)
            current = current.next

            # Advance each input list when it still has a node.
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # Skip the dummy node and return the actual sum list.
        return dummy_head.next