class Node:                     # definig the class for the node type variable
    def __init__(self):
        self.data = None
        self.next = None
        self.pre = None


class Lis:                         # definig the list class having all the methods in it
    def __init__(self):                # constructor for defining the head
        # initially head will be none will be modified when node is inserted
        self.head = None

    def insert_at_begin(self, val):             # insert at beginning function
        new_node = Node()
        new_node.data = val
        if self.head is None:                   # if list is empty then head will point on the new_node
            self.head = new_node
        else:
            # modifying the new_node pointers so as to manipulate the list
            new_node.pre = None
            new_node.next = self.head
            self.head.pre = new_node
            self.head = new_node

    def insert_at_end(self, val):                   # inserting at end function
        new_node = Node()
        new_node.data = val
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:             # looop will run until the current points the last node
                current = current.next
            new_node.pre = current
            current.next = new_node

    def insert_at_pos(self, val, pos):
        if self.head is None or pos == 1:                   # situation is of the type of insert at begin
            self.insert_at_begin(val)
            return
        elif pos > 0:
            new_node = Node()
            new_node.data = val
            k = 1
            current = self.head
            n = self.head
            # running the loop for  pos-1 and adding node after this position
            while k < pos - 1 and current.next is not None:
                n = current
                current = current.next
            if k == pos - 1:
                n.next = new_node
                new_node.pre = n
                new_node.next = current
                current.pre = new_node
                return
            elif current.next is None:
                print("position not exist")

    def delete_first(self):
        self.head = self.head.next
        self.head.pre = None

    def delete_last(self):
        if self.head is None:
            print("list is empty")
            return
        else:
            current_node = self.head
            pre_node = self.head
            while current_node.next is not None:
                pre_node = current_node
                current_node = current_node.next
            pre_node.next = None

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end="  ")
            current = current.next
        print("")


if __name__ == '__main__':
    list1 = Lis()
    list1.insert_at_begin(25)
    list1.print_list()
    list1.insert_at_end(29)
    list1.print_list()
    list1.insert_at_pos(27, 1)
    list1.print_list()
