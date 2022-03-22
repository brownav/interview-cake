'''
Reverse a singly linked list

Input: 1->2->3->4->5
Output: 5->4->3->2->1
'''

class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution():
    def reverse_list(self, head: ListNode) -> ListNode:
        curr, prev = head, None

        while curr:
            tmp  = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev

    def print_list(self, head: ListNode) -> None:
        curr = head
        while curr:
            print(curr.val)
            curr = curr.next

# Driver code
sol = Solution()
head = ListNode(1, ListNode(2, ListNode(3)))
sol.print_list(head)
new_head = sol.reverse_list(head)
print()
sol.print_list(new_head)
