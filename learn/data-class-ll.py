'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
from dataclasses import dataclass

# Write your code here


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return f"({self.data})"


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self) -> str:
        repr = ""
        for node in self:
            repr += str(node) + " -> "
        repr += "None"
        return repr

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def tail_node(self):
        current = self.head
        if not current:
            return current
        while current.next:
            current = current.next
        return current

    def append(self, data):
        node = Node(data)
        tail = self.tail_node()
        if tail:
            tail.next = node
        else:
            self.head = node

    def reverse(self):
        prev = None
        current = self.head
        while current:
            current.next, prev, current = prev, current, current.next
        self.head = prev


def main():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    print(ll)
    ll.reverse()
    print(ll)


main()
