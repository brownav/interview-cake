from typing import Optional

"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Input: head = [1,1,2]
Output: [1,2]

Input: head = [1,1,2,3,3]
Output: [1,2,3]
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def delete_duplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        curr = head
        while curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head

    def print_ll(self, head):
        if not head:
            return None

        curr = head
        while curr:
            print(curr.val)
            curr = curr.next


# Driver code
head = ListNode(1, ListNode(1, ListNode(2)))
solution = Solution()
head2 = solution.delete_duplicates(head)
solution.print_ll(head2)
