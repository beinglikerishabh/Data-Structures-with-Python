class Node:
    def __init__(self, val):
        self.data = val
        self.next = None  # class for defining the node of the list


class Lis:                                          # class for defining the list
    def __init__(self):
        self.head = None

    def listLength(self):
        if self.head is None:
            return 0
        else:
            counter = 1
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
                counter += 1
            return counter

    def printList(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            while temp.next != self.head:
                print(temp.data)
                temp = temp.next

    def insertAtBegin(self, data):
        newnode = Node(data)
        if self.head is None:
            newnode.next = self.head
            self.head = newnode
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            newnode.next = self.head
            temp.next = newnode
            self.head = newnode

    def insertAtEnd(self, data):
        newnode = Node(data)
        if self.head is None:
            newnode.next = self.head
            self.head = newnode
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            newnode.next = self.head
            temp.next = newnode

    def insertAtPos(self, val, pos):
        new_node = Node(val)
        count = 1
        current = self.head
        while count < pos - 1 and current.next != self.head:
            count += 1
            current = current.next
        if current == pos-1:
            new_node.next = current.next
            current.next = new_node
        else:
            return
