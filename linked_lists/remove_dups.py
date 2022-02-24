# Problem no.1: Remove duplicates from an unsorted linked list
# Problem no.2: Find the kth to last element of a singly linked list
# Problem no.3: Reverse linked list

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head


    def append_node(self, node):
        if self.head is None:
            self.head = node
            return self.head

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node
        return self.head


    def prepend_node(self, node):
        if self.head is None:
            self.head = node
            return self.head

        node.next = self.head
        self.head = node
        return self.head


    # problem no. 1 solution
    def remove_dups(self):
        current = self.head
        node_values = set()

        while current.next is not None:
            node_values.add(current.data)
            if current.next.data in node_values:
                current.next = current.next.next
            else:
                current = current.next
        return self.head


    # problem no. 2 solution
    def kth_from_last(self, k):
        nodes = []
        current = self.head

        while current is not None:
            nodes.append(current.data)
            current = current.next

        key = len(nodes) - k
        return nodes[k]


    # problem no. 3 solution
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


    def print_ll(self):
        if self.head is None:
            print('empty list')
        else:
            current = self.head
            while current is not None:
                print(current.data)
                current = current.next

list1 = LinkedList()
nodea = Node(2)
nodeb = Node(5)
nodec = Node(3)
noded = Node(2)
nodee = Node(6)
nodef = Node(6)
list1.append_node(nodea)
list1.append_node(nodeb)
list1.append_node(nodec)
list1.append_node(noded)
list1.append_node(nodee)
list1.append_node(nodef)
list1.print_ll()
list1.kth_from_last(3)
# list1.remove_dups()
# list1.print_ll()
list1.reverse()
list1.print_ll()
