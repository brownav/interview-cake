'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Input: head = [1,2], n = 1
Output: [1]
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head: return None

        # two pointer solution
        fast = slow = head

        # advance fast by n
        for i in range(n):
            fast = fast.next

        # check for edge case where size == n
        if not fast:
            return head.next

        # advance fast and slow until fast hits end, difference will be n
        while fast.next:
            fast = fast.next
            slow = slow.next

        # slow is stopped at len - n, skip over n
        slow.next = slow.next.next
        return head

    def print_ll(self, head: ListNode):
        curr = head
        while curr:
            print(curr.val)
            curr = curr.next


# Driver code
sol = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
sol.print_ll(head)
print()
head2 = sol.removeNthFromEnd(head, 2)
sol.print_ll(head2)
