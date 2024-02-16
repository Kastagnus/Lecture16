class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print(f"Added first element: {new_node.data}")
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        print(f"New element: {new_node.data}, has been added !")

    def remove(self):
        if self.head is None:
            return None
        if self.head.next is None:
            self.head = None
            return
        second_last_node = self.head
        while second_last_node.next.next:
            second_last_node = second_last_node.next
        second_last_node.next = None
        print("Removed last element from linked list")


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.remove()
