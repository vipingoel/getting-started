# Enter your code here. Read input from STDIN. Print output to STDOUT

class TwoStackQueue:
    def __init__(self):
        self.forward_stack = []
        self.reverse_stack = []

    def dequeue(self):
        if not self.reverse_stack:
            while self.forward_stack:
                self.reverse_stack.append(self.forward_stack.pop())
        return self.reverse_stack.pop()

    def enqueue(self, element):
        self.forward_stack.append(element)

    def front(self):
        front = self.dequeue()
        # adding back to reverse as we only need to seek the front element
        self.reverse_stack.append(front)
        return front


def main():
    queue = TwoStackQueue()

    n = int(input())
    for i in range(n):
        query_input = input().split()
        query_type = int(query_input[0])

        if query_type == 1:
            queue.enqueue(int(query_input[1]))
        elif query_type == 2:
            queue.dequeue()
        elif query_type == 3:
            print(queue.front())
        else:
            raise Exception("invalid input")


main()
