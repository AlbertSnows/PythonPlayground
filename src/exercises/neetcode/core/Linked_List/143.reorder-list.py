"""
143. Reorder List
Difficulty: Medium
https://leetcode.com/problems/reorder-list/

──────────────────────────────────────────────────

You are given the head of a singly linked-list. The list can be
represented as:

L0 &rarr; L1 &rarr; &hellip; &rarr; Ln - 1 &rarr; Ln

Reorder the list to be on the following form:

L0 &rarr; Ln &rarr; L1 &rarr; Ln - 1 &rarr; L2 &rarr; Ln - 2 &rarr;
&hellip;

You may not modify the values in the list's nodes. Only nodes
themselves may be changed.

 

Example 1:

Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:

Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

 

Constraints:

	• The number of nodes in the list is in the range [1, 5 * 10^4].

	• 1 <= Node.val <= 1000
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
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
        ([1, 2, 3, 4], [1, 4, 2, 3]),
        ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
    ]
    for (values, expected) in tests:
        head = build_list(values)
        sol.reorderList(head)
        result = list_to_values(head)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: reorderList({values}) -> {result} (expected {expected})")
