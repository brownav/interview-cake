"""
# Merge two sorted singly-linked lists into third new list

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Constraints:
* The number of nodes in both lists is in the range [0, 50].
* -100 <= Node.val <= 100
* Both list1 and list2 are sorted in non-decreasing order.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if not list1 or not list2:
            return []

        curr = ListNode(-1)
        head = curr

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        return head.next

    def print_ll(self, head: ListNode) -> None:
        curr = head
        while curr:
            print(curr.val)
            curr = curr.next


# Driver Code
solution = Solution()
head = solution.mergeTwoLists(
    ListNode(1, ListNode(2, ListNode(4))), ListNode(1, ListNode(3, ListNode(4)))
)
solution.print_ll(head)
