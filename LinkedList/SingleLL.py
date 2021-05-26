class Node:
    def __init__(self, val):
        self.data = val
        self.next = None  # class for defining the node of the list


class Lis:                                          # class for defining the list
    def __init__(self):
        self.head = None                        # initially the head is none
        self.length = 0             # length of the list will b described

    def insert_at_begin(self, val):
        new_node = Node(val)  # constructor call for the node
        if self.length == 0:  # checking the length of the node if its 0 or not
            self.head = new_node  # if the length is zero then put the first node as new node
        else:
            new_node.next = self.head  # putting the new node as the first node
            self.head = new_node  # setting the head as the first node of the list
        self.length += 1  # increasing the lentgh of the list by 1

    def insert_at_end(self, val):
        new_node = Node(val)  # creating the new node by constructor
        current = self.head
        while current.next is not None:  # travellling to the last node of the list
            current = current.next
        current.next = new_node  # setting newnode the last node of the list
        self.length += 1

    def insert_at_pos(self, val, pos):
        if pos < 0 or pos > self.length+1:
            return None
        else:
            if pos == 0:
                self.insert_at_begin(val)
            else:
                if pos - 1 == self.length:
                    self.insert_at_end(val)
                else:
                    new_node = Node(val)
                    count = 1
                    current = self.head
                    while count < pos - 1:
                        count += 1
                        current = current.next
                    new_node.next = current.next
                    current.next = new_node
                    self.length += 1

    def delete_first(self):
        if self.length == 0:
            print("list is empty")
        else:
            self.head = self.head.next
            self.length -= 1

    def delete_last(self):
        if self.length == 0:
            print("list is empty")
        else:
            current_node = self.head
            pre_node = self.head
            while current_node.next is not None:
                pre_node = current_node
                current_node = current_node.next
            pre_node.next = None
            self.length -= 1

    def delete_at_pos(self, pos):
        if self.length < pos or pos < 0:
            print("pos is not valid")
            return
        else:
            count = 0
            current = self.head
            pre = self.head
            while current.next is not None or count < pos:
                pre = current
                current = current.next
                count += 1
            if current.next is None:
                print("pos not exist")
                return
            else:
                pre.next = current.next
                self.length -= 1
                return

    def delete_by_value(self, val):
        current = self.head
        pre = self.head
        while current.next is not None or current.data != val:
            pre = current
            current = current.next
        if current.next is None and current.data != val:
            print("value doesnt exist")
            return
        else:
            pre.next = current.next
            self.length -= 1
            return

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end="  ")
            current = current.next
        print("")


if __name__ == '__main__':
    list1 = Lis()
    list1.insert_at_begin(11)
    list1.print_list()
    list1.insert_at_end(13)
    list1.print_list()
    list1.insert_at_pos(12, 2)
    list1.print_list()
    list1.delete_first()
    list1.print_list()
    list1.delete_last()
    list1.print_list()
    list1.delete_at_pos(4)
    list1.print_list()
    list1.delete_by_value(12)
    list1.print_list()
