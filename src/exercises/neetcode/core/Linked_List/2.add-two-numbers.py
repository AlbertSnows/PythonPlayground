"""
2. Add Two Numbers
Difficulty: Medium
https://leetcode.com/problems/add-two-numbers/

──────────────────────────────────────────────────

You are given two non-empty linked lists representing two
non-negative integers. The digits are stored in reverse order, and
each of their nodes contains a single digit. Add the two numbers and
return the sum as a linked list.

You may assume the two numbers do not contain any leading zero,
except the number 0 itself.

 

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

	• The number of nodes in each linked list is in the range [1, 100].

	• 0 <= Node.val <= 9

• It is guaranteed that the list represents a number that does not
have leading zeros.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        pass


def build_list(values):
    head = None
    tail = None
    for v in values:
        node = ListNode(v)
        if head is None:
            head = node
        else:
            tail.next = node
        tail = node
    return head


def list_to_values(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


if __name__ == "__main__":
    sol = Solution()
    tests = [
        (([2, 4, 3], [5, 6, 4]), [7, 0, 8]),
        (([0], [0]), [0]),
        (([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]), [8, 9, 9, 9, 0, 0, 0, 1]),
    ]
    for (args, expected) in tests:
        l1 = build_list(args[0])
        l2 = build_list(args[1])
        result_head = sol.addTwoNumbers(l1, l2)
        result = list_to_values(result_head)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: addTwoNumbers{args} -> {result} (expected {expected})")
