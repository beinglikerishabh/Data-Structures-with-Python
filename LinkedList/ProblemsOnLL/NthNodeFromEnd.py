""" Use the Driver program for 
    running the code as i have just uploaded the methode
    to be included in the LinkedList Class while creating the ADT    """


def nthNodeFromEnd(self, n):  # if we wanna use it as function instead of methode
    if n < 0:  # we need to send the object of linked list of which nth node to be found
        return None
    temp = self.head
    count = 0
    while count < n and temp != None:
        temp = temp.next
        count += 1
    if count < n or temp == None:
        print("linked list doesn't contain n elements")
        return
    nth = self.head
    while temp != None:
        temp = temp.next
        nth = nth.next
    return nth

