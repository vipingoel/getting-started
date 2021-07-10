# https://www.hackerearth.com/practice/algorithms/sorting/bucket-sort/tutorial/
import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data):
        self.root = Node(data)

    def insert_in_order(self, data):
        node = Node(data)
        if not self.root:
            self.root = node
            return

        prev = None
        current = self.root
        while current and current.data < data:
            prev, current = current, current.next

        if not prev:
            # insert at the first position
            self.root, node.next = node, current
        else:
            prev.next, node.next = node, current

    def __repr__(self) -> str:
        res = ""
        current = self.root
        while current:
            res += str(current.data) + " "
            current = current.next
        return res


def count_set_bits(x):
    count = 0
    while x > 0:
        if x & 1:
            count += 1
        x >>= 1
    return count


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    set_bits = [0]*n
    max_set_bits = 0
    for i in range(n):
        count = count_set_bits(arr[i])
        set_bits[i] = count
        max_set_bits = max(max_set_bits, count)
    buckets = [None]*(max_set_bits+1)
    for i in range(n):
        bucket = buckets[set_bits[i]]
        if bucket:
            bucket.insert_in_order(arr[i])
        else:
            buckets[set_bits[i]] = LinkedList(arr[i])
    for bucket_list in buckets:
        if bucket_list:
            print(bucket_list)
