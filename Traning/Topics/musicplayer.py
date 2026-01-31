class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def specific_position(self, data, position):
        if position < 0:
            print("Invalid position")
            return

        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        for _ in range(position - 1):
            if temp is None:
                print("Position out of range")
                return
            temp = temp.next

        if temp is None:
            print("Position out of range")
            return

        new_node.next = temp.next
        temp.next = new_node

    def display(self):
        current = self.head
        if current is None:
            print("List is empty")
            return

        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def middle(self):
        if self.head is None:
            return None

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data

    def search(self, key):
        current = self.head
        position = 1

        while current:
            if current.data == key:
                return position
            current = current.next
            position += 1

        return -1

    def delete_from_beginning(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next

    def delete_from_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None