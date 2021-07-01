""" Use the Driver program for 
    running the code as i have just uploaded the methode
    to be included in the LinkedList Class while creating the ADT    """


def cycle(self):
    fastptr = self.head
    slowptr = self.head
    # ensure the list is not empty  somewhere ahead.
    while(fastptr and slowptr):
        fastptr = fastptr.next  # fast pointer takes first step
        if fastptr == slowptr:
            return True  # both pointer match means there is a loop
        if fastptr is None:
            return False  # there is no loop as List terminated.
        fastptr = fastptr.next  # second step of the fast pointer
        if fastptr == slowptr:
            return True  # both pointer match means there is a loop
        slowptr = slowptr.next  # first step of slow pointer
