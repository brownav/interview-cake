# Remove Dups: Write code to remove duplicates from an unsorted linked list
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def add_node(self, node):
        if self.head is None:
            self.head = node
            return self.head

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node
        return self.head

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

    def print_ll(self):
        if self.head is None:
            print('empty list')
        else:
            current = self.head
            print(current.data)
            while current.next is not None:
                current = current.next
                print(current.data)

list1 = LinkedList(Node(0))
nodea = Node(2)
nodeb = Node(5)
nodec = Node(3)
noded = Node(2)
nodee = Node(6)
nodef = Node(6)
list1.add_node(nodea)
list1.add_node(nodeb)
list1.add_node(nodec)
list1.add_node(noded)
list1.add_node(nodee)
list1.add_node(nodef)
list1.print_ll()
list1.remove_dups()
list1.print_ll()