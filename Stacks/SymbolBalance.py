class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def isempty(self):
        return self.head == None

    def push(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode

    def pop(self):
        if self.isempty():
            return None
        else:
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            return poppednode.data

    def peek(self):
        if self.isempty():
            return None
        else:
            return self.head.data

    # Prints out the stack
    def display(self):
        iternode = self.head
        if self.isempty():
            print("Stack Underflow")
        else:
            while(iternode != None):
                print(iternode.data)
                iternode = iternode.next
            return

def checkBalance(input):
    symbolstack = Stack()
    balanced = None
    topsymbol = None
    for symbols in input:
        if symbols in ["[","{","("]:
            symbolstack.push(symbols)
        else:
            if symbolstack.isempty():
                balanced = False
            else:
                topsymbol = symbolstack.pop()
                if  symbols == ")" and topsymbol == "(":
                    balanced = True
                elif symbols == "}" and topsymbol == "{":
                    balanced = True
                elif symbols == "]" and topsymbol == "[":
                    balanced = True
                else:
                    balanced = False
    return balanced

print(checkBalance("{[][][]([])}"))
